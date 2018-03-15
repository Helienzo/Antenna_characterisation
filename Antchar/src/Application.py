from src import *
class Application():

    def __init__(self, dsp, data, ax1,fig,endEvent):
        self.pos = position()
        self.dsp = dsp
        self.data = data
        self.ax1 = ax1
        self.fig = fig
        self.plotEvent = threading.Event()
        self.dataEvent = dsp.getDataEvent() # Threading event for new value
        self.recEvent = threading.Event() # Threading event for recoding or not
        self.endEvent = endEvent # Threading event for killing the aplication
        self.pars = parser()
        self.value = [0] # measurment value
        self.rec = s_saver(self.dataEvent,data,self.recEvent)
        # Initialization of curses application
        self.stdscr = curses.initscr()
        self.stdscr.clear()
        self.stdscr.refresh()
        self.stdscr.nodelay(1)
        self.stdscr.keypad(1)
        self.running = True
        #Start the thread
        self.app_thread =threading.Thread(target=self.app)
        self.app_thread.deamon = True
        self.app_thread.start()

    def get_val(self):
        return self.value[0]

    def getPlotEvent(self):
        return self.plotEvent

    def endprocess(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        self.running = False
        self.pars.set_status_false()
        self.pars.empty_queue()
        self.pos.stop()
        gpsp.running = False
        gpsp.join() # wait for the thread to finish what it's doing
        self.pos.stop()
        self.endEvent.set()
        

    def app(self):
         
        k = "" #init k the input character
        info_string = ""
        instruction = "# Write command$ " #17 characters
        tid = 0
         # Controll of main loop

        try:
            
            while (self.running):
                 
                time.sleep(0.1)
                tid = tid+0.1 
                k = self.stdscr.getch()
                self.pars.new_character(k)
                
                #if k == curses.KEY_UP:
                #    recentCommand()
                
                if self.pars.get_do_status(): # If new command is available
                    command_queue = self.pars.get_queue() # Get commands

                    if command_queue[0] == "time":
                        if len(command_queue) > 1:
                            try: 
                                tid = int(command_queue[1])
                            except ValueError:
                                tid = tid
                                info_string = 'undefined value: ' + str(command_queue[1])
                        else:
                            tid = 0  
                        self.pars.set_status_false()
                        self.pars.empty_queue()

                    # Help command
                    elif command_queue[0] == 'help':

                        if len(command_queue) > 1:
                            try: 
                                info_string = help_string(str(command_queue[1]))
                            except SyntaxError:
                                info_string = 'undefined help command: ' + str(command_queue[1])
                        else:
                            info_string = help_string("")  
                        self.pars.set_status_false()
                        self.pars.empty_queue()

                    elif command_queue[0] == 'val':
                        info_string = "Current value: " + str(self.data.getData(4))
                        self.pars.set_status_false()
                        self.pars.empty_queue()       

                    #set the center frequency
                    elif command_queue[0] == 'setcfreq':

                        if len(command_queue) > 1:
                            try: 
                                self.dsp.set_c_freq(double(double(command_queue[1]))*double(1000000)-0.5e6)
                            except ValueError:
                                info_string = 'undefined value: ' + str(command_queue[1])
                        else:
                            info_string = "freq command must have a value input" # Change to helpfunction
                        self.pars.set_status_false()
                        self.pars.empty_queue()

                    #get the frequency
                    elif command_queue[0] == 'getcfreq':
                        info_string = "Current center frequency: " + str(self.dsp.get_c_freq()) + " Hz"
                        self.pars.set_status_false()
                        self.pars.empty_queue()

                    #set the loop
                    elif command_queue[0] == 'setloop':

                        if len(command_queue) > 1:

                            if command_queue[1] == 'auto' and len(command_queue) > 2:

                                try:
                                    self.dsp.set_auto_loop(int(command_queue[2]))
                                except ValueError:
                                    info_string = 'undefined value: ' + str(command_queue[2])

                            else:

                                try:
                                    tmp_loop = int(command_queue[1]) 
                                    self.dsp.set_loop(tmp_loop)
                                except ValueError:
                                    info_string = 'undefined value: ' + str(command_queue[1])

                        else:
                            info_string = "setloop command must have a value input" # Change to helpfunction
                        self.pars.set_status_false()
                        self.pars.empty_queue()

                    elif command_queue[0] == 'origin':
                        self.pos.set_origin()
                        self.pars.set_status_false()
                        self.pars.empty_queue()

                    #record some values and then plot them with gnuplot
                    elif command_queue[0] == 'recordsamples':
                        if self.recEvent.isSet() != True:
                            if len(command_queue) > 2:
                                try: 
                                    self.rec.recThread_samples(str(command_queue[1]),int(command_queue[2]),self.pos)
                                except ValueError:
                                    info_string = 'undefined value: ' + str(command_queue[2])
                            else:
                                info_string = "record command must have a value and name input" # Change to helpfunction
                        else:
                            info_string = "Already recording" 
                        self.pars.set_status_false()
                        self.pars.empty_queue()

                    elif command_queue[0] == 'recordtime':
                        if self.recEvent.isSet() != True:
                            if len(command_queue) > 2:
                                try: 
                                    self.rec.recThread_time(str(command_queue[1]),float(command_queue[2]),self.pos)
                                except ValueError:
                                    info_string = 'undefined value: ' + str(command_queue[2])
                            else:
                                info_string = "record command must have a value and name input" # Change to helpfunction
                        else:
                            info_string = "Already recording" 
                        self.pars.set_status_false()
                        self.pars.empty_queue()
                    
                    elif command_queue[0] == "rec":
                        if self.recEvent.isSet() == True:
                            if len(command_queue) > 1:
                                if command_queue[1] == "start":
                                    self.rec.start()
                                elif command_queue[1] == "stop":
                                    self.rec.stop()
                                elif command_queue[1] == "pause":
                                    self.rec.pause()
                                elif command_queue[1] == "step":
                                    self.rec.step()
                                else:
                                    info_string = "undefined mode command: " + str(command_queue[1])
                            else:
                                info_string = "rec needs either start, stop or pause"
                        else:
                            info_string = "Not recording" 
                        self.pars.set_status_false()
                        self.pars.empty_queue()

                    elif command_queue[0] == "mode":
                        if len(command_queue) > 1:
                            if command_queue[1] == "lock":
                                self.dsp.lock()
                            elif command_queue[1] == "update":
                                self.dsp.update()
                            elif command_queue[1] == "unlock":
                                self.dsp.unlock()
                            else:
                                info_string = 'undefined mode command: ' + str(command_queue[1])
                        else:
                            info_string = "Specify a command" # Change to helpfunction
                        self.pars.set_status_false()
                        self.pars.empty_queue()

                    elif command_queue[0] == "plot":
                        if len(command_queue) > 1:
                            if command_queue[1] == "clear":
                                self.ax1.cla()
                            elif command_queue[1] == "close":
                                plt.close(self.fig)
                            else:
                                try:
                                    self.rec.plotter(str(command_queue[1]),self.ax1)
                                    self.plotEvent.set()
                                except IOError:
                                    info_string = 'undefined filename: ' + str(command_queue[1])
                        else:
                            info_string = "Specify a filename" # Change to helpfunction
                        self.pars.set_status_false()
                        self.pars.empty_queue()

                    #quit the program
                    elif command_queue[0] == "quit":
                        curses.nocbreak()
                        self.stdscr.keypad(False)
                        curses.echo()
                        curses.endwin()
                        self.endprocess()

                    else:
                        info_string = 'undefined command: ' + str(command_queue[0])
                        self.pars.set_status_false()
                        self.pars.empty_queue()
                
                update_screen(self.stdscr,tid,self.pos,self.dsp,self.data,self.pars,info_string,self.recEvent, self.bar)
                info_string = ""
                self.stdscr.refresh()
                
        except (KeyboardInterrupt,SystemExit): #when you press ctrl+c
            curses.nocbreak()
            self.stdscr.keypad(False)
            curses.echo()
            curses.endwin()
            self.endprocess()
        

