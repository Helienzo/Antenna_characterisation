import wiringpi2 as wpi
import time

wpi.wiringPiSetup()
wpi.pinMode(2,1)
wpi.pinMode(0,1)
flag = False
mode = 1

while flag != True:
    mode = input("Loop 1, 2 or 3? 0 to quit \n")    
    integ = 1
    
    if mode == 1:
        wpi.digitalWrite(0,1)
        wpi.digitalWrite(2,0)
        #time.sleep(10)
        raw_input("press enter to continue")
    
    elif mode == 2:
        wpi.digitalWrite(0,1)
        wpi.digitalWrite(2,1)
        #time.sleep(10)
        raw_input("press enter to continue")
    
    elif mode == 3:
        wpi.digitalWrite(0,0)
        wpi.digitalWrite(2,1)
        #time.sleep(10)
        raw_input("press enter to continue")
    
    elif mode == 4:
        wpi.digitalWrite(0,0)
        wpi.digitalWrite(2,0)
        #time.sleep(10)
        raw_input("press enter to continue")
        
    elif mode == 0:
        flag = True
    
    else:
        print("Try again")
