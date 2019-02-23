#!/usr/bin/env python3
"""
j.r.anderson
Date:     2019-02-18
Purpose:  Tic-Tac-Toe Outcome
"""

import argparse
import sys
import re
import os

# --------------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe Outcome',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
    'positional', help='A positional argument', metavar='STATE')

    return parser.parse_args()
# --------------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)
#---------------------------------------------------------
def die(msg='Something bad happend'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)
#---------------------------------------------------------
def main():
    """Let the party begin"""

    args = get_args()
    state_outcome = args.positional
    win_dict = {'XXX......':'X', 'OOO......':'O', '...XXX...':'X',
                '...OOO...':'O', '......XXX':'X', '......OOO':'O', 
                'X..X..X..':'X', 'O..O..O..':'O', '.X..X..X.':'X', 
                '.O..O..O.':'O', '..X..X..X':'X', '..O..O..O':'O', 
                'X...X...X':'X', 'O...O...O':'O', '..X.X.X..':'X', 
                '..O.O.O..':'O'}


    if not re.search('^[.XO]{9}$',state_outcome):
        die('State "{}" must be 9 characters of only ., X, O'.format(state_outcome))


    state_translate = ''

    if win_dict.get(state_outcome) != None:
        die('{} has won'.format(win_dict.get(state_outcome)))

    for move, player in win_dict.items():
        #print('move: {} player: {}'.format(move,player))
        for i, char in enumerate(state_outcome, start=1):
            if char == move[i-1]:
                state_translate += str(char)
            else:
                state_translate += '.'
        #print(state_translate)
        if state_translate == move:
            #print('HELLO')
            die('{} has won'.format(win_dict.get(state_translate)))
        #else:
        #    die('No winner')
        state_translate = ''
    die('No winner')




#---------------------------------------------------------
if __name__ == '__main__':
    main()
