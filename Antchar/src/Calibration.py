from src import *

class Calibration():
    def __init__(self, data, rec, pos):
        self._data = data
        self._rec = rec
        self._pos = pos
        self._calThread = threading.Thread(target = self.recCalibration)
        self.nf_max = 0

    def calibrate(self):
        myFile = open("calibration.txt",'r')
        for line in myFile:
            currLine = line.split(" ")
            if line > 1:
                self.nf_max = float(currLine[2])
            if line > 2:
                if float(currLine[2]) > self.nf_max:
                    self.nf_max = currLine[2]

    def recCalibration(self):
        self._rec.recThread_samples("calibration", 100, self._pos)
        self._recEvent.wait()
        time.sleep(1)
        self.calibrate()

    def calibrationThread(self):
        if !self._calThread.isAlive():
            self._calThread = threading.Thread(target = self.recCalibration)
            self._calThread.daemon = True
            self._calThread.start()
        else:
            raise IOError


    def getNoiseFloor():
        return self.nf_max

    def getSNR(self):
        return (data.getData(2) - self.nf_max)
