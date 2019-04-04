#!/usr/bin/env python3
"""
Name: jranderson
Date: 04.02.19
Purpose: Tic-Tac-Toe Outcome-Regex 
"""

import os
import re
import sys

#---------------------------------------------------------
def main():
    """Sko-Codin!"""

    args = sys.argv[1:]
    
    if len(args) != 1:
        print('Usage: {} STATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    state = args[0].upper()

    win_dict = {'XXX......':'X', 'OOO......':'O', '...XXX...':'X',
                '...OOO...':'O', '......XXX':'X', '......OOO':'O', 
                'X..X..X..':'X', 'O..O..O..':'O', '.X..X..X.':'X', 
                '.O..O..O.':'O', '..X..X..X':'X', '..O..O..O':'O', 
                'X...X...X':'X', 'O...O...O':'O', '..X.X.X..':'X', 
                '..O.O.O..':'O'}

    instate_re = re.compile('^[.XO]{9}')
    good_input = instate_re.match(state)

    if good_input:
        win1 = re.compile('(?P<win1>XXX|OOO)')
        w1 = win1.search(state)

        win2 = re.compile('(?P<win2>[X](?:[\.O]){1,2}[X](?:[\.O]){1,2}[X]|[O](?:[\.X]){1,2}[O](?:[\.X]){1,2}[O])') 
        w2 = win2.search(state)

        for move, winner in win_dict.items():
            match = re.fullmatch(move, state)
            if match:
                print('{} has won'.format(winner))
                sys.exit(1)
        print('No winner')
 
    else:
        print('State "{}" must be 9 characters of only ., X, O'.format(state))

#---------------------------------------------------------
if __name__ == '__main__':
    main()
