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

class antenna_polarization_adder_ff(gr.sync_block):
    """
    docstring for block antenna_polarization_adder_ff
    """
    def __init__(self):
        self.axis = [0,0,0]
        gr.sync_block.__init__(self,
            name="antenna_polarization_adder_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
    def third_root(self,vec):
        tmp = numpy.sqrt( vec[0]**2 +vec[1]**2 +vec[2]**2 )
        return tmp

    def work(self, input_items, output_items):
        
        in0 = input_items[0]
        out = output_items[0]
        tmp = 0
        #print("P: ",in0)
        #print(" ")
        if len(in0) == 1:
            self.axis[0:1] = self.axis[1:2]
            self.axis[2] = in0
            tmp = (-1)*self.third_root(self.axis)
        else:
            print "WTF - Lets go home.."
        out[:] = tmp
        return len(output_items[0])

