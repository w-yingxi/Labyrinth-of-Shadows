from utils import clear_screen, print_rules, readdata, command, track_player, open_exit, find_key
from level_map import Level 
from monsters import read_monster, check_player_monster, monster_func
from print_map import map_print
from player import player_move
from global_constants import operator, directions, items
from new_victory_animation import firework
from killed_animation import words
import time
from print_title import title

def main():
    title()
    clear_screen()
    print_rules()
    while True:  #Select level.
        level=input('Choose level(1~3): ')
        if level.isnumeric():
            if 1<= int(level) <= 3:
                level = int(level)
                break
            else:
                print('Invalid level.')
        else:
            print('Invalid level.')
    
    #Randomly select maze form level.
    list1, list2, player_place, exit_place=readdata(level)
    monster_pos_lst=read_monster(list2)

    keyCount=0 
    collected_key=[] #stores the location of collected keys to check if the key is collected before
    map_print(list2, keyCount, exit_place, level)#print initial map
    while True:
        Command = command()#get command
        if Command=='Q':
            print('Game Over. Thanks for playing! ')
            break
        elif Command=='R':
            clear_screen()
            main()#restart the game
            break
        else:
            player_place=track_player(list2)#trace the player position everytime before moving 
            list2, new_player_place=player_move(Command, list2, player_place, list1, operator)
            if new_player_place: # check if player is able to move
                player_place=new_player_place
            if check_player_monster(list2,player_place, monster_pos_lst): #First check for monster: Player moves, monsters don't.
                x,y=player_place
                list2[x][y]=9
                map_print(list2,keyCount,exit_place,level)#print map to show player where they are killed
                time.sleep(0.1)
                clear_screen()
                words()#print monster animation
                print('You stepped onto a monster.')
                new_command = input('Enter R to restart, any other key to quit: ').upper()
                if new_command == 'R':
                    main()
                else: 
                    clear_screen()
                    print('Game Over. Thanks for playing! ')
                break

            list2,player_caught,monster_pos_lst = monster_func(list1, list2, monster_pos_lst,player_place)
            #monster move after player 
            if player_caught: #Second check after monster moves. 
                map_print(list2,keyCount,exit_place,level)
                time.sleep(0.5)
                clear_screen()
                words()
                new_command = input('Enter R to restart, any other key to quit: ').upper()
                if new_command == 'R':
                    main()
                else:
                    clear_screen()
                    print('Game Over. Thanks for playing! ')
                break
            map_print(list2, keyCount, exit_place, level)
            #if player is not killed by monsters, check if they get the keys
            collected_key, check = find_key(list1, list2, player_place, collected_key)#get updated collected_key
            if check:
                keyCount += 1
            list2,alpha=open_exit(list2, keyCount, exit_place, level)#check exit
            if player_place==exit_place and alpha: #Reach open exit and wins
                time.sleep(0.25)
                firework()#print victory animation
                new_command = input('Enter R to restart, any other key to quit: ').upper()
                if new_command == 'R':
                    clear_screen()
                    main()
                else:
                    #clear_screen()
                    print('Game Over. Thanks for playing! ')
                break

main()
