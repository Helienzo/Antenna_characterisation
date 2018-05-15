import numpy as np
import math
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
import csv




fig = plt.figure(1) # Plot figure
ax1 = fig.gca() # Plot data

filename = "test_vec_RAWvector.txt"

I_in = []
Q_in = []

myfile = open(str(filename),"r")

for i in range(0,6):
    line = myfile.readline()

data = line.split(" ,")

for i in range(0,len(data)):
    #print data[i]
    if i%2 == 1:
        I_in.append(float(data[i]))
    else:
        Q_in.append(float(data[i]))

plot = ax1.plot(I_in)
plt.show()
