# Install script for directory: /home/odroid/prefix/default/src/gr-antchar/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/odroid/prefix/default")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/antchar" TYPE FILE FILES
    "/home/odroid/prefix/default/src/gr-antchar/python/__init__.py"
    "/home/odroid/prefix/default/src/gr-antchar/python/dbm_correction_py_ff.py"
    "/home/odroid/prefix/default/src/gr-antchar/python/AF_finder.py"
    "/home/odroid/prefix/default/src/gr-antchar/python/Antenna.py"
    "/home/odroid/prefix/default/src/gr-antchar/python/E_field_calc_ff.py"
    "/home/odroid/prefix/default/src/gr-antchar/python/Antenna_loop_ID_ff.py"
    "/home/odroid/prefix/default/src/gr-antchar/python/Antenna_switch_c.py"
    "/home/odroid/prefix/default/src/gr-antchar/python/antenna_polarization_adder_ff.py"
    "/home/odroid/prefix/default/src/gr-antchar/python/event_sink_f.py"
    "/home/odroid/prefix/default/src/gr-antchar/python/value_sink_ff.py"
    "/home/odroid/prefix/default/src/gr-antchar/python/vector_sink_f.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/antchar" TYPE FILE FILES
    "/home/odroid/prefix/default/src/gr-antchar/build/python/__init__.pyc"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/dbm_correction_py_ff.pyc"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/AF_finder.pyc"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/Antenna.pyc"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/E_field_calc_ff.pyc"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/Antenna_loop_ID_ff.pyc"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/Antenna_switch_c.pyc"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/antenna_polarization_adder_ff.pyc"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/event_sink_f.pyc"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/value_sink_ff.pyc"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/vector_sink_f.pyc"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/__init__.pyo"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/dbm_correction_py_ff.pyo"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/AF_finder.pyo"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/Antenna.pyo"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/E_field_calc_ff.pyo"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/Antenna_loop_ID_ff.pyo"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/Antenna_switch_c.pyo"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/antenna_polarization_adder_ff.pyo"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/event_sink_f.pyo"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/value_sink_ff.pyo"
    "/home/odroid/prefix/default/src/gr-antchar/build/python/vector_sink_f.pyo"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/antchar" TYPE FILE FILES "/home/odroid/prefix/default/src/gr-antchar/python/AF_data.txt")
endif()

