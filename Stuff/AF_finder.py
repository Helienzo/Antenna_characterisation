import numpy as np
import csv
import math

running = True
noOfColumns = 26*2 + 54*2 + 11*2

freq = []
AFe = []
AFm = []
with open('AF_data.txt','r') as csvfile:
    data = csv.reader(csvfile, delimiter=' ')
    for row in data:
        freq.append(float(row[0]))
        AFe.append(float(row[1]))
        AFm.append(float(row[2]))

def finder(myVal):
    
    if myVal < 0.009  or myVal > 300:
        print("Frequency has to lie in the range 0.009-300 MHz")
        
    else:
        try: #check if input value lies in the list
            myIndex = freq.index(myVal)
            myAFe = AFe[myIndex]
            myAFm = AFm[myIndex]
    
        except ValueError:  #if it doesn't, interpolate to find it.
            for i in range (0,len(freq)-1):
                if myVal > freq[i]  and myVal < freq[i+1]:
                    a = AFe[i]
                    b = AFe[i+1]
                    c = AFm[i]
                    d = AFm[i+1]
                    f = a/(a+b)
                    g = c/(c+d)
                    print(c)
                    print(d)
                    print(g)
                    #myAFe = round(math.pow(b,f)*math.pow(a,(1-f)),2)
                    #myAFm = round(math.pow(c,g)*math.pow(d,(1-g)),2)
                    #myAFm = 1
                    
                    #''' linear interpolation below, working
                    
                    
                    intpVal = ( (myVal-freq[i]) / (freq[i+1] - freq[i]) ) #interpolate
                    myAFe = AFe[i] + intpVal*(AFe[i+1]-AFe[i])
                    myAFm = AFm[i] + intpVal*(AFm[i+1]-AFm[i])
                    #'''
        print("Your Ke is: " + str(myAFe) + " dB/m, and your Kh is " + str(myAFm) + " db/m \n")

while(running):
    inVal = raw_input("Type frequency to find out antenna factor, type quit to quit\n")
    
    try:
        inVal = float(inVal)
    
    except ValueError:
        running = False
        break
    
    finder(inVal)
    
    
