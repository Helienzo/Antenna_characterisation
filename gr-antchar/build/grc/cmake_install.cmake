# Install script for directory: /home/adam/Dropbox/Skola/Examensarbete/Git/gr-antchar/grc

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gnuradio/grc/blocks" TYPE FILE FILES
    "/home/adam/Dropbox/Skola/Examensarbete/Git/gr-antchar/grc/antchar_dbm_correction_py_ff.xml"
    "/home/adam/Dropbox/Skola/Examensarbete/Git/gr-antchar/grc/antchar_E_field_calc_ff.xml"
    "/home/adam/Dropbox/Skola/Examensarbete/Git/gr-antchar/grc/antchar_Antenna_loop_ID_ff.xml"
    "/home/adam/Dropbox/Skola/Examensarbete/Git/gr-antchar/grc/antchar_Antenna_switch_c.xml"
    "/home/adam/Dropbox/Skola/Examensarbete/Git/gr-antchar/grc/antchar_antenna_polarization_adder_ff.xml"
    "/home/adam/Dropbox/Skola/Examensarbete/Git/gr-antchar/grc/antchar_event_sink_f.xml"
    "/home/adam/Dropbox/Skola/Examensarbete/Git/gr-antchar/grc/antchar_value_sink_ff.xml"
    "/home/adam/Dropbox/Skola/Examensarbete/Git/gr-antchar/grc/antchar_vector_sink_f.xml"
    )
endif()

