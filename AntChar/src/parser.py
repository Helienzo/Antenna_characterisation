from src import *

class parser():
    command_que = []
    total_string = ""
    short_string = ""
    command_history = []
    do_status = False

    def new_character(self,k):
        if k == 32: # space
           self.command_que.append(self.short_string)
           self.short_string = ""
           self.total_string = self.total_string + chr(k)

        elif k == 10: # newline
            self.do_status = True
            self.command_que.append(self.short_string)
            self.command_history.append(self.total_string)
            self.short_string = ""
            self.total_string = ""

        elif k == 263: # Backspace
            self.total_string = self.total_string[:-1]
            self.short_string = self.short_string[:-1]

        elif (k > 64 and k<91) or (k>96 and k<123) or k == 46: #letter
            self.total_string = self.total_string + chr(k)
            self.short_string = self.short_string + chr(k)

        elif (k>47 and k<58): #Numbers
            self.total_string = self.total_string + chr(k)
            self.short_string = self.short_string + chr(k)

    def get_full_string(self):
        #Return the total string
        return self.total_string

    def clear_string(self):
        self.total_string = ""
    
    def add_history(self,_str):
        self.command_history.extend(_str)

    def get_do_status(self):
        #return the do status
        return self.do_status

    def get_que(self):
        #return que
        return self.command_que

    def set_status_false(self):
        #return que
        self.do_status = False

    def get_history(self):
        return self.command_history

    def empty_que(self):
        self.command_que[:] = []
