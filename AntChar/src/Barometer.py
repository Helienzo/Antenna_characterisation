from src import *
from Adafruit_BME280 import *

class Barometer():
    
    def __init__(self):
    	baro = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

    def run(self):
    	global baro
    	while baro.running:
    	    baro.next()
