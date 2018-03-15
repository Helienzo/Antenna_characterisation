from src import *

def update_screen(stdscr,_cl,_pos,_radio,_data,_pars,_info_string,rec_event):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    record_string = ""
    if rec_event.isSet():
        record_string = "Recording"
    else:
        record_string = "Not active"
    
    # Application main info screen 12 rows ------------------------------------------
    win =  "**********************************************\n"
    win += "***  Antenna characteriastion aplication   ***\n"
    win += "***  Running time:          "  +str(_cl)+"            ***\n"
    win += "***  current signal strengt: " + str(_data.getData(2)) + " *** \n"
    win += "***  current ceter freq:     " + str(_radio.get_c_freq()) + "      **\n"
    win += "***  current position X :     "+ str(_pos.get_X())  +" **\n"
    win += "***  current position Y :     "+ str(_pos.get_Y())  +" **\n"
    win += "***  current position Z :     "+ str(_pos.get_Z())  +" **\n"
    win += "***  Recording status : "+ record_string + ", Currentloop: "+ str(_data.getData(3)) +" **\n"
    win += "***  avilable commands: setcfreq, getcfreq, val, quit, origin  ***\n"
    win += "***  recordtime, recordsamples, plot                           ***\n"
    win += "******************************************************************\n"
    win += "\n"
    win += "------------------------------------------------------------------\n"
    stdscr.addstr(0,0,win)
    # -------------------------------------------------------------------------------

    # Command history and info screen
    avil_rows = height - 14 - 1 # 14 rows occupied by information at top of string
    
    command_history = _pars.get_history()
    list_length = len(command_history)
    str_length = len(_info_string)
    str_length = int(math.ceil(double(str_length)/width)) # Number of rows in infostring
    if str_length > 0:
        _pars.add_history(_info_string.split('\n'))
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

