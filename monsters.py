import random

def read_monster(list2): # find monsters
    monster_pos_lst = []#store location of each monster
    for row in range(len(list2)):
        for col in range(len(list2[row])):
            if list2[row][col]== 6:
                monster_pos_lst.append([row,col])
    return monster_pos_lst

def check_player_monster(list2,player_place, monster_pos_lst):  #check if player is on the same position as monster
    for monster_pos in monster_pos_lst:
        if player_place == monster_pos:
            return True
    return False

def monster_func(list1, list2, monster_pos_lst,player_place):
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    move_check = False

    for k,monster_pos in enumerate(monster_pos_lst):
        a,b = monster_pos
        list2[a][b]=3
        random.shuffle(directions)
        for dx,dy in directions: #randomly moves the monster by 1 unit
            c, d = a+dx, b+dy # new position of monster
            if list2[c][d] in [3,4]: #monster can only move onto blank space or player (moving through one-way path could cause bugs.)
                monster_pos_lst[k] = [c,d] # update original monster position 
                if [c,d]==player_place:
                    list2[c][d]=9 #catches player
                    return list2,True,monster_pos_lst    
                list2[c][d] = 6 # monster moves to new position
                move_check = True
                break
    if move_check == False: #nowhere to move. Monster stays in current position.
        list2[a][b]=6
    return list2,False,monster_pos_lst


