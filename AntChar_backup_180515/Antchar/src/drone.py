from src import *
from dronekit import connect, VehicleMode
import time
import os.path
import threading
from Data import Data
class drone():

    def __init__(self,endEvent,data):
        self.data = data
        self.endEvent = endEvent
        self.pix = ""
        self.ready_event = threading.Event()
        self.ready_event.clear()
        self.connect_thread = threading.Thread(target = self.connectT)
        self.data_thread = threading.Thread(target = self.dataT)
        self.connect_thread.deamon = True
        self.data_thread.deamon = True
        self.droneStat = False
        self.lat = 0
        self.lon = 0
        self.alt = 0
        self.pitch = 0
        self.yaw = 0
        self.roll = 0
        self.heading = 0
        self.data.setDroneData([self.lon,self.lat,self.alt,self.pitch,self.yaw,self.roll,self.heading])

    def connect(self): 
        if self.connect_thread.isAlive() or self.data_thread.isAlive():
            raise IOError
        else:
            self.connect_thread = threading.Thread(target = self.connectT)
            self.data_thread = threading.Thread(target = self.dataT)
            self.connect_thread.deamon = True
            self.data_thread.deamon = True
            self.connect_thread.start()
            time.sleep(1)
            self.data_thread.start()

    def connectT(self):
        if os.path.exists("/dev/ttyUSB0"):
            self.droneStat = True
            self.pix = connect("/dev/ttyUSB0",_initialize=True,status_printer= False ,baud=57600,wait_ready=True)
            self.ready_event.set()
        else:#except SerialException: 
            self.droneStat = False 
        self.data.setDroneStat(self.droneStat)

    def dataT(self):
        if self.droneStat:
            self.ready_event.wait()
            while self.endEvent.isSet() != True and self.ready_event.isSet():
                if self.pix.last_heartbeat > 5:
                    self.ready_event.clear()
                    self.droneStat = False 
                    self.data.setDroneStat(self.droneStat)
                self.lat = self.pix.location.global_frame.lat
                self.lon = self.pix.location.global_frame.lon
                self.alt = self.pix.location.global_frame.alt
                self.pitch = self.pix.attitude.pitch
                self.yaw = self.pix.attitude.yaw
                self.roll = self.pix.attitude.roll
                self.heading = self.pix.heading
                self.data.setDroneData([self.lon,self.lat,self.alt,self.pitch,self.yaw,self.roll,self.heading])
                time.sleep(0.1)

    def getStatus(self):
        if self.ready_event.isSet():
            return True
        else:
            return False

    def getData(self):
        return [self.lon,self.lat,self.alt,self.pitch,self.yaw,self.roll,self.heading]

    def get_ready_event(self):
        return self.ready_event


def main():
    data = Data()
    endEvent = threading.Event()
    dronec = drone(endEvent,data)
    dronec.connect()
    event = dronec.get_ready_event()
    event.wait()
    for i in range(0,10):
        time.sleep(1)
        print dronec.getData()
    endEvent.set()



if __name__ == '__main__':
    main()

