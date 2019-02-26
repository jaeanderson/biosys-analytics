#!/usr/bin/env python3
"""
Name:     j.r.anderson
Date:     2019-02-22
Purpose:  Python File - First Lines
"""

import argparse
import sys
import re
import os

# --------------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
      description='First Lines',
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
      'directory', 
      help='A directory argument', nargs='+', metavar='DIR')

    parser.add_argument(
      '-w',
      '-width',
      help = 'Integer width argument',
      metavar='int',
      type=int,
      default=50)

    return parser.parse_args()
# --------------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)
#---------------------------------------------------------
def die(msg='Something bad happend'):
    """warn() and exit with error"""
    warn(msg)
#---------------------------------------------------------
def main():
    """Let the coding begin!"""

    args = get_args()
    dirlist = args.directory
    width = args.w

    fline_dict = {}
    filelist = []

    for dirname in dirlist:
        if os.path.isdir(dirname):    
            print(dirname)
            for file in os.listdir(dirname): 
                fname = open(os.getcwd() + '/' + dirname + '/' + file)
                line = fname.readline().rstrip()
                fline_dict[file] = line + ' '
            fname.close()      
      
            pairs = sorted([(x[1], x[0]) for x in fline_dict.items()])
            for firstline, filename in pairs:
                print(firstline.ljust(width-len(filename)+1, '.') + ' ' + filename)
            fline_dict = {}
        else:         
            die('"{}" is not a directory'.format(dirname))         


#--------------------------------------------------------
if __name__=='__main__':
    main()
