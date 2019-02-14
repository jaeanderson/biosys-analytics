#!/usr/bin/env python3
"""
Author : jranderson
Date   : 2019-02-14
Purpose: Tic-Tac-Toe
"""

import sys
import os
import re
import argparse

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe board',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--state',
        help='Board state',
        metavar='str',
        type=str,
        default='.........')

    parser.add_argument(
        '-p',
        '--player',
        help='Player',
        metavar='str',
        type=str,
        default='')

    parser.add_argument(
        '-c',
        '--cell',
        help='Cell to apply -p',
        metavar='str',
        type=int)

    return parser.parse_args()
# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)
# --------------------------------------------------
def die(arg_type, arg_input):
    """warn() and exit with error"""
    if arg_type == 'state':
        msg_end = '9 characters of only -, X, O'
    elif arg_type == 'player':
        msg_end = 'X or O'
    else:
        msg_end = '1-9'

    msg='Invalid {} "{}", must be {}'.format(arg_type, arg_input, msg_end)
    warn(msg)
    sys.exit(1)
# --------------------------------------------------

def main():
    """main"""

    args = get_args()
    state = args.state
    plyr = args.player
    cell = args.cell

    boardsize = 3
    board = []
    hline = '-------------'

    if state == '.........' and plyr == '' and cell == None:
        print (hline)
        for i, c in enumerate(state):
            cell_value = i + 1 if c == '.' else c
            print('|{:^3}'.format(cell_value), end='')
            if (i+1) % boardsize == 0:
                print('|\n' + hline)
        sys.exit(1)
 
    state_ctr = 0
    for state_var in state.upper():
        if state_var in '.OX':
            state_ctr += 1

    if (len(state) != 9) or (state_ctr != len(state)):
        die("state", state)
    elif plyr == '' and cell == None:
        print(hline)
        for i, c in enumerate(state):
            cell_value = i + 1 if c == '.' else c
            print ('|{:^3}'.format(cell_value), end='')
            if (i+1) % boardsize == 0:
                print('|\n' + hline)
        sys.exit(1)

    if (plyr not in 'XO') and cell == None and state == '.........':
        die("player", plyr)

    if cell not in range(1,10) and plyr == '' and state == '.........':
        die("cell", cell)

    if (any([plyr, cell]) and not all([plyr, cell]) and state == '.........'):
        print('Must provide both --player and --cell')
        sys.exit(1)
    else:
        board = list(state)
        if board[cell-1] == 'X' or board[cell-1] == 'O':
            print('Cell {} already taken'.format(cell))
            sys.exit(1)
        else: 
            print(hline)
            for i, c in enumerate(state):
                cell_value = i + 1 if c == '.' else c
                if cell == cell_value:
                    cell_value = plyr
                print ('|{:^3}'.format(cell_value), end='')
                if (i+1) % boardsize == 0:
                    print('|\n' + hline)
    
    

#----------------------------------------------------
if __name__ == '__main__':
    main()
