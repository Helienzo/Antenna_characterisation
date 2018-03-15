import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
import numpy as np
fig = plt.figure(1) # Plot figure
ax1 = fig.gca() # Plot data
x = []
y = []
z = []
R = []
val = []
i = 0
myfile = open(str("ute12.txt"), "r")
for line in myfile:
    i += 1
    if i > 2:
        coord = line.split(" ")
        val.append(float(coord[4]))#/(float(coord[7])**2+float(coord[8])**2))
        x.append(float(coord[7]))
        y.append(float(coord[8]))
        z.append(float(coord[9]))
        R.append(np.sqrt(float(coord[7])**2+float(coord[8])**2))

#plot = ax1.plot(R)
#plot = ax1.plot(x,y)
plot = ax1.plot(val)
plt.show()
#plot = ax1.plot([0,100],[0,100],[0,100],label = 'parametric curve')
