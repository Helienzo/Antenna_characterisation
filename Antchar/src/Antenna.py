from src import *
#import wiringpi2 as wpi


class Antenna():

    def __init__(self,dec,v_len):
        self.dec = dec
        self.v_len = v_len
        self.count_nr = int(self.dec*self.v_len)
        print self.count_nr
        wpi.wiringPiSetupGpio()
        self.currLoop = 1    #stores what loop is currently active
        self.counter = 0     #sets the counter to 0.
        self.pin1 = 21
        self.pin2 = 22
        wpi.pinMode(self.pin1,wpi.GPIO.OUTPUT) #selects GPIO #21 on the odroid board
        wpi.pinMode(self.pin2,wpi.GPIO.OUTPUT) #selects GPIO #22 on the odroid board

    def setLoop(self,loop):
        if loop == 1:
            self.loopOne()
        elif loop == 2:
            self.loopTwo()
        elif loop == 3:
            self.loopThree()
        else:
            self.reset()

    def loopOne(self):
        wpi.digitalWrite(self.pin2,1)
        #time.sleep(0.05)
        wpi.digitalWrite(self.pin1,0)
        self.currLoop = 1

    def loopTwo(self):
        wpi.digitalWrite(self.pin2,1)
        wpi.digitalWrite(self.pin1,1)
        self.currLoop = 2

    def loopThree(self):
        wpi.digitalWrite(self.pin2,0)
        wpi.digitalWrite(self.pin1,1)
        self.currLoop = 3

    def reset(self):
        wpi.digitalWrite(self.pin2,0)
        wpi.digitalWrite(self.pin1,0)
        self.currLoop = 0

    def loopSwitch(self):
        if self.currLoop == 1:
            self.loopTwo()

        elif self.currLoop == 2:
            self.loopThree()

        elif self.currLoop == 3:
            self.loopOne()

    def currentLoop(self,n_samp,auto): #returns the current loop, 0 for none active
        self.counter = self.counter + n_samp #Keeps track of how many samples
                              #GnuRadio has stored for the current loop

        if self.counter > (self.count_nr-1):
            #print "loop"+ str(self.currLoop)
            #print "amount"+ str(self.counter)
            self.counter = 0 #resets the counter after a certain value
            if auto != 0:
                self.loopSwitch() #switch to next loop

        #return self.currLoop

    def getCurrentLoop(self):
        return self.currLoop

    def getCount(self):
        return self.counter
