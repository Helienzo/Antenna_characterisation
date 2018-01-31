from src import *

class s_saver():

    def record(self,noOfSamples,my,pos):     #collects and plots signal strength data from the SDR-dongle
    	val = 0
        #----------PLOTTING SETTINGS---------------#
        g = Gnuplot.Gnuplot(debug = 0)
        g.title('My Systems Plot')
        g.xlabel('x')
        g.ylabel('Value(dB)')
        g('set term png')
        g('set out "output.png"')
        myFile = open("measurements.txt", "w")
        #------------------------------------------#
        
        #----------RECORDING LOOP--------------------#
        for x in range(0, noOfSamples):
            val = my.get_val() #collect the measurement data
            X = pos.get_X()
            Y = pos.get_Y()
            Z = pos.get_Z()
            myFile.write("{0} {1} {2} {3} {4}\n".format(x, val, X, Y, Z))    #write the data to file
            time.sleep(0.01)                            #sleeps for a while so that the SDR has time to change value.
        myFile.close()                                  #close and save the file
        #-----------------------------------------__#
        
        #------------PLOTTING------------------------#
        databuff = Gnuplot.File("measurements.txt", using='2:1',with_='line', title="Signal strength")
        g.plot(databuff)
        #--------------------------------------------#
        
        #print ("Recording is done") #optional output
    
  
    def recThread(self,noOfSamples,my,pos): #starts the thread that collects data in the background 
        thread = threading.Thread(target=self.record, args = (noOfSamples,my,pos,)) #creates threading object with function record()
        thread.daemon = True                                            #make sure that if we cancel main thread this thread cancels too
        thread.start()    

