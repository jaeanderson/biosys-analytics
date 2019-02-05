#!/usr/bin/env python3
"""vowel counter in python"""

import sys
import os

def main():
    """main"""
    args = sys.argv

    if len(args) == 1 or len(args) > 2:
        scriptname=os.path.basename(args[0])
        print('Usage: {} STRING'.format(scriptname))
        sys.exit(1)

    vowel_ctr = 0
    str_arg = args[1]
    for vowel in str.lower(str_arg):
        if vowel in "aeiou":
            vowel_ctr = vowel_ctr + 1

    if vowel_ctr ==1:
        print('There is {} vowel in "{}."'.format(vowel_ctr, str_arg))
    else:    
        print('There are {} vowels in "{}."'.format(vowel_ctr, str_arg))
        
main()
