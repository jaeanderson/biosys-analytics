#!/usr/bin/env python3
"""cat command in python"""

import sys
import os

def main():
    """main"""
    args = sys.argv

    if len(args) == 1:
        arg1 = os.path.basename(args[0])
        print('Usage: {} FILE'.format(arg1))
        sys.exit(1)

    infile = sys.argv[1]

    if not os.path.isfile(infile):
        print('{} is not a file'.format(infile))
        sys.exit(1)

    for i,line in enumerate(open(infile).read().splitlines(), 1):
        print ('{:5}: {}'.format(i,line))
     
main()
