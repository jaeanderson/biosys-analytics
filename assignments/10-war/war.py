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

    rank = {1:'A',
            2:'2',
            3:'3',
            4:'4',
            5:'5',
            6:'6',
            7:'7',
            8:'8',
            9:'9',
            10:'10',
            11:'J',
            12:'Q',
            13:'K'}

    #cd = 'A2345678910JQK'
    cdeck = (list(itertools.product(suits, rank.values())))
    #print(sorted(cdeck))
    
    d = list(v+s for v, s in cdeck)
    deck_dict = {}   
    for i, card in enumerate(d):
        vmod = i % 13
        deck_dict[card] = vmod + 1

    
    sorted_deck = sorted(deck_dict.items(), key=lambda kv: kv[1])
    #sorted_deck = sorted(d, key=itemgetter(1))
    #print(deck_dict)
    #print('seed: {}'.format(seed)) 
    random.seed(seed)
    random.shuffle(sorted_deck)
    #random.shuffle(deck_dict.items())
    #print(sorted_deck)


    p1 = []; p2 = []
    p1_ctr = 0; p2_ctr = 0; card_ctr = 0
    while True:
        if len(sorted_deck) == 0:
            if p1_ctr > p2_ctr:
                game_winner = 'Player 1 wins'
            elif p1_ctr < p2_ctr:
                game_winner = 'Player 2 wins'
            else:
                game_winner = 'DRAW'
            print('P1 {} p2 {}: {}'.format(p1_ctr, p2_ctr, game_winner))
            break

        p1 = sorted_deck.pop(0)
        p1_card = p1[0]
        p1_value = p1[0][1]
        
        p2 = sorted_deck.pop(0)
        p2_card = p2[0]
        p2_value = p2[0][1]
        
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

