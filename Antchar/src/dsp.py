from src import *
from gnuradiodatacollector import gnuradiodatacollector
from Data import Data
import time
import threading
from gr_antenna import gr_antenna

class dsp():

    def __init__(self,data,endEvent):
        self.endEvent = endEvent
        self.data = data
        self.auto_run = True
        self.dataEvent = threading.Event()
        self.dspProcess = gnuradiodatacollector(data)
        dec = self.dspProcess.get_FIR_decimation()
        vlen = self.dspProcess.get_fft_size()
        self.antenna = Antenna(dec,vlen)
        self.controller_thread = threading.Thread(target = self.controller)
        self.controller_thread.deamon = True 
        self.controller_thread.start()
        self.currentLoop = 0
        self.autoSwitch = True


    def endProcess(self):
        self.dspProcess.stop()
        self.dspProcess.wait()

    def controller(self):
        while self.endEvent.isSet() != True:
            if self.auto_run == True:
                self.dspProcess.reset()
                self.dspProcess.start()
                self.dspProcess.wait()
                self.data.setData(self.antenna.getCurrentLoop(),3)
                self.dataEvent.set()
                self.loop()
                #time.sleep(3)
            else:
                time.sleep(0.1)
        self.endProcess()

    def lock(self):
        self.auto_run = False

    def unlock(self):
        self.auto_run = True

    def update(self):
        self.dspProcess.reset()
        self.dspProcess.start()
        self.dspProcess.wait()
        self.data.setData(self.antenna.getCurrentLoop(),3)
        self.dataEvent.set()
        self.loop()
        #time.sleep(3)
    
    def loop(self):
        if self.autoSwitch:
            self.antenna.loopSwitch()
        else:
            self.antenna.setLoop(self.currentLoop)

    def set_c_freq(self,freq):
        self.dspProcess.set_c_freq(freq)

    def get_c_freq(self):
        return self.dspProcess.get_c_freq()

    def set_auto_loop(self,mode):
        if mode == 1:
            self.autoSwitch = True
        else:
            self.autoSwitch = False

    def set_loop(self,loop):
        self.autoSwitch = False
        self.currentLoop = loop

    def getDataEvent(self):
        return self.dataEvent



#def main():
#    data = Data()
#    dspmain = dsp(data)
#    #print data.getVector()
    
    
    



#if __name__ == '__main__':
#    main()
