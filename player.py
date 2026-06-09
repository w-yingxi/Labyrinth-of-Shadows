from global_constants import operator
from utils import check_wall, check_block, move_block


def player_move(Command, list2, player_place, list1, operator):
    a, b = player_place
    dx,dy=operator[Command]#moving direction
    x,y=a+dx, b+dy#new position for player

    if not check_wall(list2, player_place, operator[Command]):#check if the new position is wall
        if check_block(list2, player_place, operator[Command]):# check if a block is in front of the player
            move_block(list2, player_place, operator[Command])# if yes, move the block in operator[Command] direction
            return list2, player_place # return new list2 after changing block position and player stays unmoved
        elif list1[a][b] == 0:  # check for breaking route (player can only pass once)
            list2[a][b] = 1 # breaking route becomes wall after player go through
        else:
            list2[a][b] = 3 
        player_place = [x, y] #update player position
        list2[x][y] = 4 #player move to new position 
        return list2, player_place
    else:
        return list2, False

