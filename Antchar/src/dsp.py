from src import *
from gnuradiodatacollector import gnuradiodatacollector
from Data import Data
import time
import threading
from gr_antenna import gr_antenna

class dsp():

    def __init__(self,data,endEvent,processEvent):
        self.endEvent = endEvent
        self.processEvent = processEvent
        self.data = data
        self.del_time = 0
        self.auto_run = True
        self.dataEvent = threading.Event()
        self.recloopEvent = threading.Event()
        self.dspProcess = gnuradiodatacollector(data,self.processEvent)
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
        self.dspProcess.start()
        time.sleep(2)
        while self.endEvent.isSet() != True:
            if self.auto_run == True:
                self.processEvent.wait()
                if self.data.getVector(1)[0] != 0:
                    self.dspProcess.set_select(1) # Null source
                    self.data.setData(self.antenna.getCurrentLoop(),3)
                    self.dataEvent.set()
                    self.loop()
                    self.recloopEvent.wait()
                    self.recloopEvent.clear()
                    time.sleep(self.del_time)
                    self.dspProcess.set_select(0)
                    self.processEvent.clear()

                else:
                    self.processEvent.clear()

            else:
                time.sleep(0.1)
        self.endProcess()

    def lock(self):
        self.auto_run = False

    def unlock(self):
        self.auto_run = True

    def getLockMode(self):
        return not self.auto_run

    def update(self):
        self.dspProcess.reset()
        self.dspProcess.start()
        self.dspProcess.wait()
        self.data.setData(self.antenna.getCurrentLoop(),3)
        self.dataEvent.set()
        self.loop()

    def delay(self,del_time):
        self.del_time = del_time

    def getDelay(self):
        return self.del_time

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

    def getLoop(self):
        return self.antenna.getCurrentLoop()

    def getLoopMode(self):
        return self.autoSwitch

    def getDataEvent(self):
        return self.dataEvent

    def getRecloopEvent(self):
        return self.recloopEvent

    def getDecimation(self):
        return self.dspProcess.get_FIR_decimation()

    def setDecimation(self, FIR_decimation):
        self.dspProcess.set_FIR_decimation(FIR_decimation)

    def getCutoff(self):
        return self.dspProcess.get_cutoff()

    def setCutoff(self, cutoff):
        self.dspProcess.set_cutoff(cutoff)

    def getTransition(self):
        return self.dspProcess.get_transition()

    def setTransition(self, transition):
        self.dspProcess.set_transition(transition)
