from src import *

class Calibration():
    def __init__(self, data, rec, pos,recEvent):
        self._data = data
        self._rec = rec
        self._pos = pos
        self._calThread = threading.Thread(target = self.recCalibration)
        self.nf_max = 0
        self._recEvent = recEvent

    def calibrate(self):

        myFile = open("calibration.txt",'r')
        i = 0
        for line in myFile:
            i += 1
            currLine = line.split(" ")
            #print self.nf_max
            if i == 2:
                self.nf_max = float(currLine[2])
                #print currLine[2]
            elif i > 2:
                if float(currLine[2]) > self.nf_max:
                    self.nf_max = float(currLine[2])

        myFile.close()

    def recCalibration(self):
        self._rec.recThread_samples("calibration", 50, self._pos)
        while self._recEvent.isSet():
            time.sleep(2)
        self.calibrate()

    def calibrationThread(self):
        if self._calThread.isAlive() != True:
            self._calThread = threading.Thread(target = self.recCalibration)
            self._calThread.daemon = True
            self._calThread.start()
        else:
            raise IOError


    def getNoiseFloor(self):
        return self.nf_max

    def getSNR(self):
        return (self._data.getData(0)-self.nf_max)
