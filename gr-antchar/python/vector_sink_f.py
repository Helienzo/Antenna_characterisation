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

class vector_sink_f(gr.sync_block):
    """
    Stores a vector in an external data class
    """
    def __init__(self, data,v_len,var):
        self.data = data
        self.var = var
        if var == 1:
            v_len = v_len*2
        gr.sync_block.__init__(self,
            name="vector_sink_f",
            in_sig=[(numpy.float32,v_len)],
            out_sig=None)


    def work(self, input_items, output_items):
        in0 = input_items[0]
        self.data.setVector(in0[0],self.var)
        # <+signal processing here+>
        return len(input_items[0])

