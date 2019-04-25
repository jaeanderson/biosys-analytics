#!/usr/bin/env python3

"""
Name: jranderson
Date: 04.23.19
Purpose: Word Frequencies in Python
"""

import argparse
import os
import sys
import re
from collections import defaultdict, Counter

# ---------------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Print word frequencies",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
      'infiles', 
      help='File input(s)', 
      metavar="FILE",
      nargs='+', 
      type=argparse.FileType('r', encoding='UTF-8'))

    parser.add_argument(
      '-s',
      '--sort',
      help='Sort by word or frequency ',
      metavar='str',
      default='word')

    parser.add_argument(
      '-m',
      '--min',
      help='Minimum count',
      metavar='int',
      default=0)

    return parser.parse_args()

#----------------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)

#----------------------------------------------------------
def die(msg="Something bad happened"):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)

#----------------------------------------------------------
def word_cleaner(s1):
    
    return re.sub('[^a-zA-Z0-9]', '', s1).lower()

#----------------------------------------------------------
def main():
    """Sko-codin!"""

    args = get_args()
    #fh_list = args.infiles
    sort = args.sort
    min_ct = args.min

    wdict = defaultdict(int)
    for fh_handle in args.infiles:
        for line in fh_handle:
            for word in line.split():
                cleanwrd = word_cleaner(s1=word)
                #print(word, cleanwrd)
                if cleanwrd != '':
                    wdict[cleanwrd] += 1 if cleanwrd in wdict else wdict[cleanwrd] + 1


    if sort == 'word':
        for pair in sorted(wdict.items()):
            wrd, wrdct = pair
            if wrdct >= int(min_ct):
                print('{:20} {}'.format(wrd, wrdct))

    elif sort == 'frequency':
        for pair in sorted([(x[1], x[0]) for x in wdict.items()]):
            wrdct, wrd = pair
            if wrdct >= int(min_ct):
                print('{:20} {}'.format(wrd, wrdct))

#    for wrds in sorted_dict.items(): 
#        w, wctr = wrds
#        if wctr >= int(min_ct) or int(min_ct) == 0: 
#            print('{:20} {}'.format(w, wctr))
        

#----------------------------------------------------------
if __name__ == "__main__":
    main()
