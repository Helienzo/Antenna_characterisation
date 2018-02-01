from src import *

def update_screen(stdscr,_cl,_pos,_radio,_pars,_info_string):

    height, width = stdscr.getmaxyx()
    
    # Application main info screen 12 rows ------------------------------------------
    win =  "**********************************************\n"
    win += "***  Antenna characteriastion aplication   ***\n"
    win += "***  Running time:          "  +str(_cl)+"            ***\n"
    win += "***  current signal strengt: " + str(_radio.get_val()) + " *** \n"
    win += "***  current ceter freq:     " + str(_radio.get_c_freq()) + "      **\n"
    win += "***  current position X :     "+ str(_pos.get_X())  +" **\n"
    win += "***  current position Y :     "+ str(_pos.get_Y())  +" **\n"
    win += "***  current position Z :     "+ str(_pos.get_Z())  +" **\n"
    win += "***  avilable commands: freq, val, record, setvalfreq, quit, origin ***\n"
    win += "**********************************************\n"
    win += "\n"
    win += "----------------------------------------------------\n"
    stdscr.addstr(0,0,win)
    # -------------------------------------------------------------------------------

    # Command history and info screen
    avil_rows = height - 12 - 1
    
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
        win += "command:           explanation:                         \n"
        win += "--------------------------------------------------------\n"
        win += "record $number     records $number of measurements      \n"
        win += "                   into measurement.txt                 \n"
        win += "value              returns the current SDR value (in dBm)\n"
        win += "quit               exits the current session            \n"
    
    elif(help_command == "quit"):
        win = "quit: exits the current session and closes the           \n"
        win += "terminal window                                         \n"
    
    elif(help_command == "value"):
        win =   "returns the signal strength that the SDR-dongle is     \n"
        win +=  "measuring in dBm                                       \n"
    else:
        raise SyntaxError
    return win

