from src import *

class drone():

    def __init__(self):
        self.pix = ""
        self.ready_event = threading.Event()
        self.thread = threading.Thread(target = self.data) 

    def connect(self):    
        self.thread.start()

    def data(self):
        if os.path.exists("/dev/ttyUSB0"):
            self.pix = connect("/dev/ttyUSB0",_initialize=True,status_printer= False ,baud=57600,wait_ready=True)
            self.ready_event.set()
        else:#except SerialException: 
            print "no device avilable"  

    def getStatus(self):
