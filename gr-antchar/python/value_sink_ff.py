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

class value_sink_ff(gr.sync_block):
    """
    Stores incoming values in an external data class 
    """
    def __init__(self, data,var,event):
        self.data = data
        self.var = var
        self.event = event
        gr.sync_block.__init__(self,
            name="value_sink_ff",
            in_sig=[numpy.float32],
            out_sig=None)


    def work(self, input_items, output_items):
        in0 = input_items[0]
        self.event.set()
        self.data.setData(in0[0],self.var)
        # <+signal processing here+>
        return len(input_items[0])

