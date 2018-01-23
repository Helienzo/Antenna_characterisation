#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Gr Antenna
# Generated: Tue Jan 23 14:49:54 2018
##################################################

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


class gr_antenna(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Gr Antenna")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Gr Antenna")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "gr_antenna")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.xlaiting_decimation = xlaiting_decimation = 20
        self.samp_rate = samp_rate = 2e6
        self.first_samprate = first_samprate = samp_rate/xlaiting_decimation
        self.fft_1_decimation = fft_1_decimation = 10
        self.second_samprate = second_samprate = first_samprate/fft_1_decimation
        self.fft_2_decimation = fft_2_decimation = 5
        self.third_samprate = third_samprate = second_samprate/fft_2_decimation
        self.firdes_taps_xlating = firdes_taps_xlating = firdes.low_pass_2(1, samp_rate, first_samprate*0.5, first_samprate/4, 70, firdes.WIN_HAMMING, 6.76)
        self.firdes_taps_fft_2 = firdes_taps_fft_2 = firdes.low_pass_2(1,second_samprate, third_samprate*0.5, third_samprate/4, 70, firdes.WIN_HAMMING, 6.76)
        self.firdes_taps_fft_1 = firdes_taps_fft_1 = firdes.low_pass_2(1, first_samprate, second_samprate*0.5, second_samprate/4, 70, firdes.WIN_HAMMING, 6.76)
        self.c_freq = c_freq = 96.6e6

        ##################################################
        # Blocks
        ##################################################
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(c_freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	c_freq, #fc
        	third_samprate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(xlaiting_decimation, (firdes_taps_xlating), 0, samp_rate)
        self.fft_filter_xxx_1 = filter.fft_filter_ccc(fft_1_decimation, (firdes_taps_fft_1), 1)
        self.fft_filter_xxx_1.declare_sample_delay(0)
        self.fft_filter_xxx_0 = filter.fft_filter_ccc(fft_2_decimation, (firdes_taps_fft_2), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((10e-3, ))
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_nlog10_ff_0, 0))    
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_null_sink_1, 0))    
        self.connect((self.fft_filter_xxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.fft_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.fft_filter_xxx_1, 0), (self.fft_filter_xxx_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.fft_filter_xxx_1, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "gr_antenna")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_xlaiting_decimation(self):
        return self.xlaiting_decimation

    def set_xlaiting_decimation(self, xlaiting_decimation):
        self.xlaiting_decimation = xlaiting_decimation
        self.set_first_samprate(self.samp_rate/self.xlaiting_decimation)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_firdes_taps_xlating(firdes.low_pass_2(1, self.samp_rate, self.first_samprate*0.5, self.first_samprate/4, 70, firdes.WIN_HAMMING, 6.76))
        self.set_first_samprate(self.samp_rate/self.xlaiting_decimation)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_first_samprate(self):
        return self.first_samprate

    def set_first_samprate(self, first_samprate):
        self.first_samprate = first_samprate
        self.set_firdes_taps_fft_1(firdes.low_pass_2(1, self.first_samprate, self.second_samprate*0.5, self.second_samprate/4, 70, firdes.WIN_HAMMING, 6.76))
        self.set_firdes_taps_xlating(firdes.low_pass_2(1, self.samp_rate, self.first_samprate*0.5, self.first_samprate/4, 70, firdes.WIN_HAMMING, 6.76))
        self.set_second_samprate(self.first_samprate/self.fft_1_decimation)

    def get_fft_1_decimation(self):
        return self.fft_1_decimation

    def set_fft_1_decimation(self, fft_1_decimation):
        self.fft_1_decimation = fft_1_decimation
        self.set_second_samprate(self.first_samprate/self.fft_1_decimation)

    def get_second_samprate(self):
        return self.second_samprate

    def set_second_samprate(self, second_samprate):
        self.second_samprate = second_samprate
        self.set_firdes_taps_fft_1(firdes.low_pass_2(1, self.first_samprate, self.second_samprate*0.5, self.second_samprate/4, 70, firdes.WIN_HAMMING, 6.76))
        self.set_firdes_taps_fft_2(firdes.low_pass_2(1,self.second_samprate, self.third_samprate*0.5, self.third_samprate/4, 70, firdes.WIN_HAMMING, 6.76))
        self.set_third_samprate(self.second_samprate/self.fft_2_decimation)

    def get_fft_2_decimation(self):
        return self.fft_2_decimation

    def set_fft_2_decimation(self, fft_2_decimation):
        self.fft_2_decimation = fft_2_decimation
        self.set_third_samprate(self.second_samprate/self.fft_2_decimation)

    def get_third_samprate(self):
        return self.third_samprate

    def set_third_samprate(self, third_samprate):
        self.third_samprate = third_samprate
        self.set_firdes_taps_fft_2(firdes.low_pass_2(1,self.second_samprate, self.third_samprate*0.5, self.third_samprate/4, 70, firdes.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(self.c_freq, self.third_samprate)

    def get_firdes_taps_xlating(self):
        return self.firdes_taps_xlating

    def set_firdes_taps_xlating(self, firdes_taps_xlating):
        self.firdes_taps_xlating = firdes_taps_xlating
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.firdes_taps_xlating))

    def get_firdes_taps_fft_2(self):
        return self.firdes_taps_fft_2

    def set_firdes_taps_fft_2(self, firdes_taps_fft_2):
        self.firdes_taps_fft_2 = firdes_taps_fft_2
        self.fft_filter_xxx_0.set_taps((self.firdes_taps_fft_2))

    def get_firdes_taps_fft_1(self):
        return self.firdes_taps_fft_1

    def set_firdes_taps_fft_1(self, firdes_taps_fft_1):
        self.firdes_taps_fft_1 = firdes_taps_fft_1
        self.fft_filter_xxx_1.set_taps((self.firdes_taps_fft_1))

    def get_c_freq(self):
        return self.c_freq

    def set_c_freq(self, c_freq):
        self.c_freq = c_freq
        self.qtgui_freq_sink_x_0.set_frequency_range(self.c_freq, self.third_samprate)
        self.rtlsdr_source_0.set_center_freq(self.c_freq, 0)


def main(top_block_cls=gr_antenna, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
