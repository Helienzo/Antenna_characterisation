from src import *
import time
import numpy as np
from Adafruit_BME280 import *

class Barometer():
    baro = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
    #def __init__(self):
    start_T = baro.read_temperature()
    start_P = baro.read_pressure()/100.0

    def readPressure(self):
        temp = self.baro.read_temperature() # Call temerature
        return np.float(self.baro.read_pressure()/100.0)
        
    def readTemperature(self):
        return np.float(self.baro.read_temperature())
    
    def readHumidity(self):
        temp = self.baro.read_temperature() # Call temerature
        return np.float(self.baro.read_humidity())
        
    def printPressure(self):
        pascals = self.readPressure()
        hectopascals = pascals
        print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)

    def printTemperature(self):
        degrees = self.readTemperature()
        print 'Temp      = {0:0.3f} deg C'.format(degrees)
        
    def printHumidity(self):
        humidity = self.readHumidity()
        print 'Humidity  = {0:0.2f} %'.format(humidity)
    def calcAltitude(self):
        pressDiff = (self.p0/self.readPressure())#*(1/101.325) #difference between avarage pressure at sea level and current pressure [kPa]
        temp = self.readTemperature()
        h = (287.05/9.80665)*np.log(pressDiff)*((297.15+298.15)/2.0)

        #alt = np.log(pressDiff)*(-1)*(8.3143*288.15)/(0.02896*9.82)
        return h

def main():
    
    running = True
    bar = Barometer()
    try:
        while running:
            bar.printTemperature()
            #bar.printPressure()
            print bar.readPressure()
            print bar.calcAltitude()
            time.sleep(1)
    except KeyboardInterrupt, SystemExit:
        running = False
           
if __name__ == '__main__':
    main()
