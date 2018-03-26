from src import *
import numpy as np
import math
import csv
class s_saver():

    def __init__(self,value_event,data,rec_event):
        self.value_event = value_event  # threading event from gnuradio, is set when new value is aviable
        self.rec_event = rec_event # recording event
        self.data = data
        self.vecsave_event = threading.Event()
        self.start_event = threading.Event()
        self.stop_event = threading.Event()
        self.pause_event = threading.Event()
        self.step_event = threading.Event()

    def record_samples(self,noOfSamples,filename,pos):     #collects and plots signal strength data from the SDR-dongle
        self.rec_event.set()
        E_time = 0  # Elapsed time
        C_time = 0 # Current time
        S_time = time.time() # Start time
        val = 0
        ind = 0
        name = filename.split('.')
        myFile = open(str(name[0]+".txt"), "w")
        if self.vecsave_event.isSet():
            myFilevec = open(str(name[0]+"_vector.txt"), "w")
            myFilevecRAW = open(str(name[0]+"_RAWvector.txt"), "w")
        #------------------------------------------#
        
        #----------RECORDING LOOP--------------------#
        myFile.write("Nr Etime Raw dBm dBmW/m2 sum:dBmW/m2 loop X Y Z \n")
        while ind < noOfSamples and self.stop_event.isSet() != True:
            self.start_event.clear()
            ind += 1
            self.value_event.wait() # Wait untill new value is available
            rawVal = self.data.getData(0) #collect the measurement data
            corrVal = self.data.getData(1) #collect the measurement data
            powVal = self.data.getData(2) #collect the measurement data
            loopVal = self.data.getData(3) #collect the measurement data
            totVal = self.data.getData(4) #collect the measurement data
            X = pos.get_X()
            Y = pos.get_Y()
            Z = pos.get_Z()
            lon = pos.get_long()
            lat = pos.get_lat()
            C_time = time.time() # Get current time
            E_time = C_time - S_time # Calculate elapsed 
            myFile.write("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} \n".format(ind, E_time,rawVal,corrVal,powVal,totVal,loopVal, X, Y, Z, lon, lat))    #write the data to file
            if self.vecsave_event.isSet():
                vec = self.data.getVector(0)
                vecRAW = self.data.getVector(1)
                for i in range(0,len(vec)):
                    myFilevec.write("{0} ".format(vec[i]))   #write the data to file
                myFilevec.write("\n")
                for i in range(0,len(vecRAW)):
                    myFilevecRAW.write("{0} ".format(vecRAW[i]))   #write the data to file
                myFilevecRAW.write("\n")

            if self.pause_event.isSet():
                self.pause_event.clear()
                self.start_event.wait()
                
                P_time = time.time()-C_time
                S_time += P_time
            self.value_event.clear() # Resets the flag.

        myFile.close()  #close and save the file
        if self.vecsave_event.isSet():
            myFilevec.close()  #close and save the file
            myFilevecRAW.close()  #close and save the file
        self.rec_event.clear()
        self.stop_event.clear()
        self.start_event.clear()
        self.pause_event.clear()
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
        if self.vecsave_event.isSet():
            myFilevec = open(str(name[0]+"_vector.txt"), "w")
            myFilevecRAW = open(str(name[0]+"_RAWvector.txt"), "w")
        #------------------------------------------#
        
        #----------RECORDING LOOP--------------------#
        myFile.write("Nr Etime Raw dBm dBmW/m2 sum:dBmW/m2 loop X Y Z \n")
        while E_time < noOfTime and self.stop_event.isSet() != True:
            self.start_event.clear()
            self.value_event.wait() # Wait untill new value is available
            x += 1 # Amount of samples
            rawVal = self.data.getData(0) #collect the measurement data
            corrVal = self.data.getData(1) #collect the measurement data
            powVal = self.data.getData(2) #collect the measurement data
            loopVal = self.data.getData(3) #collect the measurement data
            totVal = self.data.getData(4) #collect the measurement data
            X = pos.get_X()
            Y = pos.get_Y()
            Z = pos.get_Z()
            lon = pos.get_long()
            lat = pos.get_lat()
            C_time = time.time() # Get current time
            E_time = C_time - S_time # Calculate elapsed 
            myFile.write("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} \n".format(x, E_time,rawVal,corrVal,powVal,totVal,loopVal, X, Y, Z, lon, lat))    #write the data to file
            if self.vecsave_event.isSet():
                vec = self.data.getVector(0)
                vecRAW = self.data.getVector(1)
                for i in range(0,len(vec)):
                    myFilevec.write("{0} ".format(vec[i]))   #write the data to file
                myFilevec.write("\n")
                for i in range(0,len(vecRAW)):
                    myFilevecRAW.write("{0} ".format(vecRAW[i]))   #write the data to file
                myFilevecRAW.write("\n")
            #print E_time
            self.value_event.clear() # Resets the flag.
            
            if self.pause_event.isSet():
                self.pause_event.clear()
                self.start_event.wait()

                P_time = time.time()-C_time
                S_time += P_time

        myFile.close()                                  #close and save the file
        if self.vecsave_event.isSet():
            myFilevec.close()  #close and save the file
            myFilevecRAW.close()  #close and save the file
        self.rec_event.clear()
        self.stop_event.clear()
        self.start_event.clear()
        self.pause_event.clear()

    def record(self,filename,pos):     #collects and plots signal strength data from the SDR-dongle
        self.rec_event.set()
        self.pause_event.set()
        E_time = 0  # Elapsed time
        C_time = 0 # Current time
        S_time = time.time() # Start time   	
        count = 0    
        val = 0
        x = 0
        name = filename.split('.')
        myFile = open(str(name[0]+".txt"), "w")
        if self.vecsave_event.isSet():
            myFilevec = open(str(name[0]+"_vector.txt"), "w")
            myFilevecRAW = open(str(name[0]+"_RAWvector.txt"), "w")
        #------------------------------------------#
        
        #----------RECORDING LOOP--------------------#
        myFile.write("Nr Etime Raw dBm dBmW/m2 sum:dBmW/m2 loop X Y Z \n")
        while self.stop_event.isSet() != True:
            if self.step_event.isSet():
                self.value_event.wait() # Wait untill new value is available
                x += 1 # Amount of samples
                rawVal = self.data.getData(0) #collect the measurement data
                corrVal = self.data.getData(1) #collect the measurement data
                powVal = self.data.getData(2) #collect the measurement data
                loopVal = self.data.getData(3) #collect the measurement data
                totVal = self.data.getData(4) #collect the measurement data
                X = pos.get_X()
                Y = pos.get_Y()
                Z = pos.get_Z()
                lon = pos.get_long()
                lat = pos.get_lat()
                C_time = time.time() # Get current time
                E_time = C_time - S_time # Calculate elapsed time
                myFile.write("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} \n".format(x, E_time,rawVal,corrVal,powVal,totVal,loopVal, X, Y, Z, lon, lat))    #write the data to file

                if self.vecsave_event.isSet():
                    vec = self.data.getVector(0)
                    vecRAW = self.data.getVector(1)
                    for i in range(0,len(vec)):
                        myFilevec.write("{0} ".format(vec[i]))   #write the data to file
                    myFilevec.write("\n")
                    for i in range(0,len(vecRAW)):
                        myFilevecRAW.write("{0} ".format(vecRAW[i]))   #write the data to file
                    myFilevecRAW.write("\n")

                #print E_time
                self.value_event.clear() # Resets the flag.
                count += 1
                if count == 3:
                    count = 0
                    self.step_event.clear()

        myFile.close()                                  #close and save the file
        if self.vecsave_event.isSet():
            myFilevec.close()  #close and save the file
            myFilevecRAW.close()  #close and save the file
        self.rec_event.clear()
        self.stop_event.clear()
        self.start_event.clear()
        self.pause_event.clear()
        self.step_event.clear()

    def plotter(self,filename,ax1):
        x = []
        y = []
        z = []
        vec = self.data.getVector()
        myfile = open(str(filename), "r")
        for line in myfile:
            coord = line.split(" ")
            #x.append(float(coord[7]))
            #y.append(float(coord[8]))
            #z.append(float(coord[9]))
        plot = ax1.plot(vec)
        #plot = ax1.plot([0,100],[0,100],[0,100],label = 'parametric curve')
 
    def recThread(self,filename,pos): #starts the thread that collects data in the background 
        thread = threading.Thread(target=self.record, args = (filename,pos,)) #creates threading object with function record()
        thread.daemon = True                                            #make sure that if we cancel main thread this thread cancels too
        thread.start()

    def recThread_samples(self,filename,noOfSamples,pos): #starts the thread that collects data in the background 
        thread = threading.Thread(target=self.record_samples, args = (noOfSamples,filename,pos,)) #creates threading object with function record()
        thread.daemon = True                                            #make sure that if we cancel main thread this thread cancels too
        thread.start()

    def recThread_time(self,filename,noOfTime,pos): #starts the thread that collects data in the background
        #records in minutes 
        thread = threading.Thread(target=self.record_time, args = (noOfTime,filename,pos,)) #creates threading object with function record()
        thread.daemon = True                                            #make sure that if we cancel main thread this thread cancels too
        thread.start()

    def vecsave(self):
        if self.rec_event.isSet() != True:
            self.vecsave_event.set()

    def vecnosave(self):
        if self.rec_event.isSet() != True:
            self.vecsave_event.clear()

    def pause(self):
        self.pause_event.set()

    def start(self):
        self.start_event.set()

    def stop(self):
        self.stop_event.set()
        self.start_event.set()

    def step(self):
        #self.step_event.set()
        self.start_event.set()
        self.pause_event.set()

    def step3(self):
        #self.step_event.set()
        self.value_event.clear()
        self.step_event.set()


