from src import *

class window():
    def __init__(self,stdscr,pos,dsp,data,pars,recEvent,app):
        self._stdscr = stdscr
        self._pos = pos
        self._dsp = dsp
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
        win += "***  Temperature in box:     " + "{0:.3}".format(float(self._pos.getTemperature())) + "            ***\n"
        win += "***  Running time:           " + str(self._app.getTime())+ "            ***\n"
        win += "***  current signal strengt: " + "{0:.3}".format(float(self._data.getData(2))) + "        *** \n"
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
            win =  "These are the available commands:                       \n"
            win += "                                                        \n"
            win += "#command:           explanation:                        \n"
            win += "--------------------------------------------------------\n"
            win += "#recordsamples - $filename.txt $number, records $number of\n"
            win += "measurements with filename $filename.txt                \n"
            win += "#recordtime - $filename.txt $time, records the specified  \n"
            win += "time $time in minutes with filename $filename.txt       \n"
            win += " into measurement.txt                                   \n"
            win += "#setcfreq - Changes the current center frequency        \n"
            win += "#getcfreq - Get the current center frequency            \n"
            win += "#val - returns the current SDR value (in dBmW/m2)       \n"
            win += "#quit - Exits the current session                       \n"

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

        elif(help_command == "origin"):
            win =   "sets the current GPS-coordinates as origin in the local \n"
            win +=  "coordinate system                                       \n"

        elif(help_command == "val"):
            win =   "returns the signal strength that the SDR-dongle is     \n"
            win +=  "measuring in dBm                                       \n"

        elif(help_command == "val"):
            win =   "returns the signal strength that the SDR-dongle is     \n"
            win +=  "measuring in dBm                                       \n"

        elif(help_command == "val"):
            win =   "returns the signal strength that the SDR-dongle is     \n"
            win +=  "measuring in dBm                                       \n"

        elif(help_command == "val"):
            win =   "returns the signal strength that the SDR-dongle is     \n"
            win +=  "measuring in dBm                                       \n"

        elif(help_command == "val"):
            win =   "returns the signal strength that the SDR-dongle is     \n"
            win +=  "measuring in dBm                                       \n"
        else:
            raise SyntaxError
        return win

    def update_screen_setup(self):
        self._stdscr.clear()
        height, width = self._stdscr.getmaxyx()
        record_string = ""

        # Application main info screen 12 rows ------------------------------------------
        win  = "***  Setup file   ***\n"
        win += "***  Center frequency:     " + "{0:.3}".format(float(self._dsp.get_c_freq())) + "            ***\n"
        win += "***  Record vector :    " + "{0:.3}".format("True")  + " **\n"
        win += "***  To change a value write: set $parameter $value   ***\n"
        win += "******************************************************************\n"
        win += "\n"
        win += "------------------------------------------------------------------\n"
        self._stdscr.addstr(0,0,win)
        # -------------------------------------------------------------------------------

        # Command history and info screen
        avil_rows = height - 7 - 1 # 14 rows occupied by information at top of string

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
