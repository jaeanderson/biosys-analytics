#!/usr/bin/env python3
"""
Name: jranderson
Date: 04.13.19
Purpose: Hamming Distance 
"""

import argparse
import logging
import os
import sys

#---------------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
      description='Hamming distance',
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
      'file',
      help='File inputs', 
      nargs=2,
      metavar='FILE')

    parser.add_argument(
      '-d',
      '--debug',
      help='Debug',
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
    """Sko-Codin!"""

    args = get_args()
    infile1 = args.file[0]
    infile2 = args.file[1]
    debug = args.debug

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    logging.debug('file1 = {}, file2 = {}'.format(infile1, infile2))

    if not os.path.isfile(infile1):
        die('"{}" is not a file'.format(infile1))

    if not os.path.isfile(infile2):
        die('"{}" is not a file'.format(infile2)) 

    num_edits = 0

    #if infile1 == infile2:
    #    print(num_edits)

    f1 = open(infile1).read().split()
    f2 = open(infile2).read().split()

    text = zip(f1, f2)
#    print(list(text))
    
#    for i, word in enumerate(text):
#        print(word[i])

    hamm_dist = 0; total_diff = 0
    for i, f1_word in enumerate(f1):
        #print(i, f1_word, f2_lines[i])
        hamm_dist = dist(s1=f1_word, s2=f2[i])
        logging.debug('s1 = {}, s2 = {}, d = {}'.format(f1_word, f2[i], hamm_dist))
        total_diff += hamm_dist
    print(total_diff)

#---------------------------------------------------------
def dist(s1, s2):
    #char_ctr = 0; len_ctr = 0
    dist_diff = 0; len_diff = 0

#    print(s1, s2)
    if len(s1) != len(s2):
        len_diff = abs(len(s1) - len(s2))  

    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            dist_diff += 1
#        print(char1, char2, dist_diff)

    return dist_diff + len_diff
#---------------------------------------------------------
def test_dist():
    """dist ok"""
    tests = [('foo','faa', 1), ('foo','faa', 2), ('foo','foobar', 3),
            ('TAGGGCAATCATCCGAG','ACCGTCAGTAATGCTAC', 9),
            ('TAGGGCAATCATCCGG','ACCGTCAGTAATGCTAC', 10)]

    for s1, s2, n in tests:
        d = dist(s1, s2)
        assert d == n

#---------------------------------------------------------
if __name__ == '__main__':
    main()
