from src import *

class Window():
    def __init__(stdscr,cl,pos,dsp,data,pars,info_string,recEvent):
        self._stdscr = stdscr
        self._cl = cl
        self._pos = pos
        self._dsp = dsp
        self._data = data
        self._pars = pars
        self._info_string = info_string
        self._recEvent = recEvent
        _centerFrequency = 0
        _vectorRec = 0

        #updates the program with the current values in setup.txt
        updateFile()

    def updateFile():
        myfile = open(str("setup.txt"), "r")
        lineNo = 0
        centerFrequencyLineNo = 0
        vectorRecLineNo = 0

        for line in myfile:
            fileVec = line.split(" ")
            while lineNo < setupLen+2:
                lineNo += 1

                if "centerFrequency" in line:
                    _centerFrequency = float(fileVec[2])
                    centerFrequencyLineNo = lineNo
                elif "vectorRec" in line:
                    _vectorRec = bool(fileVec[2])
                    vectorRecLineNo = lineNo

    def update(currentWindow):
        if currentWindow == "app":
            update_screen_functions(self._stdscr,self._cl,self._pos,self._dsp,
                                    self._data,self._pars,self._info_string,self._recEvent)

        elif currentWindow == "setup"
            update_screen_setup()

    #finds the size of the setup.txt file.
    def setup_size():
        with open("setup.txt") as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    def setup_app(self):

        k = "" #init k the input character
        info_string = ""
        instruction = "# Write command$ " #17 characters
        tid = 0
         # Controll of main loop

        if command_queue[0] == "set":
            myfile = open(str("setup.txt"), "r")
            myfile_data = list(source_file.read())
            myfile.close()

            if len(command_queue) > 1:
                try:
                    insertData = str(command_queue[2])
                    if command_queue[1] == "center_frequency":
                        myfile_data.insert(centerFrequencyLineNo,
                                        "centerFrequency = " + insertData)

                    elif command_queue[1] == "vector_rec":
                        myfile_data.insert(vectorRecLineNo,
                                        "vectorRec = " + insertData)

                except ValueError:
                    info_string = 'should be in the format: set $parameter $value '
            else:
                info_string = 'should be in the format: set $parameter $value '


            myfile = open(str("setup.txt"), "wb").wite(myfile_data)

        #quit the program
        elif command_queue[0] == "quit":
            currentWindow = "app"

        else:
            info_string = 'undefined command: ' + str(command_queue[0])


def update_screen_functions(stdscr,cl,pos,dsp,data,pars,info_string,rec_event):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    record_string = ""
    if rec_event.isSet():
        record_string = "Recording"
    else:
        record_string = "Not active"

    # Application main info screen 12 rows ------------------------------------------
    win  = "***  Antenna characteriastion aplication   ***\n"
    win += "***  Temperature in box:     " + "{0:.3}".format(float(pos.getTemperature())) + "            ***\n"
    win += "***  Running time:           " + str(_cl)+ "            ***\n"
    win += "***  current signal strengt: " + "{0:.3}".format(float(data.getData(2))) + "        *** \n"
    win += "***  current ceter freq:     " + "{0:.7}".format(float(dsp.get_c_freq())) + "      **\n"
    win += "***  current position X :    " + "{0:.5}".format(float(pos.get_X()))  + " **\n"
    win += "***  current position Y :    " + "{0:.5}".format(float(pos.get_Y()))  + " **\n"
    win += "***  current position Z :    " + "{0:.5}".format(float(pos.get_Z()))  + " **\n"
    win += "***  Recording status : "+ record_string + ", Currentloop: "+ str(data.getData(3)) +" **\n"
    win += "***  avilable commands: setcfreq, getcfreq, val, quit, origin  ***\n"
    win += "***  recordtime, recordsamples, plot                           ***\n"
    win += "******************************************************************\n"
    win += "\n"
    win += "------------------------------------------------------------------\n"
    stdscr.addstr(0,0,win)
    # -------------------------------------------------------------------------------

    # Command history and info screen
    avil_rows = height - 14 - 1 # 14 rows occupied by information at top of string

    command_history = pars.get_history()
    list_length = len(command_history)
    str_length = len(info_string)
    str_length = int(math.ceil(double(str_length)/width)) # Number of rows in infostring
    if str_length > 0:
        pars.add_history(_info_string.split('\n'))
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
            stdscr.addstr(height-2-str_length-i, 0,str(tmp_str))
    stdscr.addstr(height-1, 0,"# Write command$ "+_pars.get_full_string()) # Command input

def help_string(help_command):
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
    else:
        raise SyntaxError
    return win

def update_screen_setup(pars, info_string):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    record_string = ""

    # Application main info screen 12 rows ------------------------------------------
    win  = "***  Setup file   ***\n"
    win += "***  Center frequency:     " + "{0:.3}".format(float(_centerFrequency) + "            ***\n"
    win += "***  Record vector :    " + "{0:.3}".format(_vectorRec)  + " **\n"
    win += "***  To change a value write: set $parameter $value   ***\n"
    win += "******************************************************************\n"
    win += "\n"
    win += "------------------------------------------------------------------\n"
    stdscr.addstr(0,0,win)
    # -------------------------------------------------------------------------------

    # Command history and info screen
    avil_rows = height - 7 - 1 # 14 rows occupied by information at top of string

    command_history = pars.get_history()
    list_length = len(command_history)
    str_length = len(info_string)
    str_length = int(math.ceil(double(str_length)/width)) # Number of rows in infostring
    if str_length > 0:
        pars.add_history(info_string.split('\n'))
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
            stdscr.addstr(height-2-str_length-i, 0,str(tmp_str))
    stdscr.addstr(height-1, 0,"# Write command$ "+_pars.get_full_string()) # Command input
