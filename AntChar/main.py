#!/home/odroid/prefix/default/lib python2
'''
Created on Jan 19, 2018

@author: enzo
'''
from src import *
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
def end():
    raise SystemExit
   
def main(top_block_cls=radio, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)
    fig = plt.figure()
    ax1 = fig.gca(projection='3d')
    tb = top_block_cls(qapp,ax1)
    tb.start()
    tb.show()
    #plt.show()
    def quitting():
        tb.stop()
        tb.wait()

    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()

           
if __name__ == '__main__':
    gpsp.start()
    main()
