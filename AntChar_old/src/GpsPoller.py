#import __init__
from src import *
from Barometer import Barometer
import numpy as np
from gps import *
import threading
import numpy as np
import math
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
import csv
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

    def __init__(self): #starts the thread that collects data in the background 
        thread = threading.Thread(target=self.data, args = ())
        thread.daemon = True
        thread.start()
        thread.running = True

    def e_rad(self,lat):
        #a = Equatorial radius (6378.1370 km)
        #b = Polar radius (6356.7523 km)
        #e is the eccentricity of the ellipsoid
        #R' = a * (1 - e^2) / (1 - e^2 * sin^2(lat))^(3/2)
        a = 6378.1370 # km
        b = 6356.7523 # km
        e = 1 - b**2/a**2
        R = a*(1 - e)/((1 - e*np.sin(lat)**2)**(3/2))
        return R*1000
    def spherical_to_cartisian(self,s):
        c = [0,0,0]
        c[0] = s[0]*np.sin(s[1])*np.cos(s[2])
        c[1] = s[0]*np.sin(s[1])*np.sin(s[2])
        c[2] = s[0]*np.cos(s[1])
        return c

    def cartesian_to_spherical(self,c):
        s = [0,0,0]
        s[0] = np.sqrt(c[0]**2 + c[1]**2 + c[2]**2)
        s[1] = np.arccos(c[2]/s[0])
        s[2] = np.arctan(c[1]/c[0])
        return s

    def vector_subtraction(self,v1,v2):
        v_ret = [0,0,0]
        v_ret[0] = v1[0]-v2[0]
        v_ret[1] = v1[1]-v2[1]
        v_ret[2] = v1[2]-v2[2]
        return v_ret

    def vector_add(self,v1,v2):
        v_ret = [0,0,0]
        v_ret[0] = v1[0]+v2[0]
        v_ret[1] = v1[1]+v2[1]
        v_ret[2] = v1[2]+v2[2]
        return v_ret

    def vector_angle(self,b_1,b_2):
        l_1 = np.sqrt( b_1[0]*b_1[0] + b_1[1]*b_1[1] + b_1[2]*b_1[2] )
        l_2 = np.sqrt( b_2[0]*b_2[0] + b_2[1]*b_2[1] + b_2[2]*b_2[2] )
        ang_1 = np.arccos((b_1[0]*b_2[0] + b_1[1]*b_2[1] + b_1[2]*b_2[2]) / (l_1*l_2))
        return ang_1

    def vector_length(self,b_1):
        l_1 = np.sqrt( b_1[0]*b_1[0] + b_1[1]*b_1[1] + b_1[2]*b_1[2] )
        return l_1  
        
    def vector_scalar_mult(self,vec,scal):
        ret_vec = [0,0,0]
        ret_vec[0] = vec[0]*scal
        ret_vec[1] = vec[1]*scal
        ret_vec[2] = vec[2]*scal
        return ret_vec

    def vector_normalize(self,vec):
        ret_vec = [0,0,0]
        l = self.vector_length(vec)
        ret_vec = self.vector_scalar_mult(vec,1.0/l)
        return ret_vec

    def vector_mult(self,v1,v2):
        ret_vec = [0,0,0]
        ret_vec[0] = v1[0]*v2[0]
        ret_vec[1] = v1[1]*v2[1]
        ret_vec[2] = v1[2]*v2[2]
        return ret_vec

    def dot_prod(self,v1,v2):
        tmp = self.vector_mult(v1,v2)
        val = tmp[0]+tmp[1]+tmp[2]
        return val

    def cross_prod(self,v1,v2):
        ret_vec = [ v1[1]*v2[2]-v1[2]*v2[1] ,-(v1[0]*v2[2]-v1[2]*v2[0]) , v1[0]*v2[1]-v1[1]*v2[0] ]
        return ret_vec

    def gen_base_trans_mat(self,e1,e2,e3):
        ret_mat = np.zeros((3,3))
        ret_mat[0][0] = e1[0]
        ret_mat[1][0] = e1[1]
        ret_mat[2][0] = e1[2]

        ret_mat[0][1] = e2[0]
        ret_mat[1][1] = e2[1]
        ret_mat[2][1] = e2[2]

        ret_mat[0][2] = e3[0]
        ret_mat[1][2] = e3[1]
        ret_mat[2][2] = e3[2]
        return ret_mat

    def matrix_vec_mult(self,mat,vec):
        ret_vec = [0,0,0]
        ret_vec[0] = mat[0][0]*vec[0] + mat[0][1]*vec[1] + mat[0][2]*vec[2]
        ret_vec[1] = mat[1][0]*vec[0] + mat[1][1]*vec[1] + mat[1][2]*vec[2]
        ret_vec[2] = mat[2][0]*vec[0] + mat[2][1]*vec[1] + mat[2][2]*vec[2]
        return ret_vec

    s_origin = [6335439.2988979854, 1.0451881322659466, 0.30858128427527615] #R, lat, long typical in sweden
    c_origin = [5221416.445116709, 1664399.1994215634, 3178738.2279216764] # typical in sweden
    s_coord = [0,0,0]  #R, lat, long
    c_coord = [0,0,0]
    Xcord = 0
    Ycord = 0
    Zcord = 0
    theta = 0
    phi = 0
    alt = 0
    temp = 0
    o_temp = 25
    pressure = 0
    o_pressure = 1044
    R = 6335439.2988979854
    bar = Barometer()
    z_o = [0,0,0]
    y_o = [0,0,0]
    x_o = [0,0,0]
    v1 = [0,0,0]
    h1 = [0,0,0]
    r1 = [0,0,0]
    t_mat = [[ 0.38655106,  0.38655106, -0.83735091],[-0.41393039,  0.88405905,  0.21702817],[ 0.82416013,  0.26271252,  0.5017392 ]] # Transfer from earth to local system

    def calcAltitude(self):
        pressDiff = (self.o_pressure/self.pressure)
        h = (287.05/9.80665)*np.log(pressDiff)*((2*273.15 + self.temp + self.o_temp)/2.0)
        return h

    def data(self):
        while gpsp.running:
            self.theta = gpsd.fix.latitude
            self.phi = gpsd.fix.longitude
            self.alt = gpsd.fix.altitude
            self.temp = self.bar.readTemperature()
            self.pressure = self.bar.readPressure() # Get pressure in heteropascal
            
            self.s_coord = [self.R, np.deg2rad(self.theta), np.deg2rad(self.phi)] # get spherical gps coordinates
            self.c_coord = self.spherical_to_cartisian(self.s_coord) # convert from spherical to cartesian
            self.v1 = self.vector_subtraction(self.c_origin,self.c_coord) # get vector from origin to current position
            self.h1 = self.vector_scalar_mult(self.vector_normalize(self.c_coord),self.calcAltitude()) # generate hight above ground along new coordinate 
            self.r1 = self.vector_subtraction(self.v1,self.h1) # calculate the r vector from origin to current postion
            self.r1 = self.matrix_vec_mult(self.t_mat,self.r1)
            self.Xcord = self.r1[0]
            self.Ycord = self.r1[1]
            self.Zcord = self.r1[2]
            time.sleep(0.1)

    def test(self,filename,start):
        self.s_coord[1] = np.deg2rad(float(start[0]))
        self.s_coord[2] = np.deg2rad(float(start[1]))
        self.temp = 25#self.bar.readTemperature()
        self.pressure = 1024#self.bar.readPressure()
        self.set_origin()
        print self.c_origin[1]
        print self.c_origin[2]
        wFile = open("xyz.txt", "w")
        myFile = open(str(filename), "r") 
        for line in myFile:
            coord = line.split(" ")
            self.theta = float(coord[8])
            self.phi = float(coord[9])
            self.temp = 25#self.bar.readTemperature()
            self.pressure = 1024#self.bar.readPressure() # Get pressure in heteropascal
            
            self.s_coord = [self.R, np.deg2rad(self.theta), np.deg2rad(self.phi)] # get spherical gps coordinates
            self.c_coord = self.spherical_to_cartisian(self.s_coord) # convert from spherical to cartesian
            self.v1 = self.vector_subtraction(self.c_origin,self.c_coord) # get vector from origin to current position
            self.h1 = self.vector_scalar_mult(self.vector_normalize(self.c_coord),self.calcAltitude()) # generate hight above ground along new coordinate 
            self.r1 = self.vector_subtraction(self.v1,self.h1) # calculate the r vector from origin to current postion

            self.r1 = self.matrix_vec_mult(self.t_mat,self.r1)
            self.Xcord = self.r1[0]
            self.Ycord = self.r1[1]
            self.Zcord = self.r1[2]

            wFile.write("{0} {1} {2} \n".format(self.Xcord,self.Ycord, self.Zcord))
            #time.sleep(0.1)
        print self.s_origin
        myFile.close()
        wFile.close()
        print "Done"

    def set_origin(self):

        self.R = self.e_rad(self.theta) # Calculate earth radious at current latitude
        self.s_coord[0] = self.R # Set the newly calculated Radius as R
        self.s_origin = self.s_coord # Origin of GPS set as current gps position
        self.c_origin = self.spherical_to_cartisian(self.s_origin) # origin in cartesian coord
        # Make a basis
        self.z_o = self.vector_normalize(self.c_origin) # Normal vector to the plane
        self.x_o = self.vector_normalize([1,1,-(self.z_o[0]+self.z_o[1])/self.z_o[2]]) 
        self.y_o = self.vector_normalize(self.cross_prod(self.z_o,self.x_o))
        # Make a transition matrix        
        self.t_mat = self.gen_base_trans_mat(self.x_o, self.y_o, self.z_o) # From local to earth
        self.t_mat = np.linalg.inv(self.t_mat) #from earth to local
        self.o_pressure = self.pressure # set origin pressure
        self.o_temp = self.temp  # Set origin temperature

    def get_long(self):
        return self.phi

    def get_lat(self):
        return self.theta

    def get_height(self):
        return self.calcAltitude()

    def get_X(self):
        return self.Xcord

    def get_Y(self):
        return self.Ycord

    def get_Z(self):
        return self.Zcord


    
    def stop(self): #starts the thread that collects data in the background 
        print ""

def main():
    fig = plt.figure()
    ax1 = fig.gca(projection='3d')
    running = True
    pos = position()
    start = [59.884868776,17.6804052257]
    #pos.set_origin()
    try:
        x = []
        y = []
        z = []
        pos.test("coords.txt",start)
        myfile = open("xyz.txt", "r")
        for line in myfile:
            coord = line.split(" ")
            x.append(float(coord[0]))
            y.append(float(coord[1]))
            z.append(float(coord[2]))
        plot = ax1.plot(x,y,z,label = 'parametric curve')
        plot = ax1.plot([0,100],[0,100],[0,100],label = 'parametric curve')
        plt.show()
    except KeyboardInterrupt, SystemExit:
        running = False
           
if __name__ == '__main__':
    main()
