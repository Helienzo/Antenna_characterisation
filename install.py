import os
import time

home_path = os.path.expanduser("~")

os.system("sudo apt-get install git")
os.system("sudo apt-get install libusb-1.0-0-dev pkg-config")
os.system("sudo apt-get install python2.7 python-pip python-dev python-setuptools swig")

# wiringPi
if os.path.exists(home_path + "/wiringPi/"):
    print "WiringPi exists"
else:
    print "Downloading and installing wiringPi"
    time.sleep(1)
    os.system("git clone http://github.com/hardkernel/wiringPi")
    os.system("cd " + home_path + "/wiringPi/; sudo ./build")

# wiringPi2-python
if os.path.exists(home_path + "/WiringPi2-Python/"):
    print "WiringPi2-python exists"
else:
    print "Downloading and installing WiringPi2-python"
    time.sleep(1)
    os.system("git clone http://github.com/hardkernel/WiringPi2-Python.git")
    os.system("cd " + home_path + "/WiringPi2-Python/; git submodule init; git submodule update; ./build.sh")

#Pressuresensor
if os.path.exists(home_path + "/Adafruit_Python_BME280/"):
    print "BME280 is installed"
else:
    print "Downloading and installing adafruit BME280"
    time.sleep(1)
    os.system("git clone http://github.com/adafruit/Adafruit_Python_GPIO.git")
    os.system("cd " + home_path + "/Adafruit_Python_GPIO/; sudo python setup.py install")
    os.system("git clone http://adafruit/Adafruit_Python_BME280.git")
    os.system("cd " + home_path + "/Adafruit_Python_BME280/; sudo python setup.py install")

os.system("cd " +home_path+"/Antenna_characterisation/; pip install -r requirements.txt")
os.system("sudo apt-get install cmake swig doxygen gnuradio gpsd")



if os.path.exists(home_path + "/airspyone_host-master/"):
    print "Airspy is installed"
else:
    print "Downloading and installing libairspy"
    time.sleep(1)
    os.system("cd "+ home_path + """; wget https://github.com/airspy/airspyone_host/archive/master.zip;
     unzip master.zip;
     cd airspyone_host-master; mkdir build; cd build;
     cmake ../ -DINSTALL_UDEV_RULES=ON;
     make;
     sudo make install;
     sudo ldconfig""")


if os.path.exists(home_path + "/gr-osmosdr/"):
    print "Osmosdr exist"
    os.system("cd " + home_path + "/gr-osmosdr/; cd build; cmake ../; make; sudo make install; sudo ldconfig")
else:
    print "Downloading and installing osmosdr"
    time.sleep(1)
    os.system("git clone git://git.osmocom.org/gr-osmosdr")
    os.system("cd " + home_path + "/gr-osmosdr/; mkdrir build; cd build; cmake ../; make; sudo make install; sudo ldconfig")

# The custom antchar package
os.system("cd ~/Antenna_characterisation/gr-antchar; mkdir build; cd build; cmake ../; make; sudo make install; sudo ldconfig")
