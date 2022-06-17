import os

MUX_COMMAND_PATH = "./USBLRB 0 "

class Multiplexer:
    curr_state = 0
    
    def switch_to_normal_mode(self):
        print("Normal mode")
    
    def swith_to_DLT_mode(self):
        print("DLT mode")