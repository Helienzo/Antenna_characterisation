from src import *
import numpy as np
import math
import csv
class s_saver():

    def record_samples(self,noOfSamples,filename,my,pos):     #collects and plots signal strength data from the SDR-dongle
    	val = 0
        myFile = open(str(filename), "w")
        #------------------------------------------#
        
        #----------RECORDING LOOP--------------------#
        for x in range(0, noOfSamples):
            val = my.get_val() #collect the measurement data
            X = pos.get_X()
            Y = pos.get_Y()
            Z = pos.get_Z()
            myFile.write("{0} {1} {2} {3} {4} \n".format(x, val, X, Y, Z))    #write the data to file
            time.sleep(0.1)                            #sleeps for a while so that the SDR has time to change value.
        myFile.close()                                  #close and save the file
        #-----------------------------------------__#

    def record_time(self,noOfTime,filename,my,pos):     #collects and plots signal strength data from the SDR-dongle
    	val = 0
        paus_time = 0.1
        myFile = open(str(filename), "w")
        #------------------------------------------#
        
        #----------RECORDING LOOP--------------------#
        for x in range(0,int(noOfTime*60.0/paus_time)):
            val = my.get_val() #collect the measurement data
            X = pos.get_X()
            Y = pos.get_Y()
            Z = pos.get_Z()
            myFile.write("{0} {1} {2} {3} {4} \n".format(x, val, X, Y, Z))    #write the data to file
            time.sleep(paus_time)   #sleeps for a while so that the SDR has time to change value.
        myFile.close()                                  #close and save the file

    def plotter(self,filename,ax1):
        x = []
        y = []
        z = []
        myfile = open(str(filename), "r")
        for line in myfile:
            coord = line.split(" ")
            x.append(float(coord[2]))
            y.append(float(coord[3]))
            z.append(float(coord[4]))
        plot = ax1.plot(x,y,z,label = 'parametric curve')
        #plot = ax1.plot([0,100],[0,100],[0,100],label = 'parametric curve')

    def plotting(self,filename,ax1): #starts the thread that collects data in the background
        thread = threading.Thread(target=self.plotter, args = (filename,ax1,)) #creates threading object with function record()
        thread.daemon = True                                            #make sure that if we cancel main thread this thread cancels too
        thread.start()
 
    def recThread_samples(self,filename,noOfSamples,my,pos): #starts the thread that collects data in the background 
        thread = threading.Thread(target=self.record_samples, args = (noOfSamples,filename,my,pos,)) #creates threading object with function record()
        thread.daemon = True                                            #make sure that if we cancel main thread this thread cancels too
        thread.start()

    def recThread_time(self,filename,noOfSamples,my,pos): #starts the thread that collects data in the background
        #records in minutes 
        thread = threading.Thread(target=self.record_time, args = (noOfSamples,filename,my,pos,)) #creates threading object with function record()
        thread.daemon = True                                            #make sure that if we cancel main thread this thread cancels too
        thread.start()  

