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
import math
import AF_finder as af
from gnuradio import gr

class E_field_calc_ff(gr.sync_block):
    """
    Calculate E-field from voltage
    """
    def __init__(self,res,freq):
        self.res = res
        self.freq = freq
        gr.sync_block.__init__(self,name="E_field_calc_ff",in_sig=[numpy.float32],out_sig=[numpy.float32])

    def set_freq(self,freq):
            self.freq = freq

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        afE,afH = af.finder(self.freq)
        
        micV = in0 + 107 #dBµV
        micVm = afE + micV #dBµV/m
        
        micA = in0 + 73 #dBµA
        micAm = afH + micA #dBµA/m
        
        E = 20*numpy.log10(numpy.sqrt(in0*float(self.res)/1000.0))+120+afE # dBuV/m
        H = 20*numpy.log10(numpy.sqrt(in0*float(self.res)/1000.0))+120+afH # dBuA/m
        P = E+H #dBuW/m²
        out[:] = P
        return len(output_items[0])

