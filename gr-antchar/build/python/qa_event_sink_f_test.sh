#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/adam/Dropbox/Skola/Examensarbete/Git/gr-antchar/python
export PATH=/home/adam/Dropbox/Skola/Examensarbete/Git/gr-antchar/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/adam/Dropbox/Skola/Examensarbete/Git/gr-antchar/build/swig:$PYTHONPATH
/usr/bin/python2 /home/adam/Dropbox/Skola/Examensarbete/Git/gr-antchar/python/qa_event_sink_f.py 
