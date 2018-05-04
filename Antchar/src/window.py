from src import *

class window():
    def __init__(self,stdscr,pos,dsp,data,pars,recEvent,rec,app):
        self._stdscr = stdscr
        self._pos = pos
        self._dsp = dsp
        self._rec = rec
        self._data = data
        self._pars = pars
        self._app = app
        self._recEvent = recEvent
        self._centerFrequency = 0
        self._vectorRec = 0




    def update(self,currentWindow):
        if currentWindow == "standard":
            self.update_screen_functions()

        elif currentWindow == "setup":
            self.update_screen_setup()


    def update_screen_functions(self):
        self._stdscr.clear()
        height, width = self._stdscr.getmaxyx()
        record_string = ""
        if self._recEvent.isSet():
            record_string = "Recording"
        else:
            record_string = "Not active"

        # Application main info screen 12 rows ------------------------------------------
        win  = "***  Antenna characteriastion aplication   ***\n"
        #win += "***  Temperature in box:     " + "{0:.3}".format(float(self._pos.getTemperature())) + "            ***\n"
        win += "***  Running time:           " + str(self._app.getTime())+ "            ***\n"
        win += "***  current signal strengt: " + "{0:.3}".format(float(self._data.getData(2))) + "        *** \n"
        win += "***  current SNR :           " + "{0:.3}".format(float.self_data.getData(2)-calibrate.getNoiseFloor()) + "  ** \n"
        win += "***  current ceter freq:     " + "{0:.7}".format(float(self._dsp.get_c_freq())) + "      **\n"
        win += "***  current position X :    " + "{0:.5}".format(float(self._pos.get_X()))  + " **\n"
        win += "***  current position Y :    " + "{0:.5}".format(float(self._pos.get_Y()))  + " **\n"
        win += "***  current position Z :    " + "{0:.5}".format(float(self._pos.get_Z()))  + " **\n"
        win += "***  Recording status : "+ record_string + ", Currentloop: "+ str(self._data.getData(3)) +" **\n"
        win += "***  avilable commands: setcfreq, getcfreq, val, quit, origin  ***\n"
        win += "***  recordtime, recordsamples, plot                           ***\n"
        win += "******************************************************************\n"
        win += "\n"
        win += "------------------------------------------------------------------\n"
        self._stdscr.addstr(0,0,win)
        # -------------------------------------------------------------------------------

        # Command history and info screen
        avil_rows = height - 14 - 1 # 14 rows occupied by information at top of string

        command_history = self._pars.get_history()
        list_length = len(command_history)
        info_string = self._app.getInfoString()
        str_length = len(info_string)
        str_length = int(math.ceil(double(str_length)/width)) # Number of rows in infostring
        if str_length > 0:
            self._pars.add_history(info_string.split('\n'))
        if list_length > 0:
            i = 0
            if avil_rows > list_length:
                i = list_length-1
            else:
                i = avil_rows
            while i > -1:
                i = i-1
                tmp_str = command_history[list_length-2-i]
                str_length = len(tmp_str)
                str_length = int(math.ceil(double(str_length)/width))
                if str_length > 1:
                    i = i - str_length+1
                self._stdscr.addstr(height-2-str_length-i, 0,str(tmp_str))
        self._stdscr.addstr(height-1, 0,"# Write command$ "+self._pars.get_full_string()) # Command input

    def help_string(self,help_command):
        if(help_command == ""):
            win =  "Use help $command to get more information about $command \n"
            win += "Available commands:                                     \n"
            win += "setloop, origin, rec, recordsamples, recordtime, quit,  \n"
            win += "plot, quit, mode, setup.                                \n"

        elif(help_command == "setloop"):
            win = "setloop n sets loop 0,1,2,3 in the antenna               \n"
            win += "setloop auto makes the antenna switch between loops 1-3 \n"
            win += "continously. Loop 0 is reset mode when no loop is active \n"

        elif(help_command == "origin"):
            win = "sets the current GPS coordinates to the origin in the    \n"
            win += "reference frame.                                        \n"

        elif(help_command == "rec"):
            win = "starts a continous recording of samples to the chosen file.\n"
            win += "The command must be on the form: record $filename.       \n"
            win += "When this recording is running, it is possible to use   \n"
            win += "pause, stop, start command to control the flow of the   \n"
            win += "recording. When the recording is paused, use command step \n"
            win += "to record only one samples from the current antenna     \n"
            win += "Use command step to step through all 3 loops of the antenna.\n"

        elif(help_command == "quit"):
            win = "quit: exits the current session and closes the           \n"
            win += "terminal window                                         \n"

        elif(help_command == "plot"):
            win = "plot $filename.txt plots the recorded file with name     \n"
            win +="$filename.txt                                            \n"

        elif(help_command == "recordsamples"):
            win += "recordsamples $filename.txt $number, records $number of \n"
            win += "measurements with filename $filename.txt                \n"

        elif(help_command == "recordtime"):
            win += "recordtime $filename.txt $time, records the specified   \n"
            win += "time $time in minutes with filename $filename.txt       \n"

        elif(help_command == "val"):
            win =   "returns the signal strength that the SDR-dongle is     \n"
            win +=  "measuring in dBm                                       \n"

        elif(help_command == "setcfreq"):
            win =   "Changes the center frequency for the SDR-dongle         \n"

        elif(help_command == "getcfreq"):
            win =   "returns the current center frequency for the SDR-dongle \n"

        elif(help_command == "setloop"):
            win =   "Can either be auto (setloop auto) or a specific         \n"
            win +=  "loop (e.g. setloop 1 for loop 1. There is no way to     \n"
            win +=  "turn off auto at the moment other than just choosing a  \n"
            win +=  "specific loop.                                          \n"

        elif(help_command == "calibration"):
            win = "Should only be used without real measurement signal.      \n"
            win += "Records 100 samples and finds the top value and sets    \n"
            win += "the noise floor to that value                           \n"

        elif(help_command == "setup"):
            win = "Opens the setup menu where all parameters are listed. \n"
            win += "It is also possible to load an existing setup file  \n"
            win += "from the setup menu."

        elif(help_command) == "mode":
            win = "mode $mode_variant                                   \n"
            win += "There are 4 mode variants. They are not mutually exclusive \n"
            win += "The variants are: lock True/False; update; vecsave True/False \n"
            win += "and delay $value                                    \n"
            win += "Lock is used to lock or unlock the DSP process          \n"
            win += "Update manually updates the DSP process if it is locked \n"
            win += "Vecsave either saves or doesn't save the FFT vector     \n"
            win += "Delay sets a delay between the DSP loops when it is running \n"
            win += "automatically.                                          \n"

        elif(help_command) == "plot":
            win += "It is possible to plot or clear a current plot with this \n"
            win += "command.                                                \n"
            win += "plot clear - Clears the current plot window             \n"
            win += "plot close - Closes the current plot window             \n"
            win += "plot vec $filename - plots the FFT vector from $file    \n"
            win += "plot $filename -    plots the measurement values from $file \n"
        else:
            raise SyntaxError
        return win

    def update_screen_setup(self):
        self._stdscr.clear()
        height, width = self._stdscr.getmaxyx()
        record_string = ""

        # Application main info screen 12 rows ------------------------------------------
        win  = "***  Setup file   ***\n"
        win += "***  Center frequency: " + str(float(self._dsp.get_c_freq())/float(1e6)) + "            ***\n"
        win += "***  loopMode        : " + str(self._dsp.getLoopMode())    + " \n"
        win += "***  loopNr          : " + str(self._dsp.getLoop())        + " \n"
        win += "***  Lock            : " + str(self._dsp.getLockMode())    + " \n"
        win += "***  system delay    : " + str(self._dsp.getDelay())       + " \n"
        win += "***  VecMode         : " + str(self._rec.getVecMode())     + " \n"
        win += "***  Gps origin      : " + str(self._pos.getSorigin())     + " \n"
        win += "***  Air pressure    : " + str(self._pos.getOpressure())   + " \n"
        win += "***  Air temperature : " + str(self._pos.getOtemp())       + " \n"
        win += "***  FIR decimation  : " + str(self._dsp.getDecimation())  + " \n"
        win += "***  FIR Cutoff      : " + str(self._dsp.getCutoff())      + " \n"
        win += "***  FIR transition  : " + str(self._dsp.getTransition())  + " \n"
        win += "***  To change a value write: set $parameter $value   ***\n"
        win += "------------------------------------------------------------------\n"
        self._stdscr.addstr(0,0,win)
        # -------------------------------------------------------------------------------

        # Command history and info screen
        avil_rows = height - 17 - 1 # 14 rows occupied by information at top of string

        command_history = self._pars.get_history()
        list_length = len(command_history)
        info_string = self._app.getInfoString()
        str_length = len(info_string)
        str_length = int(math.ceil(double(str_length)/width)) # Number of rows in infostring
        if str_length > 0:
            self._pars.add_history(info_string.split('\n'))
        if list_length > 0:
            i = 0
            if avil_rows > list_length:
                i = list_length-1
            else:
                i = avil_rows
            while i > -1:
                i = i-1
                tmp_str = command_history[list_length-2-i]
                str_length = len(tmp_str)
                str_length = int(math.ceil(double(str_length)/width))
                if str_length > 1:
                    i = i - str_length+1
                self._stdscr.addstr(height-2-str_length-i, 0,str(tmp_str))
        self._stdscr.addstr(height-1, 0,"# Write command$ "+self._pars.get_full_string()) # Command input
