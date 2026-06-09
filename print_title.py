from utils import clear_screen, read_terminal, move_cursor
import time
import sys

def title():
    clear_screen()
    blue = '\033[38;5;17m'
    reset = "\033[0m"
    cols, rows = read_terminal()
    text='LABYRINTH OF SHADOWS'
    #two titles are generated using https://patorjk.com/software/taag/
    title = r''' _           _                _       _   _              __   _____ _               _                   
| |         | |              (_)     | | | |            / _| /  ___| |             | |                  
| |     __ _| |__  _   _ _ __ _ _ __ | |_| |__     ___ | |_  \ `--.| |__   __ _  __| | _____      _____ 
| |    / _` | '_ \| | | | '__| | '_ \| __| '_ \   / _ \|  _|  `--. \ '_ \ / _` |/ _` |/ _ \ \ /\ / / __|
| |___| (_| | |_) | |_| | |  | | | | | |_| | | | | (_) | |   /\__/ / | | | (_| | (_| | (_) \ V  V /\__ \
\_____/\__,_|_.__/ \__, |_|  |_|_| |_|\__|_| |_|  \___/|_|   \____/|_| |_|\__,_|\__,_|\___/ \_/\_/ |___/
                    __/ |                                                                               
                   |___/                                                                                '''
    lines1 = [line for line in title.splitlines()]
    max_len1 = max(len(line) for line in lines1)
    title2 = r'''░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓████████▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░


 ░▒▓██████▓▒░░▒▓████████▓▒░       ░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒▒▓█▓▒░      
░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░         ░▒▓██████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓██████▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                    ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒
 ░▒▓██████▓▒░░▒▓█▓▒░             ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓███████████▓▒░░▒▓███████▓▒
'''
    lines2 = [line for line in title2.splitlines()]
    max_len2 = max(len(line) for line in lines2)
    last_line = 0
    if max_len1 <= cols and len(lines1)<=rows<len(lines2):# if the terminal is not large enough 
        start_x = max(1,(cols - max_len1) // 2)
        start_y = max(1, (rows - len(lines1)) //2)
        for i, line in enumerate(lines1):
            move_cursor(start_x, start_y + i)
            sys.stdout.write(blue + line + reset)
            i += 1
        last_line = start_y + len(lines1)
    elif cols >= max_len2 and rows > len(lines2):
        start_x = max(1,(cols - max_len2) // 2)
        start_y = max(1,(rows - len(lines2)) // 2)
        for i, line in enumerate(lines2):
            move_cursor(start_x, start_y + i)
            sys.stdout.write(blue + line + reset)
            i += 1
        last_line = start_y + len(lines2)
    else:#if terminal is too thin
        start_x = max(1, cols // 2)
        start_y = max(1, rows // 2 + 1)
        move_cursor(start_x, start_y)
        sys.stdout.write(blue + text + reset)
        last_line = start_y
    sys.stdout.flush()
    for _ in range(rows - last_line):
        print()
    time.sleep(1.5)


