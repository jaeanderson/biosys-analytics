#!/usr/bin/env python3
"""
Name: jranderson
Date: 03.20.19
Purpose: Blackjack 
"""

import argparse
import re
import sys
import random
import itertools

# --------------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
      description='Blackjack',
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
      '-s',
      '--seed',
      help='Seed',
      metavar='INT',
      type=int)

    parser.add_argument(
      '-p',
      '--player_hits',
      help='Player boolean flag',
      action='store_true')

    parser.add_argument(
      '-d',
      '--dealer_hits',
      help='Dealer boolean flag',
      action='store_true')

    return parser.parse_args()

#---------------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)

#---------------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)

#---------------------------------------------------------
def main():
    """Let's get ready to code"""

    args = get_args()
    seed = args.seed
    pflg = args.player_hits
    dflg = args.dealer_hits

    suits = ['\u2660', '\u2663', '\u2665', '\u2666']
    card_rank = {'A':1,
                 '2':2,
                 '3':3,
                 '4':4,
                 '5':5,
                 '6':6,
                 '7':7,
                 '8':8,
                 '9':9,
                 '10':10,
                 'J':10,
                 'Q':10,
                 'K':10}                

    c = list(itertools.product(suits, card_rank.keys()))
    d = list(v+s for v, s in c)

    deck = sorted(d)
    random.seed(seed)
    random.shuffle(deck)
    #print(deck)

    plist = []; dlist = []
    plyr_sum = 0; dlr_sum = 0
    pc3 = ''; dc3 = ''

    plist.append(deck.pop(-1))
    dlist.append(deck.pop(-1))
    plist.append(deck.pop(-1))
    dlist.append(deck.pop(-1))

    #pc1, dc1, pc2, dc2 = deck.pop(-1), deck.pop(-1), deck.pop(-1), deck.pop(-1)

    #print(pc1, pc2)
    #print(dc1, dc2)

    if pflg: 
        pc3 = deck.pop(-1)
        plist.append(pc3)
    if dflg:
        dc3 = deck.pop(-1)
        dlist.append(dc3)
 
    pc1, pc2 = plist[0], plist[1]
    dc1, dc2 = dlist[0], dlist[1]
 
    plyr_sum = get_sum(hlist=plist,crdict=card_rank)
    dlr_sum = get_sum(hlist=dlist,crdict=card_rank)

    print('D [{:>2}]: {:<} {}{}'.format(dlr_sum, dc1, dc2, ' '+dc3 if dc3 != '' else ''))
    print('P [{:>2}]: {:<} {}{}'.format(plyr_sum, pc1, pc2, ' '+pc3 if pc3 != '' else ''))

    if plyr_sum > 21:
        print('Player busts! You lose, loser!')
        sys.exit(0)
    if dlr_sum > 21:
        print('Dealer busts.')
        sys.exit(0)
    if plyr_sum == 21:
        print('Player wins. You probably cheated.')
        sys.exit(0)
    if dlr_sum == 21:
        print('Dealer wins!')
        sys.exit(0)
    if dlr_sum < 19:
        print('Dealer should hit.')
    if plyr_sum < 19:
        print('Player should hit.')    

#---------------------------------------------------------
def deal_card(hlist, dlist):
    return hlist.append(dlist.pop(-1))

#---------------------------------------------------------
def get_sum(hlist, crdict):
    sum = 0
    for c in hlist:
        sum += int(crdict[str(c[1:])])
    return sum

#---------------------------------------------------------
if __name__ == '__main__':
    main()
