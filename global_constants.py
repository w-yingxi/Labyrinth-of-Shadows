directions=[(1,0), (-1,0), (0,1), (0,-1)]
operator={'W':(-1,0),'S':(1,0),'A':(0,-1),'D':(0,1)} 

#this dictionary allows numbers in the maze list to be printed as emojis and spaces
items = {0: '\U0001F7E6', 1: '\U00002B1B', 2: '\U00002B1C', 3: '  ', 4: '\U0001F604', 5: '\U0001F511', 6: '\U0001F47E',
         7: '\U0001F7E5', 8: '\U0001F7E9', 9:'💀'}
# 0 for breaking route(player can only pass once), 1 for unmovable wall, 2 for movable block,
# 3 for space, 4 for playerP, 5 for key, 6 for monster(randomly moving), 7 for closed exit, 8 for opened exit, 9 for skull (dead player)
