#!/usr/bin/env python3
"""
Name: jranderson
Date: 03.17.19
Purpose: War! The Cardgame. 
"""

import argparse
import os
import re
import sys
import random
import itertools
from random import shuffle

# --------------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
      description='"War" cardgame',
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
      '-s',
      '--seed',
      help='Random seed',
      metavar='int',
      type=int,
      default=None)

    return parser.parse_args()

# --------------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)

# --------------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)

#---------------------------------------------------------
def main():
    """Let's get ready to code!"""

    args = get_args()
    seed = args.seed

    suits = ['\u2660','\u2663','\u2665','\u2666']
    cvalues = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

    cdeck = (list(itertools.product(suits, cvalues)))
    #print(sorted(cdeck))
    
    d = list(v+s for v, s in cdeck)
    deck_dict = {}   
    for i, card in enumerate(d):
        vmod = i % 13
        deck_dict[card] = vmod + 1

    
    card_list = list(deck_dict.keys())
    random.seed(seed)
    random.shuffle(card_list)
    print(card_list)
    #random.shuffle(deck_dict.items())
    #print(sorted_deck)


    p1 = []; p2 = []
    p1_ctr = 0; p2_ctr = 0; card_ctr = 0
    while True:
        if len(card_list) == 0:
            if p1_ctr > p2_ctr:
                game_winner = 'Player 1 wins'
            elif p1_ctr < p2_ctr:
                game_winner = 'Player 2 wins'
            else:
                game_winner = 'DRAW'
            print('P1 {} P2 {}: {}'.format(p1_ctr, p2_ctr, game_winner))
            break

        p1_card = card_list.pop()
        p1_value = deck_dict[p1_card]
        
        p2_card = card_list.pop()
        p2_value = deck_dict[p2_card]
        
        if p1_value > p2_value:
            p1_ctr += 1
            win = 'P1'
        elif p1_value < p2_value:
            p2_ctr += 1
            win = 'P2'
        else:
            win = 'WAR!'
        print('{:>3} {:>3} {:<4}'.format(p1_card, p2_card, win))

#---------------------------------------------------------
if __name__ == '__main__':
    main()

