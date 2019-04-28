#!/usr/bin/env python3

"""
Name: jranderson
Date: 04.26.19
Purpose: Find Common Words with Mismatches
"""

import argparse
import os
import sys
import io
import re
import logging
#from tabulate import tabulate

#----------------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Find Common Words",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
      'infiles', 
      help='Input files', 
      metavar="FILE",
      nargs=2, 
      type=argparse.FileType('r', encoding='UTF-8'))

    parser.add_argument(
      '-m',
      '--min_len',
      help='Minimu length of wordss',
      metavar='int',
      default=0)

    parser.add_argument(
      '-n',
      '--hamming_distance',
      help='Allowed Hamming distance',
      metavar='int',
      default=0)

    parser.add_argument(
      '-l',
      '--logfile',
      help='Logfile',
      metavar='str',
      default='.log')

    parser.add_argument(
      '-d',
      '--debug',
      help='Debug',
      action='store_true')

    parser.add_argument(
      '-t',
      '--table',
      help='Table output',
      action='store_true')

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

#---------------------------------------------------------
def dist(s1, s2):
    """Determine hamming distance"""

    hamm_diff = 0; len_diff = 0

    if len(s1) != len(s2):
        len_diff = abs(len(s1) - len(s2))  

    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            hamm_diff += 1

    return hamm_diff + len_diff

#---------------------------------------------------------
def test_dist():
    """dist ok"""

    tests = [('foo', 'boo', 1), ('foo', 'faa', 2), ('foo', 'foobar', 3),
             ('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC',
              9), ('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC', 10)]

    for s1, s2, n in tests:
        d = dist(s1, s2)
        assert d == n

#----------------------------------------------------------
def word_cleaner(s1):
    """Removes punction attached to words"""

    return re.sub('[^a-zA-Z0-9]', '', s1).lower()

#---------------------------------------------------------
def uniq_words(f, mlen):
    """Finds words in file with minimum length"""

    uniq_list = []

    for line in f:
        for word in line.split():
            clean_wrd = word_cleaner(word)
            if len(clean_wrd) >= int(mlen) and clean_wrd != '':
                uniq_list.append(clean_wrd)

    return set(sorted(uniq_list))

#----------------------------------------------------------
def test_uniq_words():
    """Test uniq_words"""

    s1 = '?foo, "bar", FOO: $fa,'
    s2 = '%Apple.; -Pear. ; baNAna!!!'

    assert uniq_words(io.StringIO(s1), 0) == set(['foo', 'bar', 'fa'])
    assert uniq_words(io.StringIO(s1), 3) == set(['foo', 'bar'])
    assert uniq_words(io.StringIO(s2), 0) == set(['apple', 'pear', 'banana'])
    assert uniq_words(io.StringIO(s2), 4) == set(['apple', 'pear', 'banana'])
    assert uniq_words(io.StringIO(s2), 5) == set(['apple', 'banana'])

#----------------------------------------------------------
def common(w1, w2, maxd):
    """Finds and returns common words between two lists and ham distance"""

    common_list = []
    for wrd1 in w1:
        for wrd2 in w2:
            if wrd1 == wrd2:
                #ham_dist = dist(s1=wrd1, s2=wrd2)
                common_list.append((wrd1, wrd2, dist(s1=wrd1, s2=wrd2)))
                #print(word1, word2, ham_dist)

    return sorted(common_list)

#----------------------------------------------------------
def test_common():
    """Test common words"""

    w1 = ['foo', 'bar', 'quux']
    w2 = ['bar', 'baz', 'faa']

    assert common(w1, w2, 0) == [('bar', 'bar', 0)]
    assert common(w1, w2, 1) == [('bar', 'bar', 0), ('bar', 'baz', 1)]
    assert common(w1, w2, 2) == [('bar', 'bar', 0), ('bar', 'baz', 1),
                                 ('bar', 'faa', 2), ('foo', 'faa', 2)]

    return 0

#----------------------------------------------------------
def print_table(cwlist, fmt):
    """Prints common words in PSQL table format"""
    
    #print(tabulate(cw_list, headers=['word1','word2','distance'], tablefmt=fmt))
    return 0
#----------------------------------------------------------
def main():
    """Sko-codin!"""

    args = get_args()
    min_len = args.min_len
    max_ham_dist = args.hamming_distance
    logfile = args.logfile
    debug = args.debug
    table = args.table

    if int(max_ham_dist) < 0:
        die('--distance "{}" must be > 0'.format(max_ham_dist))

    fh1 = args.infiles[0]
    fh2 = args.infiles[1]

    words1 = uniq_words(f=fh1, mlen=min_len)
    words2 = uniq_words(f=fh2, mlen=min_len)
    common_words = common(w1=words1, w2=words2, maxd=max_ham_dist)

    if len(common_words) == 0:
        print('No words in common.')
    

    if table:
        print('table output')
        print_table(cwlist=common_words, fmt='psql')
    else:
        print(common_words)
        print_table(cwlist=common_words, fmt='simple')        


#----------------------------------------------------------
if __name__ == "__main__":
    main()

