'''
Created on Jan 19, 2018

@author: enzo
'''
#!/usr/bin/env python2
from src.gr_antenna import gr_antenna 
from numpy import double, char
from __builtin__ import str

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser

import Gnuplot, Gnuplot.funcutils
import threading
import osmosdr
import sip
import sys
import time
import threading
import os
from gps import *
import math
import curses

class myclass(gr_antenna):
    value = 0
    freq = 1000
    def __init__(self):
        #gr_antenna.__init__()
        super(myclass,self).__init__()
        self.variable_function_probe_0 = variable_function_probe_0 = 0
        self.blocks_probe_signal_x_0 = blocks.probe_signal_f()
        
        def _variable_function_probe_0_probe():
            while True:
                val = self.blocks_probe_signal_x_0.level()
                self.value = val
                try:
                    self.set_variable_function_probe_0(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (self.freq))
                
        _variable_function_probe_0_thread = threading.Thread(target=_variable_function_probe_0_probe)
        _variable_function_probe_0_thread.daemon = True
        _variable_function_probe_0_thread.start()
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_probe_signal_x_0, 0))
        
    def get_val(self):
        return self.value
        
    def set_val_freq(self, _freq):
        self.freq = _freq

class GpsPoller(threading.Thread):
    
    def __init__(self):
    	threading.Thread.__init__(self)
    	global gpsd #bring it in scope
    	gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    	#gpsd.stream(WATCH_NMEA) #starting the stream of info
        #thread.daemon = True
    	self.current_value = None
    	self.running = True #setting the thread running to true

    def run(self):
    	global gpsd
    	while gpsp.running:
    	    gpsd.next()

class position(GpsPoller):
    Xorigin = 0
    Yorigin = 0
    Zorigin = 0
    Xcord = 0
    Ycord = 0
    Zcord = 0
    XfromO = 0
    YfromO = 0
    ZfromO = 0
    theta = 0
    phi = 0
    alt = 0
    R = 6.3781*100000
    def data(self):
        while gpsp.running:
            self.theta = gpsd.fix.latitude
            self.phi = gpsd.fix.longitude
            self.alt = gpsd.fix.altitude

            self.Xcord = (self.R+self.alt)*math.sin(self.theta)*math.cos(self.phi)
            self.Ycord = (self.R+self.alt)*math.sin(self.theta)*math.sin(self.phi)
            self.Zcord = (self.R+self.alt)*math.cos(self.theta)

            self.XfromO = self.Xcord - self.Xorigin
            self.YfromO = self.Ycord - self.Yorigin
            self.ZfromO = self.Zcord - self.Zorigin
            time.sleep(0.1)
    def set_origin(self):
        self.Xorigin = self.Xcord
        self.Yorigin = self.Ycord
        self.Zorigin = self.Zcord

    def get_X(self):
        return self.XfromO

    def get_Y(self):
        return self.YfromO

    def get_Z(self):
        return self.YfromO

    def __init__(self): #starts the thread that collects data in the background 
        thread = threading.Thread(target=self.data, args = ())
        thread.daemon = True
        thread.start()
        thread.running = True
    
    def stop(self): #starts the thread that collects data in the background 
        print ""

class s_saver(myclass):

    def record(self,noOfSamples,my,pos):     #collects and plots signal strength data from the SDR-dongle
    	val = 0
        #----------PLOTTING SETTINGS---------------#
        g = Gnuplot.Gnuplot(debug = 0)
        g.title('My Systems Plot')
        g.xlabel('x')
        g.ylabel('Value(dB)')
        g('set term png')
        g('set out "output.png"')
        myFile = open("measurements.txt", "w")
        #------------------------------------------#
        
        #----------RECORDING LOOP--------------------#
        for x in range(0, noOfSamples):
            val = my.get_val() #collect the measurement data
            X = pos.get_X()
            Y = pos.get_Y()
            Z = pos.get_Z()
            myFile.write("{0} {1} {2} {3} {4}\n".format(x, val, X, Y, Z))    #write the data to file
            time.sleep(0.01)                            #sleeps for a while so that the SDR has time to change value.
        myFile.close()                                  #close and save the file
        #-----------------------------------------__#
        
        #------------PLOTTING------------------------#
        databuff = Gnuplot.File("measurements.txt", using='2:1',with_='line', title="Signal strength")
        g.plot(databuff)
        #--------------------------------------------#
        
        #print ("Recording is done") #optional output
    
  
    def recThread(self,noOfSamples,my,pos): #starts the thread that collects data in the background 
        thread = threading.Thread(target=self.record, args = (noOfSamples,my,pos,)) #creates threading object with function record()
        thread.daemon = True                                            #make sure that if we cancel main thread this thread cancels too
        thread.start()    

class parser():
    command_que = []
    total_string = ""
    short_string = ""
    command_history = []
    do_status = False

    def new_character(self,k):
        if k == 32: # space
           self.command_que.append(self.short_string)
           self.short_string = ""
           self.total_string = self.total_string + chr(k)

        elif k == 10: # newline
            self.do_status = True
            self.command_que.append(self.short_string)
            self.command_history.append(self.total_string)
            self.short_string = ""
            self.total_string = ""

        elif k == 263: # Backspace
            self.total_string = self.total_string[:-1]
            self.short_string = self.short_string[:-1]

        elif (k > 64 and k<91) or (k>96 and k<123): #letter
            self.total_string = self.total_string + chr(k)
            self.short_string = self.short_string + chr(k)

        elif (k>47 and k<58): #Numbers
            self.total_string = self.total_string + chr(k)
            self.short_string = self.short_string + chr(k)

    def get_full_string(self):
        #Return the total string
        return self.total_string

    def clear_string(self):
        self.total_string = ""
    
    def add_history(self,_str):
        self.command_history.extend(_str)

    def get_do_status(self):
        #return the do status
        return self.do_status

    def get_que(self):
        #return que
        return self.command_que

    def set_status_false(self):
        #return que
        self.do_status = False

    def get_history(self):
        return self.command_history

    def empty_que(self):
        self.command_que[:] = []
  

