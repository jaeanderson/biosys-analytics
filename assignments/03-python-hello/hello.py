#!/usr/bin/env python3
"""hello in python"""

import sys
import os

def main():
    """main"""
    args = sys.argv

    if len(args) == 1:
        arg1 = os.path.basename(args[0])
        print('Usage: {} NAME [NAME2 ...]'.format(arg1))
        sys.exit(1)

    names = args[1:]
    numnames = len(args) - 1
    
    if numnames == 1:
        print('Hello to the {} of you: {}!'.format(numnames, names[0])) 
    elif numnames == 2:
        print('Hello to the {} of you: {} and {}!'.format(numnames, names[0], names[1]))
    else:
        lastname = names.pop(-1)
        print('Hello to the {} of you: {}'.format(numnames, ', '.join(names)) + ', and', lastname + '!')

main()
