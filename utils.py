import os
import copy
from level_map import Level
from global_constants import directions, operator, items
import sys

def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear')#clear the entire sceen (before or after printing)

def read_terminal():
    cols, rows=os.get_terminal_size()#get the size of terminal
    return cols, rows

def move_cursor(x,y):
    sys.stdout.write(f"\033[{y};{x}H")#ANSI escape code to move cursor
    sys.stdout.flush()#send insturction immediately to terminal

def print_rules():
    print('Welcome to the game!')
    print('1. You are \U0001F604.')
    print('2. \U0001F47E is the monster. \U0001F47E will move in random directions and kill you if it catches you.')
    print('3. The exit will not open \U0001F7E5 before you get all the keys \U0001F511.')
    print('4. \U0001F7E9 stands for open exit.')
    print('5. \U00002B1C are blocks you could push onto an empty space.')
    print('6. You cannot walk through walls \U00002B1B.')
    print('7. \U0001F7E6 is one-way-path. After you pass through it, it will turn into walls \U00002B1B. ')
    print('Controls: w/a/s/d to move, q to quit, r to restart')

def readdata(level):  # reads maze data (list1 is template and should not be changed), player position, and exit position
    list1, _, _=Level(level) #get the chosen template of game map
    list2 = copy.deepcopy(list1)#create a copy of the game map for further updates
    player_place = track_player(list2)#locate the player
    exit_place=[]
    for row in range (len(list2)):
        for col in range (len(list2[row])):
            if list2[row][col] == 7 or list2[row][col] == 8:
                exit_place = [row, col] #reads exit data
    return list1, list2, player_place, exit_place

def command():  # ask for input: WASDRQ
    while True:
        Command = input('Please enter your choice (WASD or wasd, R for restart, Q for quit): ').upper()
        if Command in {'W', 'A', 'S', 'D', 'Q', 'R', 'END'}:
            return Command
        else:
            print('Invalid choice. Please re-enter.')

def check_block(list2, player_place, direction):
    x,y = player_place
    dx,dy=direction
    if list2[x+dx][y+dy] == 2:#if block is in front of the player
        return True
    else:
        return False

# check_block is True, so moves block:
def move_block(list2, player_place, direction):
    x,y = player_place
    dx,dy=direction
    if list2[x+dx+dx][y+dy+dy] not in [1, 2, 5, 6, 7, 8]:#check if there is space for movement behind the block 
        list2[x+dx][y+dy]=3 #[x+dx,y+dy] is block position
        list2[x+dx+dx][y+dy+dy]=2
        return list2 #True
    else: #Fail to move block because something other than space is behind it. 
        return False

def check_wall(list2, player_place, direction):
    x,y = player_place
    dx,dy=direction
    if list2[x+dx][y+dy] == 1 or list2[x+dx][y+dy] == 7:#check if there is wall or closed-exit in front of player
        return True
    else:
        return False

def check_one_way_path(list1, player_place, direction):
    x, y = player_place
    dx, dy = direction
    if list1[x + dx][y + dy] == 0: #check if one-way path is in front of the player
        return True
    else:
        return False

def find_key(list1, list2, player_place, collected_key):
    x, y = player_place
    if list1[x][y] == 5: 
        if [x,y] not in collected_key: #check if the key has been collected
            list2[x][y]=4
            collected_key.append([x,y]) # store the key position to represent the key has been collected
            return collected_key,True
        else:
            # when list1[x][y]==5 but [x,y] in collected_key, the key has been collected
            return collected_key,False
    else: 
        # [x,y] does not have key
        return collected_key,False

# if keys aren't all collected, exit won't open
def key_check(keyCount, level):
    _, total_keys, _=Level(level)
    if keyCount == total_keys:  
        return True
    return False

def open_exit(list2, keyCount, exit_place, level):
    a, b = exit_place
    if key_check(keyCount, level):#all keys are collected
        list2[a][b] = 8 #exit open
        return list2, True # return the updated map
    else:
        return list2, False

def track_player(list2):#trace player position
    player_place = []
    for row in range (len(list2)):
        for col in range (len(list2[row])):
            if list2[row][col] == 4:
                player_place=[row, col]
    return player_place