def application(stdscr,top_block_cls=myclass, options=None):

    def update_screen(stdscr,_cl,_pos,_myclass,_pars,_info_string):

        height, width = stdscr.getmaxyx()
        
        # Application main info screen 12 rows ------------------------------------------
        win =  "**********************************************\n"
        win += "***  Antenna characteriastion aplication   ***\n"
        win += "***  Running time:          "  +str(_cl)+"            ***\n"
        win += "***  current signal strengt: " + str(_myclass.get_val()) + " *** \n"
        win += "***  current ceter freq:     " + str(_myclass.get_c_freq()) + "      **\n"
        win += "***  current position X :     "+ str(_pos.get_X())  +" **\n"
        win += "***  current position Y :     "+ str(_pos.get_Y())  +" **\n"
        win += "***  current position Z :     "+ str(_pos.get_Z())  +" **\n"
        win += "***  avilable commands: freq, val, record, setvalfreq, quit, origin ***\n"
        win += "**********************************************\n"
        win += "\n"
        win += "----------------------------------------------------\n"
        stdscr.addstr(0,0,win)
        # -------------------------------------------------------------------------------

        # Command history and info screen
        avil_rows = height - 12 - 1
        
        command_history = _pars.get_history()
        list_length = len(command_history)
        str_length = len(_info_string)
        str_length = int(math.ceil(double(str_length)/width)) # Number of rows in infostring
        if str_length > 0:
            _pars.add_history(_info_string.split('\n'))
        if list_length > 0:
            i = 0
            if avil_rows > list_length:
                i = list_length-1
            else:
                i = avil_rows
            while i > -1:
                i = i-1
                tmp_str = command_history[list_length-2-i]
                str_length = len(tmp_str)
                str_length = int(math.ceil(double(str_length)/width))
                if str_length > 1:
                    i = i - str_length+1
                stdscr.addstr(height-2-str_length-i, 0,str(tmp_str))
        stdscr.addstr(height-1, 0,"# Write command$ "+_pars.get_full_string()) # Command input
    
    # Initialization of qt graphics
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)
    
    # Start threads and create objects
    tb = top_block_cls()
    tb.start()
    tb.show()
    rec = s_saver()
    pos = position()

    # Initialization of curses application
    stdscr.clear()
    stdscr.refresh()
    stdscr.nodelay(1)
    stdscr.keypad(1)
    k = "" #init k the input character
    info_string = ""
    instruction = "# Write command$ " #17 characters
    command_history = ["","","","",""]
    tid = 0
    running = True # Controll of main loop
    pars = parser()

    try:
        while (running): 
            time.sleep(0.1) 
            stdscr.clear()
            tid = tid+0.1 
            k = stdscr.getch()
            pars.new_character(k)

            if pars.get_do_status():
                command_que = pars.get_que()

                if command_que[0] == "time":
                    if len(command_que) > 1:
                        try: 
                            tid = int(command_que[1])
                        except ValueError:
                            tid = tid
                            info_string = 'undefined value: ' + str(command_que[1])
                    else:
                        tid = 0  
                    pars.set_status_false()
                    pars.empty_que() 
                elif command_que[0] == 'val':
                    print tb.get_val()
                    pars.set_status_false()
                    pars.empty_que()       
                #set the center frequency
                elif command_que[0] == 'freq':
                    in_val = raw_input('Set center freq: ')  
                    tb.set_c_freq(double(in_val)*double(1000000))
                    pars.set_status_false()
                    pars.empty_que()
                #get the frequency
                elif command_que[0] == 'get':
                    print tb.get_c_freq()
                    pars.set_status_false()
                    pars.empty_que()
                elif command_que[0] == 'origin':
                    pos.set_origin()
                    pars.set_status_false()
                    pars.empty_que()
                elif command_que[0] == 'setvalfreq':
                    in_val = raw_input('Value frequency: ')
                    tb.set_val_freq(int(in_val))
                    pars.set_status_false()
                    pars.empty_que()
		        #record some values and then plot them with gnuplot
                elif command_que[0] == 'record':
                    noOfSamples = input('No. of samples to record: ')
                    rec.recThread(noOfSamples,tb,pos)
                    pars.set_status_false()
                    pars.empty_que()
                #quit the program
                elif command_que[0] == "quit":
                    running = False
                    pars.set_status_false()
                    pars.empty_que()
                    stdscr.keypad(0)
                    tb.stop()
                    tb.wait()
                    pos.stop()
                    quit()
                else:
                    pars.set_status_false()
                    pars.empty_que()
            
            update_screen(stdscr,tid,pos,tb,pars,info_string)
            info_string = ""
            stdscr.refresh()

        

            #tb.update_screen(pos)
    except (KeyboardInterrupt,SystemExit): #when you press ctrl+c
        print "\nKilling Thread..."
        gpsp.running = False
        gpsp.join() # wait for the thread to finish what it's doing
        tb.stop()
        tb.wait()
        pos.stop()
        stdscr.keypad(0)
    print "Done.\nExiting."

def main():
    curses.wrapper(application)
           
if __name__ == '__main__':
    gpsp = GpsPoller()
    gpsp.start()
    main()
