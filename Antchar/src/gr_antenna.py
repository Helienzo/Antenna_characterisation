#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Gr Antenna
# Generated: Mon Mar 12 13:16:35 2018
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import antchar
import osmosdr
import time


class gr_antenna(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Gr Antenna")

        ##################################################
        # Variables
        ##################################################
        self.transition = transition = 10e3
        self.samp_rate = samp_rate = 2.5e6
        self.cutoff = cutoff = 9.1e3
        self.lowpasstaps = lowpasstaps = firdes.low_pass_2(1, samp_rate, cutoff,transition, 120,firdes.WIN_BLACKMAN, 6.76)
        self.c_freq = c_freq = 96.1e6
        self.number_of_taps_FIR = number_of_taps_FIR = len(lowpasstaps)
        self.loop = loop = 1
        self.fft_size = fft_size = 8192
        self.channel_in_mhz = channel_in_mhz = (c_freq+0.5e6)/1.0e6
        self.channel_freq = channel_freq = c_freq+0.5e6
        self.auto_loop = auto_loop = 1
        self.FIR_decimation = FIR_decimation = 32

        ##################################################
        # Blocks
        ##################################################
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'airspy' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(c_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(2, 0)
        self.osmosdr_source_0.set_iq_balance_mode(1, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(0, 0)
        self.osmosdr_source_0.set_if_gain(0, 0)
        self.osmosdr_source_0.set_bb_gain(0, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccf(FIR_decimation, (lowpasstaps), 0.5e6, samp_rate)
        self.fft_vxx_0 = fft.fft_vcc(fft_size, True, (window.blackmanharris(fft_size)), True, 1)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, fft_size, 0)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1.0/float(fft_size), ))
        self.blocks_max_xx_0 = blocks.max_ff(fft_size,1)
        self.blocks_head_0_0_0 = blocks.head(gr.sizeof_gr_complex*1, FIR_decimation*fft_size)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(fft_size)
        self.antchar_dbm_correction_py_ff_0 = antchar.dbm_correction_py_ff((c_freq+0.5e6)/1.0e6)
        self.antchar_antenna_polarization_adder_ff_0 = antchar.antenna_polarization_adder_ff()
        self.antchar_E_field_calc_ff_0 = antchar.E_field_calc_ff((c_freq+0.5e6)/1.0e6)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.antchar_E_field_calc_ff_0, 0), (self.antchar_antenna_polarization_adder_ff_0, 0))
        self.connect((self.antchar_antenna_polarization_adder_ff_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.antchar_dbm_correction_py_ff_0, 0), (self.antchar_E_field_calc_ff_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_head_0_0_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.blocks_max_xx_0, 0), (self.antchar_dbm_correction_py_ff_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_max_xx_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_head_0_0_0, 0))

    def get_transition(self):
        return self.transition

    def set_transition(self, transition):
        self.transition = transition
        self.set_lowpasstaps(firdes.low_pass_2(1, self.samp_rate, self.cutoff,self.transition, 120,firdes.WIN_BLACKMAN, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_lowpasstaps(firdes.low_pass_2(1, self.samp_rate, self.cutoff,self.transition, 120,firdes.WIN_BLACKMAN, 6.76))
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff
        self.set_lowpasstaps(firdes.low_pass_2(1, self.samp_rate, self.cutoff,self.transition, 120,firdes.WIN_BLACKMAN, 6.76))

    def get_lowpasstaps(self):
        return self.lowpasstaps

    def set_lowpasstaps(self, lowpasstaps):
        self.lowpasstaps = lowpasstaps
        self.set_number_of_taps_FIR(len(self.lowpasstaps))
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.lowpasstaps))

    def get_c_freq(self):
        return self.c_freq

    def set_c_freq(self, c_freq):
        self.c_freq = c_freq
        self.osmosdr_source_0.set_center_freq(self.c_freq, 0)
        self.set_channel_in_mhz((self.c_freq+0.5e6)/1.0e6)
        self.set_channel_freq(self.c_freq+0.5e6)
        self.antchar_dbm_correction_py_ff_0.set_freq((self.c_freq+0.5e6)/1.0e6)
        self.antchar_E_field_calc_ff_0.set_freq((self.c_freq+0.5e6)/1.0e6)

    def get_number_of_taps_FIR(self):
        return self.number_of_taps_FIR

    def set_number_of_taps_FIR(self, number_of_taps_FIR):
        self.number_of_taps_FIR = number_of_taps_FIR

    def get_loop(self):
        return self.loop

    def set_loop(self, loop):
        self.loop = loop

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size
        self.blocks_multiply_const_vxx_0.set_k((1.0/float(self.fft_size), ))
        self.blocks_head_0_0_0.set_length(self.FIR_decimation*self.fft_size)

    def get_channel_in_mhz(self):
        return self.channel_in_mhz

    def set_channel_in_mhz(self, channel_in_mhz):
        self.channel_in_mhz = channel_in_mhz

    def get_channel_freq(self):
        return self.channel_freq

    def set_channel_freq(self, channel_freq):
        self.channel_freq = channel_freq

    def get_auto_loop(self):
        return self.auto_loop

    def set_auto_loop(self, auto_loop):
        self.auto_loop = auto_loop

    def get_FIR_decimation(self):
        return self.FIR_decimation

    def set_FIR_decimation(self, FIR_decimation):
        self.FIR_decimation = FIR_decimation
        self.blocks_head_0_0_0.set_length(self.FIR_decimation*self.fft_size)


def main(top_block_cls=gr_antenna, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
