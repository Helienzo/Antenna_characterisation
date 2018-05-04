from src import *
class Application():

    def __init__(self, dsp, data, ax1,fig,endEvent):
        self.currentWindow = "standard"
        self.pos = position()
        self.dsp = dsp
        self.data = data
        self.ax1 = ax1
        self.fig = fig
        self.tid = 0
        self.info_string = ""
        self.plotEvent = threading.Event()
        self.dataEvent = dsp.getDataEvent() # Threading event for new value
        self.recEvent = threading.Event() # Threading event for recoding or not
        self.endEvent = endEvent # Threading event for killing the aplication
        self.pars = parser()
        self.value = [0] # measurment value
        self.rec = s_saver(self.dataEvent,data,self.recEvent)
        self.config = config(self.pos,dsp,self.rec)
        self.centerFrequencyLineNo = 0
        self.vectorRecLineNo = 0
        # Initialization of curses application
        self.stdscr = curses.initscr()
        self.stdscr.clear()
        self.stdscr.refresh()
        self.stdscr.nodelay(1)
        self.stdscr.keypad(1)
        self.running = True
        self.Calibration = Calibration(self.data,self.rec,self.pos)

        self.window = window(self.stdscr,self.pos,self.dsp,self.data,
                            self.pars,self.recEvent,self.rec,self)

        #Start the thread
        self.app_thread =threading.Thread(target=self.app)
        self.app_thread.deamon = True
        self.app_thread.start()
        self.updateFile()

    def get_val(self):
        return self.value[0]

    def getPlotEvent(self):
        return self.plotEvent

    def getInfoString(self):
        return self.info_string

    def getTime(self):
        return self.tid

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

        try:
            while (self.running):
                time.sleep(0.1)
                self.tid += 0.1
                k = self.stdscr.getch()
                self.pars.new_character(k)

                #if k == curses.KEY_UP:
                #    recentCommand()

                if self.pars.get_do_status(): # If new command is available
                    if self.currentWindow == "standard":
                        self.standardApp()
                    elif self.currentWindow == "setup":
                        self.setupApp()

                self.window.update(self.currentWindow)
                self.info_string = ""
                self.stdscr.refresh()

        except (KeyboardInterrupt,SystemExit): #when you press ctrl+c
            curses.nocbreak()
            self.stdscr.keypad(False)
            curses.echo()
            curses.endwin()
            self.endprocess()

    def standardApp(self):
        command_queue = self.pars.get_queue() # Get commands

        if command_queue[0] == "time":
            if len(command_queue) > 1:
                try:
                    self.tid = int(command_queue[1])
                except ValueError:
                    self.tid = self.tid
                    self.info_string = 'undefined value: ' + str(command_queue[1])
            else:
                self.tid = 0

            self.pars.set_status_false()
            self.pars.empty_queue()

        elif command_queue[0] == 'help':
            if len(command_queue) > 1:
                try:
                    self.info_string = self.window.help_string(str(command_queue[1]))
                except SyntaxError:
                    self.info_string = 'undefined help command: ' + str(command_queue[1])
            else:
                self.info_string = self.window.help_string("")

            self.pars.set_status_false()
            self.pars.empty_queue()

        elif command_queue[0] == 'val':
            self.info_string = "Current value: " + str(self.data.getData(4))
            self.pars.set_status_false()
            self.pars.empty_queue()

        elif command_queue[0] == 'setcfreq':

            if len(command_queue) > 1:
                try:
                    self.config.setCenterFreq(float(command_queue[1]))
                except ValueError:
                    self.info_string = 'undefined value: ' + str(command_queue[1])
            else:
                self.info_string = "freq command must have a value input" # Change to helpfunction

            self.pars.set_status_false()
            self.pars.empty_queue()

        elif command_queue[0] == 'getcfreq':
            self.info_string = "Current center frequency: " + str(self.dsp.get_c_freq()) + " Hz"
            self.pars.set_status_false()
            self.pars.empty_queue()

        elif command_queue[0] == 'setloop':
            if len(command_queue) > 1:
                try:
                    if command_queue[1] == 'auto':

                        self.config.setLoopAuto()

                    elif int(command_queue[1]) in [0,1,2,3]: #checks that the user chooses an existing loop

                        self.config.setLoop(int(command_queue[1]))
                    else:
                        self.info_string = 'must choose auto or specific loop: ' + str(command_queue[1])
                except ValueError:
                    self.info_string = 'Undefined parameter: ' + str(command_queue[1])
            else:
                self.info_string = 'must choose auto or specific loop'

            self.pars.set_status_false()
            self.pars.empty_queue()

        elif command_queue[0] == 'origin':
            self.config.setOrigin()
            self.pars.set_status_false()
            self.pars.empty_queue()

        elif command_queue[0] == 'record':
            if self.recEvent.isSet() != True:
                if len(command_queue) > 1:
                    try:
                        self.rec.recThread(str(command_queue[1]),self.pos)
                    except ValueError:
                        self.info_string = 'undefined value: ' + str(command_queue[1])
                else:
                    self.info_string = "record command must have a name input" # Change to helpfunction
            else:
                self.info_string = "Already recording"
            self.pars.set_status_false()
            self.pars.empty_queue() #record some values and then plot them with gnuplot

        elif command_queue[0] == 'recordsamples':
            if self.recEvent.isSet() != True:
                if len(command_queue) > 2:
                    try:
                        self.rec.recThread_samples(str(command_queue[1]),int(command_queue[2]),self.pos)
                    except ValueError:
                        self.info_string = 'undefined value: ' + str(command_queue[2])
                else:
                    self.info_string = "record command must have a value and name input" # Change to helpfunction
            else:
                self.info_string = "Already recording"
            self.pars.set_status_false()
            self.pars.empty_queue()

        elif command_queue[0] == 'calibration':
            if self.recEvent.isSet() != True:
                try:
                    self.Calibration.calibrationThread()
                except IOError:
                    self.info_string = "Calibration or recording in progress"
            else:
                self.info_string = "Cannot calibrate while calibrating or recording"
            self.pars.set_status_false()
            self.pars.empty_queue()

        elif command_queue[0] == 'recordtime':
            if self.recEvent.isSet() != True:
                if len(command_queue) > 2:
                    try:
                        self.rec.recThread_time(str(command_queue[1]),float(command_queue[2]),self.pos)
                    except ValueError:
                        self.info_string = 'undefined value: ' + str(command_queue[2])
                else:
                    self.info_string = "record command must have a value and name input" # Change to helpfunction
            else:
                self.info_string = "Already recording"
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
                    elif command_queue[1] == "step3":
                        self.rec.step3()
                    else:
                        self.info_string = "undefined mode command: " + str(command_queue[1])
                else:
                    self.info_string = "rec needs either start, stop or pause"
            else:
                self.info_string = "Not recording"
            self.pars.set_status_false()
            self.pars.empty_queue()

        elif command_queue[0] == "mode":
            if len(command_queue) > 1:
                if command_queue[1] == "lock":
                    if len(command_queue)>2:
                        try:
                            self.config.setLock(ast.literal_eval(command_queue[2]))
                        except(ValueError,SyntaxError):
                            self.info_string = "lock must be True or False " + "(note capitalization)"
                    else:
                        self.info_string = "lock must be True or False " + "(note capitalization)"
                elif command_queue[1] == "update":
                    self.dsp.update()
                elif command_queue[1] == "vecsave":
                    if len(command_queue)>2:
                        try:
                            self.config.vectorSaveMode(ast.literal_eval(command_queue[2]))
                        except(ValueError,SyntaxError):
                            self.info_string("Argument must be True or False " +
                                             "(note capitalization)")
                    else:
                        self.info_string = "lock must be True or False " + "(note capitalization)"
                elif command_queue[1] == "delay":
                    if len(command_queue) > 2:
                        try:
                            self.config.setDelay(float(command_queue[2]))
                        except ValueError:
                            self.info_string = 'undefined value: ' + str(command_queue[2])
                    else:
                        self.info_string = 'delay must have a value'
                else:
                    self.info_string = 'undefined mode command: ' + str(command_queue[1])
            else:
                self.info_string = "Specify a command" # Change to helpfunction
            self.pars.set_status_false()
            self.pars.empty_queue()

        elif command_queue[0] == "plot":
            if len(command_queue) > 1:
                if command_queue[1] == "clear":
                    self.ax1.cla()
                elif command_queue[1] == "close":
                    plt.close(self.fig)
                elif command_queue[1] == "vec":
                    try:
                        self.rec.plottvec(str(command_queue[2]),str(command_queue[3]),self.ax1)
                        self.plotEvent.set()
                    except IOError:
                        self.info_string = 'undefined filename: ' + str(command_queue[1])
                else:
                    try:
                        self.rec.plotter(str(command_queue[1]),self.ax1)
                        self.plotEvent.set()
                    except IOError:
                        self.info_string = 'undefined filename: ' + str(command_queue[1])
            else:
                self.info_string = "Specify a filename" # Change to helpfunction
            self.pars.set_status_false()
            self.pars.empty_queue()

        elif command_queue[0] == "setup":
            self.currentWindow = "setup"
            self.pars.set_status_false()
            self.pars.empty_queue()

        elif command_queue[0] == "quit":
            curses.nocbreak()
            self.stdscr.keypad(False)
            curses.echo()
            curses.endwin()
            self.endprocess()

        else:
            self.info_string = 'undefined command: ' + str(command_queue[0])
            self.pars.set_status_false()
            self.pars.empty_queue()

    def setupApp(self):
         # Controll of main loop
        command_queue = self.pars.get_queue() # Get commands
        question = self.pars.get_question()

        #handles if user has been asked y or n question for example when saving files
        if question:
            if command_queue[0] == 'y' or command_queue[0] == 'Y' or  command_queue[0] == 'yes':
                string_list = self.pars.get_command_history()
                string_list = string_list[len(string_list)-2].split(" ")
                self.config.save(string_list[1])

            elif command_queue[0] == 'n' or command_queue[0] == 'N' or  command_queue[0] == 'no':
                self.info_string = 'Did not overwrite.'

            else:
                self.info_string = 'Did not answer yes or no. Question terminated'
            self.pars.set_question(False)
            self.pars.empty_queue()
            self.pars.set_status_false()


        elif command_queue[0] == "set":

            if len(command_queue) > 1:

                if command_queue[1] == "origin": #set gps origin manually
                    self.config.setOrigin()
                elif len(command_queue) > 2:
                    try:

                        if command_queue[1] == "centerfrequency":

                            self.config.setCenterFreq(float(command_queue[2]))

                        elif command_queue[1] == "vectorrec":
                            self.config.vectorSaveMode(ast.literal_eval(command_queue[2]))

                        elif command_queue[1] == "delay": #set delay in the loop
                            self.config.setDelay(float(command_queue[2]))

                        elif command_queue[1] == "loop": #set auto loop switching or set specific loop
                            if len(command_queue) > 2:
                                if command_queue[2] == 'auto':

                                        self.config.setLoopAuto()

                                elif int(command_queue[2]) in [0,1,2,3]: #checks that the user chooses an existing loop
                                    self.config.setLoop(int(command_queue[2]))

                                else:
                                    self.info_string = 'must choose auto or specific loop'
                            else:
                                self.info_string = 'must choose auto or specific loop'

                        elif command_queue[1] == "lock": #set to lock the dsp chain or not
                            self.config.setLock(ast.literal_eval(command_queue[2]))

                        elif command_queue[1] == "cutoff": #set cutoff frequency (in Hz)
                            self.config.setCutOff(int(command_queue[2]))

                        elif command_queue[1] == "decimation": #set decimation in the lowpass filter in gnuradio
                            self.config.setDecimation(int(command_queue[2]))

                        elif command_queue[1] == "transition": #set transition width in dsp chain.
                            self.config.setTransition(float(command_queue[2]))

                    except(ValueError,SyntaxError):
                        self.info_string = 'Undefined parameter: ' + str(command_queue[2])
                else:
                    self.info_string = 'Not enough input parameters: set $parameter $value '
            else:
                self.info_string = 'Not enough input parameters: set $parameter $value '
            self.pars.set_status_false()
            self.pars.empty_queue()

        elif command_queue[0] == "save":
            if len(command_queue) > 1:
                if self.config.fileCheck(command_queue[1]): #Check if a file already exists with same name
                    self.info_string = 'File already exists. Do you want to overwrite it? [y/n]'
                    self.pars.set_question(True)

                else:
                    self.config.save(command_queue[1])

            else:
                self.info_string = 'Must write filename'
            self.pars.set_status_false()
            self.pars.empty_queue()

        elif command_queue[0] == "load":
            try:
                self.config.load(str(command_queue[1]))
            except IOError:
                self.info_string = 'That file does not exist. Try again.'
            self.pars.set_status_false()
            self.pars.empty_queue()
        #quit the program
        elif command_queue[0] == "close":
            self.currentWindow = "standard"
            self.pars.set_status_false()
            self.pars.empty_queue()

        elif command_queue[0] == "quit":
            curses.nocbreak()
            self.stdscr.keypad(False)
            curses.echo()
            curses.endwin()
            self.endprocess()

        else:
            self.info_string = 'undefined command: ' + str(command_queue[0])
            self.pars.set_status_false()
            self.pars.empty_queue()

    def setup_size(self):
        with open("setup.txt") as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    def updateFile(self):
            try:
                self.config.load("default.txt")
            except IOError:
                self.info_string = 'default.txt setup file does not exist'
