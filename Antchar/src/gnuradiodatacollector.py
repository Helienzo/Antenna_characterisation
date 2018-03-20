from src import *
from gr_antenna import gr_antenna
import antchar
class gnuradiodatacollector(gr_antenna):

    def __init__(self,data):
        super(gnuradiodatacollector,self).__init__()

        ##################################################
        # Blocks
        ##################################################
        self.antchar_value_sink_ff_0 = antchar.value_sink_ff(data,0)
        self.antchar_value_sink_ff_1 = antchar.value_sink_ff(data,1)
        self.antchar_value_sink_ff_2 = antchar.value_sink_ff(data,2)
        self.antchar_vector_sink_f_0 = antchar.vector_sink_f(data,self.fft_size,0)
        self.antchar_vector_sink_f_1 = antchar.vector_sink_f(data,self.fft_size,1)
        
        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_nlog10_ff_0, 0), (self.antchar_vector_sink_f_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.antchar_vector_sink_f_1, 0))
        self.connect((self.blocks_max_xx_0, 0), (self.antchar_value_sink_ff_0, 0))
        self.connect((self.antchar_dbm_correction_py_ff_0, 0), (self.antchar_value_sink_ff_1, 0))
        self.connect((self.antchar_E_field_calc_ff_0, 0), (self.antchar_value_sink_ff_2, 0))

    def reset(self):
        self.blocks_head_0_0_0.reset()

