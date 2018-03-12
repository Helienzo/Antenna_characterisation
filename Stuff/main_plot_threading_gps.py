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

    def update_screen(self,pos):
        os.system('clear')
        val_str = str(self.get_val())
        print("\t**********************************************")
        print("\t***  Antenna characteriastion aplication   ***")
        print("\t*** current signal strengt: " + val_str + " *** ")
        print("\t*** current ceter freq:     " + str(self.get_c_freq()) + "      **")
        print("\t*** current position X :     "+ str(pos.get_X())  +" **")
        print("\t*** current position Y :     "+ str(pos.get_Y())  +" **")
        print("\t*** current position Z :     "+ str(pos.get_Z())  +" **")
        print("\t*** avilable commands: freq, val, record, setvalfreq, quit, origin ***")
        print("\t**********************************************")

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



def main(top_block_cls=myclass, options=None):
    
    
    
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)
    
    os.system('clear')
    inp = ''
    tb = top_block_cls()
    tb.start()
    tb.show()
    rec = s_saver()
    pos = position()
    try:
        while inp != quit: 
            time.sleep(0.01)
            tb.update_screen(pos)
            inp = raw_input('write command: ')
            
            #print the signal strength, hard to see now with the update of the screen
            if inp == 'val':
                print tb.get_val()
                
		    #has no effect currently
            elif inp == 'start':
                print ''
                
            #set the center frequency
            elif inp == 'freq':
                in_val = raw_input('Set center freq: ')  
                tb.set_c_freq(double(in_val)*double(1000000))
                
            #get the frequency
            elif inp == 'get':
                print tb.get_c_freq()
                
            #quit the program
            elif inp == 'quit':
                tb.stop()
                tb.wait()
                pos.stop()
                quit()
            elif inp == 'origin':
                pos.set_origin()
            
            elif inp == 'setvalfreq':
                in_val = raw_input('Value frequency: ')
                tb.set_val_freq(int(in_val))

		    #record some values and then plot them with gnuplot
            elif inp == 'record':
                noOfSamples = input('No. of samples to record: ')
                rec.recThread(noOfSamples,tb,pos)
    except (KeyboardInterrupt,SystemExit ): #when you press ctrl+c
        print "\nKilling Thread..."
        gpsp.running = False
        gpsp.join() # wait for the thread to finish what it's doing
        tb.stop()
        tb.wait()
        pos.stop()
    print "Done.\nExiting."
            
if __name__ == '__main__':
    gpsp = GpsPoller()
    gpsp.start()
    main()
