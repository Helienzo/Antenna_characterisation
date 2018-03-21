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

class Antenna_switch_c(gr.sync_block):
    """
    docstring for block Antenna_switch_c
    """
    def __init__(self,dec,v_len,loop,auto):
        self.dec = dec
        self.v_len = v_len
        self.ant = Antenna(self.dec,self.v_len)
        self.loop = loop
        self.auto = auto
        gr.sync_block.__init__(self,
            name="Antenna_switch_c",
            in_sig=[numpy.complex64],
            out_sig=None)

    def set_auto(self,auto):
        self.auto = auto

    def set_loop(self,loop):
        self.loop = loop
        if self.auto == 0:
            if self.loop == 1:
                self.ant.loopOne()
            elif self.loop == 2:
                self.ant.loopTwo()
            elif self.loop == 3:
                self.ant.loopThree()
            else:
                self.ant.reset()

    def work(self, input_items, output_items):
        in0 = input_items[0]
        #print(len(in0))
        self.ant.currentLoop(len(input_items[0]),self.auto)
        if self.auto == 0:
            if self.loop == 1:
                self.ant.loopOne()
            elif self.loop == 2:
                self.ant.loopTwo()
            elif self.loop == 3:
                self.ant.loopThree()
            else:
                self.ant.reset()
        return len(input_items[0])

