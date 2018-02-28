from src import *
import wiringpi2 as wpi


class Antenna()
    
    def __init__(self):
        wpi.wiringPiSetup()
        self.currLoop = 1    #stores what loop is currently active 
        self.counter = 0     #sets the counter to 0.
        wpi.pinMode(2,0) #selects GPIO #21 on the odroid board
        wpi.pinMode(0,0) #selects GPIO #22 on the odroid board

    def loopOne(self):
        wpi.digitalWrite(0,1)
        wpi.digitalWrite(2,0)
        currLoop = 1

    def loopTwo(self):
        wpi.digitalWrite(0,1)
        wpi.digitalWrite(2,1)
        currLoop = 2
    
    def loopThree(self):
        wpi.digitalWrite(0,0)
        wpi.digitalWrite(2,1)
        currLoop = 3
    
    def reset(self):
        wpi.digitalWrite(0,0)
        wpi.digitalWrite(2,0)
        currLoop = 0
    
    def loopSwitch(self)
        if currLoop == 1:
            self.loopTwo()
                
        elif currLoop == 2:
            self.loopThree()
            
        elif currLoop == 3:
            self.loopOne()
    
    def currentLoop(self): #returns the current loop, 0 for none active
        counter = counter + 1 #Keeps track of how many samples 
                              #GnuRadio has stored for the current loop
        
        if counter > 25:
            counter = 0 #resets the counter after a certain value
            loopSwitch() #switch to next loop
        
        return currLoop
    
    def getCount(self):
        return counter
