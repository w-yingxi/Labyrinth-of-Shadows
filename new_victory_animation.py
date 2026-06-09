import os
import sys
import re
import time
import random
import math
from utils import clear_screen

RESET = "\033[0m"
color_set = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]



def read_terminal():
    cols, rows=os.get_terminal_size()
    center_x=cols//2#center x-coordinate
    center_y=rows//2#center y-coordinate
    return rows, cols, center_x, center_y

def strip_ansi(text):
    return re.sub(r'\033\[[0-9;]*m', '', text)#strip any unwanted ANSI code, especially when calulating length

def move_cursor(x,y):
    # \003[{y};{x}H is ANSI escape code --> move cursor
    sys.stdout.write(f"\033[{y};{x}H") #"input" "command" to terminal to move cursor to (x,y)
    sys.stdout.flush() # ask buffer immediately send data in sys.stdout.write to terminals

def launch_rocket():
    rows,cols, center_x, center_y=read_terminal()
    centerX_pos=max(2, center_x)
    ground=max(8, rows-4)#launch from row-4 unless terminal is too small
    rocket=\
    ["  /\\  ",
     " /!!\\ ",
     "/||||\\",
     "  ||  ",
     "  /\\  "]
    for y in range (ground,6, -1):# y represents the bottom line of rocket. it decreases from ground to 6, so visually the rocket is moving upward
        clear_screen()
        for i, line in enumerate(rocket): # everytime when rocket move up by 1 row, enumerate the rocket to relocate each part
            line_y=y-(len(rocket)-1-i) # calculates the y coordinate (height from the bottom of the terminal) for each line of rocket
            if 1<=line_y<rows-1: # make sure the rocket will not touch the bottom or the top of the terminal screen
                rocket_centerX=max(1, centerX_pos-len(line)//2) # determine the x coordinate for each line, put it in the horizontal center place unless the terminal is too thin
                move_cursor(rocket_centerX,line_y)#move cursor to designated location
                sys.stdout.write(random.choice(color_set)+line+RESET) # print line with random color
        sys.stdout.flush() # show on screen
        time.sleep(0.06) #move in every 0.06 second
    time.sleep(0.18)#explode 0.18 second after rocket reach the top

def explosion():
    rows, cols, center_x, center_y = read_terminal()
    start_x=center_x
    start_y=max(4, rows//4) # explosion happens in upper part of the screen
    particles=[]
    for p in range (140):
        dx=random.uniform(-1,1)
        dy=random.uniform(-1,1)
        life=random.randint(10,40)
        color=random.choice(color_set)
        char=random.choice(['*', '.', 'o', '+', 'x'])
        particles.append([start_x,start_y,dx,dy,life,color,char]) # each particle has random direction, life span, color, type
    frame=0
    while frame<150 and any(p[4]>0 for p in particles): #the explotion lasts for 150 frames
        for r in range (3):# the circle increases for three times
            clear_screen()
            for radius in range (6+r*3): # radius increases by 3 each time
                angle=random.random()*2*math.pi # randomly choose an angle from 2pi
                rx=int(start_x+radius*math.cos(angle))
                ry=int(start_y+radius*math.sin(angle)*0.5)#explode in eclipse
                if 1<=rx<rows-1 and 2<=ry<cols-1:
                    move_cursor(rx,ry)
                    sys.stdout.write(random.choice(color_set)+random.choice(['*', '.', 'o', '+', 'x'])+RESET)
            sys.stdout.flush()
        for p in particles:
            if p[4] > 0:
                p[0] += p[2]  # change x coordinate of particle
                p[1] += p[3] # change y coordinate of particle
                p[4] -= 1  #life-1
                move_cursor(round(p[0]), round(p[1]))
                if 1<=round(p[0])<=cols-1 and 1<=round(p[1])<=rows-1:
                    sys.stdout.write(p[5]+ p[6] + RESET)#print particles
                    p[5] = random.choice(color_set)
                    p[6] = random.choice(['*', '.', 'o', '+', 'x'])
        sys.stdout.flush()
        frame+=1
        time.sleep(0.05)

def congrats():
    clear_screen()
    rows, cols, center_x, center_y = read_terminal()
    text='CONGRATULATIONS!!!YOU WIN!!!'
    banner=\
    [
    r"   _____ ____  _   _  _____ _____         _______ _    _ _            _______ _____ ____  _   _  _____  ",
    r"  / ____/ __ \| \ | |/ ____|  __ \     /\|__   __| |  | | |        /\|__   __|_   _/ __ \| \ | |/ ____| ",
    r' | |   | |  | |  \| | |  __| |__) |   /  \  | |  | |  | | |       /  \  | |    | || |  | |  \| | (___   ',
    r" | |   | |  | | . ` | | |_ |  _  /   / /\ \ | |  | |  | | |      / /\ \ | |    | || |  | | . ` |\___ \  ",
    r" | |___| |__| | |\  | |__| | | \ \  / ____ \| |  | |__| | |____ / ____ \| |   _| || |__| | |\  |____) | ",
    r"  \_____\____/|_| \_|\_____|_|  \_\/_/    \_\_|   \____/|______/_/    \_\_|  |_____\____/|_| \_|_____/  "
    ]
    if cols<len(strip_ansi(banner[0]))+4:#if terminal is too small to print banner
        start_x=max(1,center_x-len(strip_ansi(text))//2)#calculate with visible size==>guarantee the text will always shown in the center of the terminal  
        start_y=max(1, center_y)
        move_cursor(start_x, start_y)#move cursor to [start_x, start_y] so the text will be printed from [start_x, start_y]
        for char in text:
            sys.stdout.write(random.choice(color_set)+char+RESET)#print each character with different colors
            sys.stdout.flush()
            time.sleep(0.05)
        print()
        time.sleep(0.08)
    else:
        for i, line in enumerate(banner):
            start_x = max(1, (cols - len(strip_ansi(line))) // 2 + 1)#calculate with visible size
            start_y = max(1, (rows - len(banner)) // 2 + 1 + i)#move i rows from the top of the banner
            move_cursor(start_x, start_y)
            sys.stdout.write(random.choice(color_set)+line + RESET)#different colors for different lines
        sys.stdout.flush()
        time.sleep(0.05)

    confetti_Yrange=min(20, rows-rows//3)#confetti only appears in the lower part of the terminal
    frame=0
    while frame<70:
        for r in range (confetti_Yrange, rows):
            x=random.randint(1,cols-1)#randomly choose a column except the first col
            move_cursor(x,r)
            sys.stdout.write(random.choice(color_set)+random.choice(['*', '.', 'o', '+', 'x']) + RESET)
        sys.stdout.flush()
        time.sleep(0.05)
        frame+=1

    x = max(1,center_x-len(strip_ansi(text))//2+1)#calculate with visible size
    y = rows-3#print at the thrid-to-last row
    move_cursor(x, y)
    for char in text:
        sys.stdout.write(random.choice(color_set) + char + RESET)
        sys.stdout.flush()
        time.sleep(0.03)
    print()
    time.sleep(1)

def firework():
    launch_rocket()
    explosion()
    congrats()


