#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/odroid/prefix/default/src/gr-antchar/python
export PATH=/home/odroid/prefix/default/src/gr-antchar/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/odroid/prefix/default/src/gr-antchar/build/swig:$PYTHONPATH
/usr/bin/python2 /home/odroid/prefix/default/src/gr-antchar/python/qa_Antenna_loop_ID_ff.py 
