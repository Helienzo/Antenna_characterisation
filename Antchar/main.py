#!/home/odroid/prefix/default/lib python2
'''
Created on Jan 19, 2018

@author: enzo
'''
from src import *
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
   
def main():
    # Init all parts of application
    try:
        endEvent = threading.Event()
        fig = plt.figure() # Plot figure
        ax1 = fig.gca(projection='3d') # Plot data
        data = Data() # The data class that contains all data
        dspProcces = dsp(data,endEvent) # The signalproccesing block
        app = Application(dspProcces,data,ax1,endEvent) # Terminal application
        plotevent = app.getPlotEvent()
        
        while plotevent.isSet() == False and endEvent.isSet() == False:
            time.sleep(1)
        if plotevent.isSet():
            plt.show()
    except (KeyboardInterrupt,SystemExit):
        app.endprocess()
if __name__ == '__main__':
    gpsp.start() # Global gps object start
    main()
