#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class dbm_correction_py_ff(gr.sync_block):
    """
    Frequency dependent dbm correction block frequency in MHz
    """
    def __init__(self,freq):

        self.freq = freq
        self.p1 = [1.0524391e-05, -0.0021925117, 0.16505503, -5.3744775, 71.307462]
        self.p2 = [-2.8766667, 220.53]
        self.p3 = [2.2556752e-10, -1.0486753e-07, 1.3099734e-05, -5.5318219e-06, -0.064232164, 4.2569307]
        self.p4 = [-1.8666667, 468.90556]
        self.p5 = [0.001735155, -0.86826021, 107.62026]
        self.p6 = [-0.95, 265.79333]
        self.p7 = [0.001134465, -0.63980835, 88.963656]
        gr.sync_block.__init__(self,name="dbm_correction_py_ff",in_sig=[numpy.float32],out_sig=[numpy.float32])
    def set_freq(self,freq):
            self.freq = freq

    def work(self, input_items, output_items):
        
        in0 = input_items[0]
        out = output_items[0]
        #print("dBm: ",in0)
        if self.freq >=30 and self.freq < 75:
            res = self.p1[0]*self.freq**4 + self.p1[1]*self.freq**3 + self.p1[2]*self.freq**2 +self.p1[3]*self.freq + self.p1[4];

        elif self.freq >=75 and self.freq < 76:
            res = self.p2[0]*self.freq + self.p2[1]

        elif self.freq >=76 and self.freq < 250:
            res = self.p3[0]*self.freq**5 + self.p3[1]*self.freq**4 + self.p3[2]*self.freq**3 +self.p3[3]*self.freq**2 + self.p3[4]*self.freq + self.p3[5];

        elif self.freq >=250 and self.freq < 251.8:
            res = self.p4[0]*self.freq + self.p4[1]

        elif self.freq >=251.8 and self.freq < 279.3:
            res = self.p5[0]*self.freq**2 + self.p5[1]*self.freq + self.p5[2]

        elif self.freq >=279.3 and self.freq < 281:
            res = self.p6[0]*self.freq + self.p6[1]

        elif self.freq >=281 and self.freq <= 300:
            res = self.p7[0]*self.freq**2 + self.p7[1]*self.freq + self.p7[2]
        else:
            res = 0

        out[:] = res + in0

        return len(output_items[0])
