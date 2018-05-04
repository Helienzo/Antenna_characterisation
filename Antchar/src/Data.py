from src import *
import numpy as np
class Data():

    def __init__(self):
        self.vector_raw = []
        self.vector_log = []
        self.rawData = [0]
        self.dbmCorr = [0]
        self.power = [0,0,0]
        self.totPower = [0]
        self.currentLoop = [0]
        self.NF = 0
        self.droneData = []
        self.droneStat = False
    
    #function for other classes to store data in this class
    def setData(self,data,var):
        
        if var == 0:
            self.rawData[0] = data

        elif var == 1:
            self.dbmCorr[0] = data

        elif var == 2:
            
            self.power[2] = self.power[1]
            self.power[1] = self.power[0]
            self.power[0] = data
            self.totPower[0] = self.polAdder(self.power)
            
        elif var == 3:
            self.currentLoop[0] = data
    
    def setDroneData(self,data):
        self.droneData = data

    def setDroneStat(self,stat):
        self.droneStat = stat

    def getDroneData(self):
        return self.droneData

    def getDroneStat(self):
        return self.droneStat

    def esimateNF(self):
        vec_len = len(self.vector_log)
        
        return self.NF

    def setVector(self, inVec,var):
        #self.vector = inVec
        if var == 0:        
            self.vector_log = []
            self.vector_log.extend(inVec)
        elif var == 1:
            self.vector_raw = []
            self.vector_raw.extend(inVec)

    def getVector(self,var):
        if var == 0: 
            return self.vector_log
        elif var == 1: 
            return self.vector_raw
        else:
            return 0

    #function for other classes to retrieve data
    def getData(self, var):
        
        if var == 0:
            return self.rawData[0]

        elif var == 1:
            return self.dbmCorr[0]

        elif var == 2:            
            return self.power[0]

        elif var == 3:
            return self.currentLoop[0]
            
        elif var == 4:
            return self.totPower[0]

    
    #summarizes data from the three loops to retrieve final power value
    def polAdder(self,power):
        res = 10*np.log10(np.sqrt((0.001*(10**(power[0]/10)))**2 + (0.001*(10**(power[1]/10)))**2 + (0.001*(10**(power[2]/10)))**2)*1000)
        return res 
    
    
    
