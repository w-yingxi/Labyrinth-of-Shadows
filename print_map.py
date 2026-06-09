from level_map import Level
from global_constants import items
from utils import open_exit, clear_screen, read_terminal, move_cursor
import os
import sys


def map_print(list2, keyCount, exit_place, level):
    cols, rows=read_terminal()
    table=print_table(list2, exit_place, keyCount, level)
    printMap=[]#create a new map (only for print) to get total size of game-map and table
    new_row=''
    for i in range(len(list2)):
        for k in list2[i]:
            new_row+=items[k]
        if i<len(table):
            new_row+=f"          {table[i]}"
        printMap.append(new_row)
        new_row=''

    start_x=max(1, (cols-len(printMap[0]))//2)#the map will always print from a collumn that is half length of itself from center column==>place in center
    start_y=max(1, (rows-len(printMap))//2)

    for i, r in enumerate (printMap):
        move_cursor(start_x,start_y+i) # move to next row in terminal==>each line is "i" rows from the top of the map
        sys.stdout.write(r) # print r of printMap
    sys.stdout.flush()
    for _ in range(max(1,(rows-len(printMap))//2)): #so the game-instruction line will not print immediately after the map (more aesthetic)
        print()

def print_table(list2, exit_place, keyCount, level):
    _,alpha=open_exit(list2, keyCount, exit_place, level)
    _,total_keys,_=Level(level)
    if alpha: #keys all collected is True
        exit='open  '
    else:
        exit='closed'
    clear_screen()
    table=[
        f'=============GAME STATUS=============',
        f'||    Total keys: {total_keys}                ||',
        f'||    Number of keys collected: {keyCount}  ||',
        f'||    Exit status: {exit}          ||',
        f'====================================='
    ]
    return table


