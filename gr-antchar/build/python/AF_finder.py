import numpy as np
import csv
import math
import os
freq = []
AFe = []
AFm = []
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'AF_data.txt')
with open(filename,'r') as csvfile:
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
                    #myAFe = round(math.pow(b,f)*math.pow(a,(1-f)),2)
                    #myAFm = round(math.pow(c,g)*math.pow(d,(1-g)),2)
                    #myAFm = 1
                    
                    #''' linear interpolation below, working
                    
                    
                    intpVal = ( (myVal-freq[i]) / (freq[i+1] - freq[i]) ) #interpolate
                    myAFe = AFe[i] + intpVal*(AFe[i+1]-AFe[i])
                    myAFm = AFm[i] + intpVal*(AFm[i+1]-AFm[i])
        return myAFe, myAFm
    
    
