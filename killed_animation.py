import time
import os
from utils import read_terminal, move_cursor, clear_screen
import sys


def words():
    red = "\033[31m" # dark red
    reset = "\033[0m" # color of terminal
    #message is generated using https://patorjk.com/software/taag/
    message = """
 ███▄ ▄███▓ ▒█████   ███▄    █   ██████ ▄▄▄█████▓▓█████  ██▀███  
▓██▒▀█▀ ██▒▒██▒  ██▒ ██ ▀█   █ ▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
▓██    ▓██░▒██░  ██▒▓██  ▀█ ██▒░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
▒██    ▒██ ▒██   ██░▓██▒  ▐▌██▒  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
▒██▒   ░██▒░ ████▓▒░▒██░   ▓██░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
░  ░      ░  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░
░      ░   ░ ░ ░ ▒     ░   ░ ░ ░  ░  ░    ░         ░     ░░   ░ 
       ░       ░ ░           ░       ░              ░  ░   ░     
                  
                  
                  You were caught by monster
"""
    lines = message.strip("\n").split("\n") # split "message" by lines to from a list for iterate
    len_message=0
    for l in lines:
        if len(l)>len_message:
            len_message=len(l) # find the max horizontal length of "message"
    clear_screen()
    cols, rows=read_terminal()
    start_x=max(1, (cols-len_message)//2) # print "message" in the center of terminal
    start_y=max(1,(rows-len(lines))//2)

    for i, line in enumerate(lines):
        move_cursor(start_x, start_y+i)#start to print at [start_x, start_y+i]
        sys.stdout.write(red+line+reset)#print in red
        sys.stdout.flush()
        time.sleep(0.12)  # Delay between lines
    for _ in range (max(1,(rows-len(lines))//2)):
        print()





