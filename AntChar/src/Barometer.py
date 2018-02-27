from src import *
from Adafruit_BME280 import *

class Barometer():
    
    def __init__(self):
    	baro = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

    def run(self):
    	while baro.running:
    	    baro.next()

    def printPressure(self)
        pascals = self.read_pressure()
        hectopascals = pascals / 100
        print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)

    def printTemperature(self)
        degrees = self.read_temperature()
        print 'Temp      = {0:0.3f} deg C'.format(degrees)
        
    def printHumidity(self)
        humidity = self.read_humidity()
        print 'Humidity  = {0:0.2f} %'.format(humidity)
