from src import *

class radio(gr_antenna):
    value = 0
    freq = 1000
    rec = s_saver()

    def __init__(self,qapp):
        #gr_antenna.__init__(self)
        super(radio,self).__init__()
        self.variable_function_probe_0 = variable_function_probe_0 = 0
        self.blocks_probe_signal_x_0 = blocks.probe_signal_f()

        def _variable_function_probe_0_probe():
            while True:
                val = self.blocks_probe_signal_x_0.level()
                self.value = val
                try:
                    self.set_variable_function_probe_0(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (self.freq))
        
        def app():
            stdscr = curses.initscr()    
            rec = s_saver()
            pos = position()
            #raw_input("press any key")
            # Initialization of curses application
            
            stdscr.clear()
            stdscr.refresh()
            stdscr.nodelay(1)
            stdscr.keypad(1)
            k = "" #init k the input character
            info_string = ""
            instruction = "# Write command$ " #17 characters
            command_history = ["","","","",""]
            tid = 0
            running = True # Controll of main loop
            pars = parser()

            #try:
                
            while (running):
                 
                time.sleep(0.1) 
                stdscr.clear()
                tid = tid+0.1 
                k = stdscr.getch()
                pars.new_character(k)
                
                if pars.get_do_status():
                    command_que = pars.get_que()

                    if command_que[0] == "time":
                        if len(command_que) > 1:
                            try: 
                                tid = int(command_que[1])
                            except ValueError:
                                tid = tid
                                info_string = 'undefined value: ' + str(command_que[1])
                        else:
                            tid = 0  
                        pars.set_status_false()
                        pars.empty_que()

                    elif command_que[0] == 'help':

                        if len(command_que) > 1:
                            try: 
                                info_string = help_string(str(command_que[1]))
                            except SyntaxError:
                                info_string = 'undefined help command: ' + str(command_que[1])
                        else:
                            info_string = help_string("")  
                        pars.set_status_false()
                        pars.empty_que()

                    elif command_que[0] == 'val':
                        info_string = "Current value: " + str(self.get_val())
                        pars.set_status_false()
                        pars.empty_que()       
                    #set the center frequency
                    elif command_que[0] == 'freq':

                        if len(command_que) > 1:
                            try: 
                                self.set_c_freq(double(double(command_que[1]))*double(1000000))
                            except ValueError:
                                info_string = 'undefined value: ' + str(command_que[1])
                        else:
                            info_string = "freq command must have a value input" # Change to helpfunction
                        pars.set_status_false()
                        pars.empty_que()
                    #get the frequency
                    elif command_que[0] == 'get':
                        info_string = "Current center frequency: " + str(self.get_c_freq()) + " Hz"
                        pars.set_status_false()
                        pars.empty_que()

                    elif command_que[0] == 'origin':
                        pos.set_origin()
                        pars.set_status_false()
                        pars.empty_que()

                    elif command_que[0] == 'setvalfreq':

                        if len(command_que) > 1:
                            try: 
                                self.set_val_freq(int(command_que[1]))
                            except ValueError:
                                info_string = 'undefined value: ' + str(command_que[1])
                        else:
                            info_string = "setvalfreq command must have a value input" # Change to helpfunction
                        pars.set_status_false()
                        pars.empty_que()

	                #record some values and then plot them with gnuplot
                    elif command_que[0] == 'record':

                        if len(command_que) > 1:
                            try: 
                                rec.recThread(int(command_que[1]),self,pos)
                            except ValueError:
                                info_string = 'undefined value: ' + str(command_que[1])
                        else:
                            info_string = "record command must have a value input" # Change to helpfunction
                        pars.set_status_false()
                        pars.empty_que()

                    #quit the program
                    elif command_que[0] == "quit":
                        running = False
                        pars.set_status_false()
                        pars.empty_que()
                        stdscr.keypad(0)
                        self.stop()
                        self.wait()
                        pos.stop()
                        gpsp.running = False
                        gpsp.join() # wait for the thread to finish what it's doing
                        pos.stop()
                        stdscr.keypad(0)
                        curses.endwin()
                        qapp.exit()


                    else:
                        pars.set_status_false()
                        pars.empty_que()
                
                update_screen(stdscr,tid,pos,self,pars,info_string)
                info_string = ""
                stdscr.refresh()

                

                    #self.update_screen(pos)
            #except (KeyboardInterrupt,SystemExit): #when you press ctrl+c
             #   print "\nKilling Thread..."
              #  gpsp.running = False
               # gpsp.join() # wait for the thread to finish what it's doing
                #self.stop()
                #self.wait()
                #pos.stop()
                #stdscr.keypad(0)
            #print "Done.\nExiting."

        _variable_function_probe_0_thread = threading.Thread(target=_variable_function_probe_0_probe)
        _variable_function_probe_0_thread.daemon = True
        _variable_function_probe_0_thread.start()
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_probe_signal_x_0, 0))
        app_thread =threading.Thread(target=app)
        app_thread.deamon = True
        app_thread.start()

    def get_val(self):
        return self.value

    def set_val_freq(self, _freq):
        self.freq = _freq
