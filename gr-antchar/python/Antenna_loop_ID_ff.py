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
from Antenna import Antenna

class Antenna_loop_ID_ff(gr.sync_block):
    """
    docstring for block Antenna_loop_ID
    """
    def __init__(self,dec,v_len):
        self.dec = dec
        self.v_len = v_len
        self.ant = Antenna(self.dec,self.v_len)
        gr.sync_block.__init__(self,
            name="Antenna_loop_ID_ff",
            in_sig=[numpy.complex64],
            out_sig=[numpy.float32])


    def work(self, input_items, output_items):
        loop = output_items[0] #loop output
        # <+signal processing here+>
        
        loop[:] = self.ant.currentLoop() #Functionality of switching loop
                                    #is built into Antenna.py
                                    
        return len(output_items[:])

