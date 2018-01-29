#!/usr/bin/env python

import sys,os
import curses
import time
import threading

def stuff(stdscr):

    def update_screen(cl):
        #val_str = str(self.get_val())
        win =  "**********************************************\n"
        win += "***  Antenna characteriastion aplication   ***\n"
        win += "***  Running time:          " +str(cl)+"            ***\n"
        win += "***  current signal strengt: " +" val_str" + " *** \n"
        win += "***  current ceter freq:     " + "str(self.get_c_freq())" + "      **\n"
        win += "***  current position X :     ""+ str(pos.get_X())"  +" **\n"
        win += "***  current position Y :     ""+ str(pos.get_Y())  "+" **\n"
        win += "***  current position Z :     ""+ str(pos.get_Z())  "+" **\n"
        win += "***  avilable commands: freq, val, record, setvalfreq, quit, origin ***\n"
        win += "**********************************************\n"
        return win

    # Initialization
    stdscr.clear()
    stdscr.refresh()
    stdscr.nodelay(1)
    stdscr.keypad(1)
    k = "" #init k
    in_string = ""
    command_history = ["1","2","3","4","5"] 
    nr = 0
    running = True
    while (running):
        
        
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        nr = nr+0.1 
        stdscr.addstr(0,0 ,update_screen(nr))

        time.sleep(0.1)

        k = stdscr.getch()
        if (k > 64 and k<91) or (k>97 and k<123):
            in_string = in_string + chr(k)
            #in_string = "test"
        elif k == 263:
            in_string = in_string[:-1]
        elif k == 10:
            if in_string == "time":
                nr = 0
            elif in_string == "quit":
                running = False
            h_len = len(command_history)-1
            for i in range(0,h_len):
                command_history[h_len-i] = command_history[h_len-1-i]
            command_history[0] ="Command history: " + in_string
            in_string = ""

        stdscr.addstr(13, 0,command_history[0])
        stdscr.addstr(14, 0,command_history[1])
        stdscr.addstr(15, 0,command_history[2])
        stdscr.addstr(12, 0,"# Write command$ "+in_string)
        #stdscr.addstr(13, 13,str(k))
        
        #win = curses.newwin(10,10,3,3)
        #win.addstr("window?")
        stdscr.refresh()
    stdscr.keypad(0)

def main():
    curses.wrapper(stuff)

if __name__ == '__main__':
    main()
