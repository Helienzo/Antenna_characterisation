#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Gr Antenna
# Generated: Wed Mar  7 09:17:11 2018
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
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import antchar
import osmosdr
import sip
import sys
import time
from gnuradio import qtgui


class gr_antenna(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Gr Antenna")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Gr Antenna")
        qtgui.util.check_set_qss()
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
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            fft_size,
            0,
            1,
            "x-Axis",
            "y-Axis",
            "",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(-200, 10)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_win)
        self.qtgui_number_sink_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_1.set_update_time(0.10)
        self.qtgui_number_sink_1.set_title("Polarisation adder dBmW/m²")

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_1.set_min(i, -150)
            self.qtgui_number_sink_1.set_max(i, 10)
            self.qtgui_number_sink_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_1.set_label(i, labels[i])
            self.qtgui_number_sink_1.set_unit(i, units[i])
            self.qtgui_number_sink_1.set_factor(i, factor[i])

        self.qtgui_number_sink_1.enable_autoscale(False)
        self._qtgui_number_sink_1_win = sip.wrapinstance(self.qtgui_number_sink_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_1_win)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            1,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("Corrected dBm")

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0.set_min(i, -150)
            self.qtgui_number_sink_0_0.set_max(i, 10)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_0_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            1,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("Measured dBm")

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -150)
            self.qtgui_number_sink_0.set_max(i, 10)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
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
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, fft_size, 0)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1.0/float(fft_size), ))
        self.blocks_max_xx_0 = blocks.max_ff(fft_size,1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(fft_size)
        self.antchar_dbm_correction_py_ff_0 = antchar.dbm_correction_py_ff((c_freq+0.5e6)/1.0e6)
        self.antchar_antenna_polarization_adder_ff_0 = antchar.antenna_polarization_adder_ff()
        self.antchar_E_field_calc_ff_0 = antchar.E_field_calc_ff((c_freq+0.5e6)/1.0e6)
        self.antchar_Antenna_switch_c_0 = antchar.Antenna_switch_c(FIR_decimation, fft_size,loop,auto_loop)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.antchar_E_field_calc_ff_0, 0), (self.antchar_antenna_polarization_adder_ff_0, 0))
        self.connect((self.antchar_antenna_polarization_adder_ff_0, 0), (self.qtgui_number_sink_1, 0))
        self.connect((self.antchar_dbm_correction_py_ff_0, 0), (self.antchar_E_field_calc_ff_0, 0))
        self.connect((self.antchar_dbm_correction_py_ff_0, 0), (self.qtgui_number_sink_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_max_xx_0, 0), (self.antchar_dbm_correction_py_ff_0, 0))
        self.connect((self.blocks_max_xx_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_max_xx_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.antchar_Antenna_switch_c_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "gr_antenna")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

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
        self.antchar_Antenna_switch_c_0.set_loop(self.loop)

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size
        self.blocks_multiply_const_vxx_0.set_k((1.0/float(self.fft_size), ))

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
        self.antchar_Antenna_switch_c_0.set_auto(self.auto_loop)

    def get_FIR_decimation(self):
        return self.FIR_decimation

    def set_FIR_decimation(self, FIR_decimation):
        self.FIR_decimation = FIR_decimation


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
