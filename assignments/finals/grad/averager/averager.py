#!/usr/bin/env python3

"""
Name: jranderson
Date: 05.07.19
Purpose: Find Common Words with Mismatches
"""

import argparse
import os
import sys
import io
import re
import logging

#----------------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Average all the numbers in a document",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
      'infiles', 
      help='Input files', 
      metavar="FILE",
      nargs='+') 
      #type=argparse.FileType('r', encoding='UTF-8'))


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
def main():
    """Skoo-codin!"""

    args = get_args()

    for infile in args.infiles: 
        if not os.path.isfile(infile):
            print('"{}" is not a file'.format(infile), file=sys.stderr)
        else:
            avg = 0; mtch_ctr = 0; sum_nums = 0
            #avg_list = []

            fh = open(infile, 'r')
            find_num_re = re.compile('^[+-]?[0-9]\d*(\.\d+)?')
            for word in fh.read().split():
                match = re.match(find_num_re, word)
                if match:
                    mtch_ctr += 1
                    sum_nums += float(match.group(0))
            if mtch_ctr == 0:
                avg = 0
            else:
                avg = sum_nums / mtch_ctr    
            print('{:10.02f}: {}'.format(avg, os.path.basename(infile)))

#---------------------------------------------------------- 
if __name__ == "__main__":
    main()
