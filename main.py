'''
Created on Jan 19, 2018

@author: enzo
'''
#!/usr/bin/env python2
from src.gr_antenna import gr_antenna 
from numpy import double

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
import osmosdr
import sip
import sys
import time
import threading
import os



class myclass(gr_antenna):
    value = 0
    freq = 100
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
        print self.value    

def main(top_block_cls=myclass, options=None):
    
    
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)
    
    #fo = open("foo.txt", "wb")
    os.system('clear')
    inp = ''
    
    tb = top_block_cls()
    tb.start()
    tb.show()
    print 'To init the measurment write start'
    while inp != quit: 
        
        inp = raw_input('write command: ')
        if inp == 'val':
            tb.get_val()
        elif inp == 'start':     
            print ''
        elif inp == 'freq':
            in_val = raw_input('Set center freq: ')  
            tb.set_c_freq(double(in_val)*double(1000000))
        elif inp == 'get':
            print tb.get_c_freq()
        elif inp == 'quit':
            tb.stop()
            tb.wait()
            quit()

if __name__ == '__main__':
    main()