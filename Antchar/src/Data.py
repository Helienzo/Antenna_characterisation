from src import *
import numpy as np
class Data():

    def __init__(self):
        self.vector = []
        self.rawData = [0]
        self.dbmCorr = [0]
        self.power = [0,0,0]
        self.totPower = [0]
        self.currentLoop = [0]
    
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
    

    def setVector(self, inVec):
        #self.vector = inVec        
        self.vector = []
        self.vector.extend(inVec)

    def getVector(self):
        return self.vector


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
    
    
    
