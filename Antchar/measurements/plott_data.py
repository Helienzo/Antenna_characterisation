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
ang = []
i = 0
#Referens 11 12
myfile = open(str("ute2.txt"), "r")
myfilevec = open(str("ute6_vector.txt"), "r")
for line in myfilevec:
    i += 1
    if i > 200 and i < 203:
        coord = line.split(" ")

        vec = [None]*len(coord)
        for ind in range(0,len(coord)-1):
            vec[ind] = float(coord[ind])
plot = ax1.plot(vec)
i=0   

for line in myfile:
    i += 1
    if i > 2 and i < 500:
        coord = line.split(" ")
         
        x_tmp = float(coord[7])
        y_tmp = float(coord[8])
        z_tmp = float(coord[9])
        r = x_tmp**2 + y_tmp**2
        val_tmp_abs = (r)*10**(float(coord[5])/10)/1000.0
        val_tmp =float(coord[5])
        #if float(coord[6]) == 3:
        val.append(val_tmp_abs)#/(float(coord[7])**2+float(coord[8])**2))

        z.append(z_tmp)
        #calculate angle
        ang_tmp = np.arctan2(y_tmp,x_tmp)
        ang.append(ang_tmp)
        pol_x = val_tmp*np.cos(ang_tmp)
        pol_y = val_tmp*np.sin(ang_tmp)
        x.append(x_tmp)
        y.append(y_tmp)

        
        R.append(np.sqrt(float(coord[7])**2+float(coord[8])**2))


#plot = ax1.plot(x,y)
#fig = plt.figure(2) # Plot figure
#ax2 = fig.gca() # Plot data
#plot = ax2.plot(y)

#plot = ax1.plot(R)
plot = ax1.plot(val)
fig = plt.figure(2)
ax = plt.subplot(111, projection='polar')
max_val = np.max(val)
plot = ax.plot(ang,( val/max_val ))
ax.grid(True)

#plot = ax1.plot(np.rad2deg(ang))
#plot = ax1.plot(val)
plt.show()
#plot = ax1.plot([0,100],[0,100],[0,100],label = 'parametric curve')
