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
        myFile.write("Nr Etime Raw dBm dBmW/m2 sum:dBmW/m2 loop X Y Z long lat droneData: lat long alt pitch yaw roll heading\n")
        while ind < noOfSamples and self.stop_event.isSet() != True:
            self.start_event.clear()
            ind += 1
            self.value_event.wait() # Wait untill new value is available
            rawVal = self.data.getData(0) #collect the measurement data
            corrVal = self.data.getData(1) #collect the measurement data
            powVal = self.data.getData(2) #collect the measurement data
            loopVal = self.data.getData(3) #collect the measurement data
            totVal = self.data.getData(4) #collect the measurement data
            dronedata = self.data.getDroneData()
            X = pos.get_X()
            Y = pos.get_Y()
            Z = pos.get_Z()
            lon = pos.get_long()
            lat = pos.get_lat()
            C_time = time.time() # Get current time
            E_time = C_time - S_time # Calculate elapsed 
            myFile.write("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} \n".format(ind, E_time,rawVal,corrVal,powVal,totVal,loopVal, X, Y, Z, lon, lat, dronedata[0],dronedata[1],dronedata[2],dronedata[3],dronedata[4],dronedata[5],dronedata[6]))    #write the data to file
            if self.vecsave_event.isSet():
                vec = self.data.getVector(0)
                vecRAW = self.data.getVector(1)
                for i in range(0,len(vec)-1):
                    myFilevec.write("{0} {1}".format(vec[i],","))   #write the data to file
                myFilevec.write("{0}".format(vec[len(vec)-1]))
                myFilevec.write("\n")
                for i in range(0,len(vecRAW)-1):
                    myFilevecRAW.write("{0} {1}".format(vecRAW[i],","))   #write the data to file
                myFilevecRAW.write("{0}".format(vecRAW[len(vecRAW)-1]))
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
        myFile.write("Nr Etime Raw dBm dBmW/m2 sum:dBmW/m2 loop X Y Z long lat droneData: lat long alt pitch yaw roll heading\n")
        while E_time < noOfTime and self.stop_event.isSet() != True:
            self.start_event.clear()
            self.value_event.wait() # Wait untill new value is available
            x += 1 # Amount of samples
            rawVal = self.data.getData(0) #collect the measurement data
            corrVal = self.data.getData(1) #collect the measurement data
            powVal = self.data.getData(2) #collect the measurement data
            loopVal = self.data.getData(3) #collect the measurement data
            totVal = self.data.getData(4) #collect the measurement data
            dronedata = self.data.getDroneData()
            X = pos.get_X()
            Y = pos.get_Y()
            Z = pos.get_Z()
            lon = pos.get_long()
            lat = pos.get_lat()
            C_time = time.time() # Get current time
            E_time = C_time - S_time # Calculate elapsed 
            myFile.write("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} \n".format(x, E_time,rawVal,corrVal,powVal,totVal,loopVal, X, Y, Z, lon, lat, dronedata[0],dronedata[1],dronedata[2],dronedata[3],dronedata[4],dronedata[5],dronedata[6]))    #write the data to file
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
        self.pause_event.clear()
        self.step_event.clear()
        self.start_event.clear()
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
        myFile.write("Nr Etime Raw dBm dBmW/m2 sum:dBmW/m2 loop X Y Z long lat droneData: lat long alt pitch yaw roll heading\n")
        while self.stop_event.isSet() != True:
            if self.step_event.isSet() or self.start_event.isSet():
                self.value_event.wait() # Wait untill new value is available
                x += 1 # Amount of samples
                rawVal = self.data.getData(0) #collect the measurement data
                corrVal = self.data.getData(1) #collect the measurement data
                powVal = self.data.getData(2) #collect the measurement data
                loopVal = self.data.getData(3) #collect the measurement data
                totVal = self.data.getData(4) #collect the measurement data
                dronedata = self.data.getDroneData()
                X = pos.get_X()
                Y = pos.get_Y()
                Z = pos.get_Z()
                lon = pos.get_long()
                lat = pos.get_lat()
                C_time = time.time() # Get current time
                E_time = C_time - S_time # Calculate elapsed time
                myFile.write("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} \n".format(x, E_time,rawVal,corrVal,powVal,totVal,loopVal, X, Y, Z, lon, lat, dronedata[0],dronedata[1],dronedata[2],dronedata[3],dronedata[4],dronedata[5],dronedata[6]))    #write the data to file

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

    def getVecMode(self):
        return self.vecsave_event.isSet()

    def plotter(self,filename,ax1):
        x = []
        y = []
        z = []
        val = []
        i = 0
        vec = self.data.getVector(0)
        myfile = open(str(filename), "r")
        for line in myfile:
            i += 1
            coord = line.split(" ")
            if i>2:
                val.append(float(coord[2]))
                #y.append(float(coord[8]))
                #z.append(float(coord[9]))
        plot = ax1.plot(val)
        #plot = ax1.plot([0,100],[0,100],[0,100],label = 'parametric curve')

    def plottpos(self,filename,ax1,pos):
        s_origin = [6335821.4310934115, np.rad2deg(1.0434507105248343), np.rad2deg(0.3080101271502993)]
        t_mat = [[0.38771524931916784, 0.38771524931916784, -0.8362737416006499], [-0.41419889165158386, 0.883767445234581, 0.21770250549348494], [0.823478089325985, 0.26197707569349843, 0.5032413419137067]]
        c_origin = [5217410.1263874294, 1659839.9706340474, 3188447.2791090696]
        x = []
        y = []
        z = []
        s_coord = [s_origin[0],0,0]
        c_coord = [0,0,0]
        lon = []
        i = 0
        vec = self.data.getVector(0)
        myfile = open(str(filename), "r")
        f = ((np.cos(np.deg2rad(s_origin[1]))/np.sin(np.deg2rad(s_origin[1])))) # GPS Correction factor

        for line in myfile:
            i += 1
            coord = line.split(" ")
            if i>2:
                if coord[7] != "nan":

                    s_coord[2] = np.deg2rad(f*(float(coord[10])-s_origin[2])+ s_origin[2])
                    s_coord[1] = np.deg2rad(float(coord[11]))
                    c_coord = pos.spherical_to_cartisian(s_coord)
                    v1 = pos.vector_subtraction(c_origin,c_coord)
                    h1 = pos.vector_scalar_mult(pos.vector_normalize(c_coord),1) # generate hight above ground along new coordinate 
                    r1 = pos.vector_subtraction(v1,h1) # calculate the r vector from origin to current postion
                    r1 = pos.matrix_vec_mult(t_mat,r1)
                    x.append(r1[0])
                    y.append(r1[1])
                    z.append(r1[2])

        #plot = ax1.plot(val)
        plot = ax1.plot(x,y,label = 'parametric curve')
        

    def plottvec(self,filename,vecline,ax1):
        val = []
        myfile = open(str(filename),"r")
        val = myfile.readlines()
        fileVec = val[int(vecline)].split("\n")
        val = ast.literal_eval(fileVec[0])
        plot = ax1.plot(val)
 
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
        self.value_event.clear()
        self.start_event.set()

    def stop(self):
        self.stop_event.set()
        time.sleep(0.2) # Wait for stop sequence to init
        self.start_event.set() 

    def step(self):
        #self.step_event.set()
        self.value_event.clear()
        self.step_event.set()
        #self.start_event.set()
        #self.pause_event.set()

    def step3(self):
        #self.step_event.set()
        self.value_event.clear()
        self.step_event.set()


