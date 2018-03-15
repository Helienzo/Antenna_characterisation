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
        fig = plt.figure(1) # Plot figure
        ax1 = fig.gca() # Plot data
        #ax1 = fig.add_subplot(111)
        data = Data() # The data class that contains all data
        dspProcces = dsp(data,endEvent) # The signalproccesing block
        app = Application(dspProcces,data,ax1,fig,endEvent) # Terminal application
        plotevent = app.getPlotEvent()
        
        while endEvent.isSet() == False:
            time.sleep(1)
            if plotevent.isSet():
                plotevent.clear()
                plt.show()
                

    except (KeyboardInterrupt,SystemExit):
        app.endprocess()
if __name__ == '__main__':
    gpsp.start() # Global gps object start
    main()
