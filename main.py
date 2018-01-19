'''
Created on Jan 19, 2018

@author: enzo
'''
from gr_antenna import gr_antenna 

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import threading
import time


class myclass(gr_antenna):
    value = 0
    def __init__(self):
        #gr_antenna.__init__()
        super(myclass,self).__init__()
        self.variable_function_probe_0 = variable_function_probe_0 = 0
        self.blocks_probe_signal_x_0 = blocks.probe_signal_c()
        def _variable_function_probe_0_probe():
            while True:
                val = self.blocks_probe_signal_x_0.level()
                self.value = val
                try:
                    self.set_variable_function_probe_0(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _variable_function_probe_0_thread = threading.Thread(target=_variable_function_probe_0_probe)
        _variable_function_probe_0_thread.daemon = True
        _variable_function_probe_0_thread.start()
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_probe_signal_x_0, 0))
    
    def get_val(self):
        print self.value    

def main(top_block_cls=myclass, options=None):

    tb = top_block_cls()
    tb.start()
    inp = ''
    
    while inp != quit: 
        
        inp = raw_input('write command: ')
        if inp == 'val':
            tb.get_val()
        elif inp == 'quit':
            tb.stop()
            tb.wait()
            quit()

if __name__ == '__main__':
    main()