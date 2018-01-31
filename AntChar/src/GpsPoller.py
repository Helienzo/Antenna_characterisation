from src import *
class GpsPoller(threading.Thread):
    
    def __init__(self):
    	threading.Thread.__init__(self)
    	global gpsd #bring it in scope
    	gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    	#gpsd.stream(WATCH_NMEA) #starting the stream of info
        #thread.daemon = True
    	self.current_value = None
    	self.running = True #setting the thread running to true

    def run(self):
    	global gpsd
    	while gpsp.running:
    	    gpsd.next()
gpsp = GpsPoller()
class position(GpsPoller):
    Xorigin = 0
    Yorigin = 0
    Zorigin = 0
    Xcord = 0
    Ycord = 0
    Zcord = 0
    XfromO = 0
    YfromO = 0
    ZfromO = 0
    theta = 0
    phi = 0
    alt = 0
    R = 6.3781*100000
    def data(self):
        while gpsp.running:
            self.theta = gpsd.fix.latitude
            self.phi = gpsd.fix.longitude
            self.alt = gpsd.fix.altitude

            self.Xcord = (self.R)*math.sin(self.theta)*math.cos(self.phi)
            self.Ycord = (self.R)*math.sin(self.theta)*math.sin(self.phi)
            self.Zcord = (self.R)*math.cos(self.theta)

            self.XfromO = self.Xcord - self.Xorigin
            self.YfromO = self.Ycord - self.Yorigin
            self.ZfromO = self.Zcord - self.Zorigin
            time.sleep(0.1)
    def set_origin(self):
        self.Xorigin = self.Xcord
        self.Yorigin = self.Ycord
        self.Zorigin = self.Zcord

    def get_X(self):
        return self.XfromO

    def get_Y(self):
        return self.YfromO

    def get_Z(self):
        return self.YfromO

    def __init__(self): #starts the thread that collects data in the background 
        thread = threading.Thread(target=self.data, args = ())
        thread.daemon = True
        thread.start()
        thread.running = True
    
    def stop(self): #starts the thread that collects data in the background 
        print ""
