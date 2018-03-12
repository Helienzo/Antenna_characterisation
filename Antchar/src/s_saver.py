from src import *
import numpy as np
import math
import csv
class s_saver():

    def __init__(self,value_event,data,rec_event):
        self.value_event = value_event  # threading event from gnuradio, is set when new value is aviable
        self.rec_event = rec_event # recording event
        self.data = data

    def record_samples(self,noOfSamples,filename,pos):     #collects and plots signal strength data from the SDR-dongle
        self.rec_event.set()
        E_time = 0  # Elapsed time
        C_time = 0 # Current time
        S_time = time.time() # Start time
        val = 0
        name = filename.split('.')
        myFile = open(str(name[0]+".txt"), "w")
        myFilevec = open(str(name[0]+"_vector.txt"), "w")
        #------------------------------------------#
        
        #----------RECORDING LOOP--------------------#
        myFile.write("Nr Etime Raw dBm dBmW/m2 sum:dBmW/m2 loop X Y Z \n")
        for x in range(0, noOfSamples):
            self.value_event.wait() # Wait untill new value is available
            rawVal = self.data.getData(0) #collect the measurement data
            corrVal = self.data.getData(1) #collect the measurement data
            powVal = self.data.getData(2) #collect the measurement data
            loopVal = self.data.getData(3) #collect the measurement data
            totVal = self.data.getData(4) #collect the measurement data
            vec = self.data.getVector()
            X = pos.get_X()
            Y = pos.get_Y()
            Z = pos.get_Z()
            myFile.write("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} \n".format(x+1, E_time,rawVal,corrVal,powVal,totVal,loopVal, X, Y, Z))    #write the data to file
            for i in range(0,len(vec)):
                myFilevec.write("{0} ".format(vec[i]))   #write the data to file
            myFilevec.write("\n")
            C_time = time.time() # Get current time
            E_time = C_time - S_time # Calculate elapsed time
            self.value_event.clear() # Resets the flag.
        myFile.close()  #close and save the file
        myFilevec.close()  #close and save the file
        self.rec_event.clear()
        #-----------------------------------------__#

    def record_time(self,noOfTime,filename,pos):     #collects and plots signal strength data from the SDR-dongle
        self.rec_event.set()
        E_time = 0  # Elapsed time
        C_time = 0 # Current time
        S_time = time.time() # Start time   	
        noOfTime = noOfTime*60 # From minutes to seconds        
        val = 0
        x = 0
        name = filename.split('.')
        myFile = open(str(name[0]+".txt"), "w")
        myFilevec = open(str(name[0]+"_vector.txt"), "w")
        #------------------------------------------#
        
        #----------RECORDING LOOP--------------------#
        myFile.write("Nr Etime Raw dBm dBmW/m2 sum:dBmW/m2 loop X Y Z \n")
        while E_time < noOfTime:
            self.value_event.wait() # Wait untill new value is available
            x += 1 # Amount of samples
            rawVal = self.data.getData(0) #collect the measurement data
            corrVal = self.data.getData(1) #collect the measurement data
            powVal = self.data.getData(2) #collect the measurement data
            loopVal = self.data.getData(3) #collect the measurement data
            totVal = self.data.getData(4) #collect the measurement data
            vec = self.data.getVector()
            X = pos.get_X()
            Y = pos.get_Y()
            Z = pos.get_Z()
            myFile.write("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} \n".format(x, E_time,rawVal,corrVal,powVal,totVal,loopVal, X, Y, Z))    #write the data to file
            for i in range(0,len(vec)):
                myFilevec.write("{0} ".format(vec[i]))   #write the data to file
            myFilevec.write("\n")
            C_time = time.time() # Get current time
            E_time = C_time - S_time # Calculate elapsed time
            #print E_time
            self.value_event.clear() # Resets the flag.

        myFile.close()                                  #close and save the file
        myFilevec.close()  #close and save the file
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
 
    def recThread_samples(self,filename,noOfSamples,pos): #starts the thread that collects data in the background 
        thread = threading.Thread(target=self.record_samples, args = (noOfSamples,filename,pos,)) #creates threading object with function record()
        thread.daemon = True                                            #make sure that if we cancel main thread this thread cancels too
        thread.start()

    def recThread_time(self,filename,noOfTime,pos): #starts the thread that collects data in the background
        #records in minutes 
        thread = threading.Thread(target=self.record_time, args = (noOfTime,filename,pos,)) #creates threading object with function record()
        thread.daemon = True                                            #make sure that if we cancel main thread this thread cancels too
        thread.start()  
