from src import *
import numpy as np
import math
import csv
class s_saver():

    def __init__(self,value_event,value,rec_event):
        self.value_event = value_event  # threading event from gnuradio, is set when new value is aviable
        self.rec_event = rec_event # recording event
        self.value = value  #List that contains the gnuradio calculated value

    def record_samples(self,noOfSamples,filename,my,pos):     #collects and plots signal strength data from the SDR-dongle
        val = 0
        self.rec_event.set()
        myFile = open(str(filename), "w")
        #------------------------------------------#
        
        #----------RECORDING LOOP--------------------#
        for x in range(0, noOfSamples):
            self.value_event.wait() # Wait untill new value is available
            val = self.value[0] #collect the measurement data
            T = time.time()
            X = pos.get_X()
            Y = pos.get_Y()
            Z = pos.get_Z()
            myFile.write("{0} {1} {2} {3} {4} {5} \n".format(x+1, T, val, X, Y, Z))    #write the data to file
            self.value_event.clear() # Resets the flag.
        myFile.close()                                  #close and save the file
        self.rec_event.clear()
        #-----------------------------------------__#

    def record_time(self,noOfTime,filename,my,pos):     #collects and plots signal strength data from the SDR-dongle
        self.rec_event.set()
        E_time = 0  # Elapsed time
        C_time = 0 # Current time
        S_time = time.time() # Start time   	
        noOfTime = noOfTime*60 # From minutes to seconds        
        val = 0
        x = 0
        myFile = open(str(filename), "w")
        #------------------------------------------#
        
        #----------RECORDING LOOP--------------------#
        while E_time < noOfTime:
            self.value_event.wait() # Wait untill new value is available
            x += 1 # Amount of samples
            val = self.value[0] #collect the measurement data
            T = time.time()
            X = pos.get_X()
            Y = pos.get_Y()
            Z = pos.get_Z()
            myFile.write("{0} {1} {2} {3} {4} {5} \n".format(x, T, val, X, Y, Z))    #write the data to file
            C_time = time.time() # Get current time
            E_time = C_time - S_time # Calculate elapsed time
            #print E_time
            self.value_event.clear() # Resets the flag.

        myFile.close()                                  #close and save the file
        self.rec_event.clear()

    def plotter(self,filename,ax1):
        x = []
        y = []
        z = []
        myfile = open(str(filename), "r")
        for line in myfile:
            coord = line.split(" ")
            x.append(float(coord[3]))
            y.append(float(coord[4]))
            z.append(float(coord[5]))
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

    def recThread_time(self,filename,noOfTime,my,pos): #starts the thread that collects data in the background
        #records in minutes 
        thread = threading.Thread(target=self.record_time, args = (noOfTime,filename,my,pos,)) #creates threading object with function record()
        thread.daemon = True                                            #make sure that if we cancel main thread this thread cancels too
        thread.start()  

