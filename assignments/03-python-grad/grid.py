#!/usr/bin/env python3
"""grid in python"""

import sys
import os

def main():
    """main"""
    
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} NUM'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    gridsize = int(args[0])
    grid = []
    
    if gridsize in range(2, 10):
        for i in range(1, gridsize **2 + 1):
            grid.append(i)
            if i % (gridsize) == 0:
                print ('{:3}\n'.format(i), end = '')
            else:
                print ('{:3}'.format(i), end = '')
    else:
        print('NUM ({}) must be between 1 and 9'.format(gridsize))
        sys.exit(1)    

main()
