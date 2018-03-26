import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
import numpy as np

fig = plt.figure(1) # Plot figure
ax1 = fig.gca() # Plot data

x = []
y = []
z = []
R = []
ang = []
val = []
val_loop1 = []
val_loop2 = []
val_loop3 = []
ang_loop1 = []
ang_loop2 = []
ang_loop3 = []
loopnr = 0
i = 0
#Referens 11 12

myfile = open(str("ute6.txt"), "r")
"""
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
"""
for line in myfile:
    i += 1
    if i > 2 and i < 500:
        coord = line.split(" ")
         
        x_tmp = float(coord[7])
        y_tmp = float(coord[8])
        z_tmp = float(coord[9])
        
        z.append(z_tmp)
        #calculate angle
        ang_tmp = np.arctan2(y_tmp,x_tmp)
        
        r = x_tmp**2 + y_tmp**2
        
        val_tmp_abs = r*10**(float(coord[4])/10)/1000.0
        val_tmp =float(coord[5])
        
        if int(coord[6]) == 1:
            val_loop1.append(val_tmp_abs)
            ang_loop1.append(ang_tmp)
        
        elif int(coord[6]) == 2:
            val_loop2.append(val_tmp_abs)
            ang_loop2.append(ang_tmp)
            
        elif int(coord[6]) == 3:
            val_loop3.append(val_tmp_abs)
            ang_loop3.append(ang_tmp)
        
        #val.append(val_tmp_abs)#/(float(coord[7])**2+float(coord[8])**2))
        x.append(x_tmp)
        y.append(y_tmp)
        
        val_tmp_abs = r*10**(float(coord[5])/10)/1000.0
        val.append(val_tmp_abs)
        ang.append(ang_tmp)
        
        R.append(np.sqrt(float(coord[7])**2+float(coord[8])**2))


#plot = ax1.plot(x,y)
#fig = plt.figure(2) # Plot figure
#ax2 = fig.gca() # Plot data
#plot = ax2.plot(y)

#plot = ax1.plot(R)
#plot = ax1.plot(val)p
ax = plt.subplot(111, projection='polar')
#max_val = np.max(val)
max_val_vec = [np.max(np.abs(val_loop1)), np.max(np.abs(val_loop2)), np.max(np.abs(val_loop3))]
max_val = np.max(max_val_vec)
#plot = ax.plot(ang,( val/max_val ))
ax.grid(True)
#ax1.plot(val_loop1)
'''
plot = ax.plot(np.rad2deg(ang_loop1),np.abs(val_loop1))
plot = ax.plot(np.rad2deg(ang_loop2),np.abs(val_loop2))
plot = ax.plot(np.rad2deg(ang_loop3),np.abs(val_loop3))
'''


plot1 = ax.plot(ang_loop1,np.abs(val_loop1)/max_val,'r', label = 'Loop 1')
plot2 = ax.plot(ang_loop2,np.abs(val_loop2)/max_val,'b', label = 'Loop 2')
plot3 = ax.plot(ang_loop3,np.abs(val_loop3)/max_val,'g', label = 'Loop 3')
plot4 = ax.plot(ang, np.abs(val/max_val), 'k', label = 'Sum of all loops')
plt.legend(handles=[plot1, plot2,plot3,plot4])
plt.show()
#plot = ax1.plot([0,100],[0,100],[0,100],label = 'parametric curve')
