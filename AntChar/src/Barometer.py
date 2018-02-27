from src import *
from Adafruit_BME280 import *

class Barometer():
    
    def __init__(self):
    	baro = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

    def run(self):
    	while baro.running:
    	    baro.next()

    def readPressure(self):
        return self.read_pressure()
        
    def readTemperature(self):
        return self.read_temperature()
    
    def readHumidity(self):
        return self.read_humidity()
        
    def printPressure(self):
        pascals = self.readPressure()
        hectopascals = pascals / 100
        print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)

    def printTemperature(self):
        degrees = self.readTemperature()
        print 'Temp      = {0:0.3f} deg C'.fSormat(degrees)
        
    def printHumidity(self):
        humidity = self.readHumidity()
        print 'Humidity  = {0:0.2f} %'.format(humidity)
    
    def calcAltitude(self):
        pressDiff = (self.readPressure/1000)*(1/101.325) #difference between avarage pressure at sea level and current pressure [kPa]
        alt = math.log(pressDiff)*(-1)*(8.3143*288.15)/(0.02896*9.82)
        return alt
