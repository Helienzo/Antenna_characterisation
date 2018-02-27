from src import *
from Adafruit_BME280 import *

class Barometer(threading.Thread):
    
    def __init__(self):
    	threading.Thread.__init__(self)
    	global baro #bring it in scope
    	baro = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
    	self.current_value = None
    	self.running = True #setting the thread running to true

    def run(self):
    	global baro
    	while baro.running:
    	    baro.next()
