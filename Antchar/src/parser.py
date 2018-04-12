from src import *

class parser():
    command_que = []
    total_string = ""
    command_history = []
    history = []
    question = False
    do_status = False
    key_count = 0

    def new_character(self,k):

        if k == 32: # space
           self.total_string = self.total_string + chr(k)

        elif k == 10: # newline
            self.do_status = True
            self.command_que.extend(self.total_string.split(' '))
            self.command_history.append(self.total_string)
            self.history.append(self.total_string)
            self.total_string = ""
            self.key_count = 0

        elif k == 259: #key upp
            tmplen = len(self.command_history)

            if self.key_count < tmplen:
                self.key_count += 1

            if self.key_count <= tmplen and tmplen !=0:
                self.total_string = self.command_history[tmplen-self.key_count]

        elif k == 258: #key down
            if self.key_count > 0: # Only decrement if it has been incremented before
                self.key_count -= 1
            tmplen = len(self.command_history)
            if self.key_count == 0:
                self.total_string = ""
            elif self.key_count <= tmplen:
                self.total_string = self.command_history[tmplen-self.key_count]
        #elif k == 260: #key left
        #elif k == 261: #key right

        elif k == 263: # Backspace
            self.total_string = self.total_string[:-1]

        elif (k > 64 and k<91) or (k>96 and k<123) or k == 46: #letters
            self.total_string = self.total_string + chr(k)

        elif (k>47 and k<58): #Numbers
            self.total_string = self.total_string + chr(k)

        elif (k == 95): #Underline
            self.total_string = self.total_string + chr(k)

    def get_full_string(self):
        #Return the total string
        return self.total_string

    def clear_string(self):
        self.total_string = ""

    def add_history(self,_str):
        self.history.extend(_str)

    def add_command_history(self,_str):
        self.command_history.extend(_str)

    def get_command_history(self):
        return self.command_history

    def get_do_status(self):
        #return the do status
        return self.do_status

    def get_queue(self):
        #return que
        return self.command_que

    def set_status_false(self):
        #return que
        self.do_status = False

    def get_history(self):
        return self.history

    def empty_queue(self):
        self.command_que[:] = []

    def get_question(self):
        return self.question

    def set_question(self, status):
        self.question = status
