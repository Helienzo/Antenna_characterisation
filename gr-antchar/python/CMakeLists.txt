# Copyright 2011 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Include python install macros
########################################################################
include(GrPython)
if(NOT PYTHONINTERP_FOUND)
    return()
endif()

########################################################################
# Install python sources
########################################################################
GR_PYTHON_INSTALL(
    FILES
    __init__.py
    dbm_correction_py_ff.py
    AF_finder.py
    Antenna.py
    E_field_calc_ff.py
    Antenna_loop_ID_ff.py
    Antenna_switch_c.py
    antenna_polarization_adder_ff.py
    event_sink_f.py
    value_sink_ff.py
    vector_sink_f.py DESTINATION ${GR_PYTHON_DIR}/antchar
)

install(FILES AF_data.txt DESTINATION ${GR_PYTHON_DIR}/antchar)
########################################################################
# Handle the unit tests
########################################################################
include(GrTest)

set(GR_TEST_TARGET_DEPS gnuradio-antchar)
set(GR_TEST_PYTHON_DIRS ${CMAKE_BINARY_DIR}/swig)
GR_ADD_TEST(qa_dbm_correction_py_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_dbm_correction_py_ff.py)
GR_ADD_TEST(qa_E_field_calc_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_E_field_calc_ff.py)
GR_ADD_TEST(qa_Antenna_loop_ID_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_Antenna_loop_ID_ff.py)
GR_ADD_TEST(qa_Antenna_switch_c ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_Antenna_switch_c.py)
GR_ADD_TEST(qa_antenna_polarization_adder_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_antenna_polarization_adder_ff.py)
GR_ADD_TEST(qa_event_sink_f ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_event_sink_f.py)
GR_ADD_TEST(qa_value_sink_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_value_sink_ff.py)
GR_ADD_TEST(qa_vector_sink_f ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_vector_sink_f.py)
