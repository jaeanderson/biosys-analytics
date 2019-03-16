#!/usr/bin/env python3
"""
Name: jranderson
Date: 03.16.19
Purpose: bottles of beers 
"""

import argparse
import os
import re
import sys

# --------------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
    description='Bottles of beer song',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
     '-n',
     '--num_bottles',
     help='How many bottles',
     metavar='INT',
     type=int,
     default=10)

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
    """Let's get ready to code!"""

    args = get_args()
    num_bottles = args.num_bottles

    if num_bottles < 1:
      die('N ({}) must be a positive integer'.format(num_bottles))

    for nbottles in range (num_bottles, 0, -1):

        print('{} bottle{} of beer on the wall,'.format(nbottles, '' if nbottles == 1 else 's'))
        print('{} bottle{} of beer,'.format(nbottles, '' if nbottles == 1 else 's'))
        print('Take one down, pass it around,')
        nbottles = nbottles - 1
        print('{} bottle{} of beer on the wall!{}'.format(nbottles, '' if nbottles == 1 else 's', '' if nbottles == 0 else '\n')) 

#---------------------------------------------------------
if __name__=='__main__':
    main()
