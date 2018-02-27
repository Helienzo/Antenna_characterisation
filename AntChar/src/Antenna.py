from src import *

import wiringpi2 as wpi
import time

class Antenna(threading.Thread)
    
    def __init__(self) 
        wpi.wiringPiSetup()
        wpi.pinMode(2,0) #selects GPIO #21 on the odroid board
        wpi.pinMode(0,0) #selects GPIO #22 on the odroid board
        self.currLoop = 0    #stores what loop is currently active 
        threading.Thread.__init__(self)
    	global ant #bring it in scope
    	self.current_value = None
    	self.running = True #setting the thread running to true

    def loop_one(self):
        wpi.digitalWrite(0,1)
        wpi.digitalWrite(2,0)
        currLoop = 1

    def loop_two(self):
        wpi.digitalWrite(0,1)
        wpi.digitalWrite(2,1)
        currLoop = 2
    
    def loop_three(self):
        wpi.digitalWrite(0,0)
        wpi.digitalWrite(2,1)
        currLoop = 3
    
    def reset(self):
        wpi.digitalWrite(0,0)
        wpi.digitalWrite(2,0)
        currLoop = 0
    
    def currentLoop(self): #returns the current loop, 0 for none active
        return currLoop
