#!/usr/bin/env python3
"""head command in python"""

import sys
import os

def main():
    """main"""
    
    args = sys.argv[1:]

    if len(args) == 0 or len(args) > 2:
        scriptname = os.path.basename(sys.argv[0])
        print('Usage: {} FILE [NUM_LINES]'.format(scriptname))
        sys.exit(1)

    if len(args) == 1:
        headnum = 3
    else:
        headnum = int(args[1])
        if headnum <= 0:
            print ('lines ({}) must be a positive number'.format(headnum))
            sys.exit(1)

    infile = args[0]   

    if not os.path.isfile(infile):
        print('{} is not a file'.format(infile))
        sys.exit(1)

    for i, line in enumerate(open(infile).read().splitlines(), 1):
        if ( i <= headnum):
            print('{}'.format(line))
    
main()
