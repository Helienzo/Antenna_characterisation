#
# Copyright 2008,2009 Free Software Foundation, Inc.
#
# This application is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This application is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

# The presence of this file turns this directory into a Python package

'''
This is the GNU Radio ANTCHAR module. Place your Python package
description here (python/__init__.py).
'''

# import swig generated symbols into the antchar namespace
try:
	# this might fail if the module is python-only
	from antchar_swig import *
except ImportError:
	pass

# import any pure python here
from dbm_correction_py_ff import dbm_correction_py_ff
from E_field_calc_ff import E_field_calc_ff
from Antenna_loop_ID_ff import Antenna_loop_ID_ff
from Antenna_switch_c import Antenna_switch_c
from antenna_polarization_adder_ff import antenna_polarization_adder_ff
from event_sink_f import event_sink_f
from Antenna import Antenna
from value_sink_ff import value_sink_ff
from vector_sink_f import vector_sink_f
#
