#!/usr/bin/env python3
"""
Name: jranderson
Date: 04.15.19
Purpose: De Bruijn Graphs in Python 
"""

import argparse
import logging
import os
import sys
from Bio import SeqIO

#---------------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
      description='Graph through sequences',
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
      'fasta',
      help='FASTA file',
      metavar='str')

    parser.add_argument(
      '-k',
      '--overlap',
      help='K size of overlap',
      metavar='int',
      default=3)

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
    fastafile = args.fasta
    overlap = int(args.overlap)

    #print(type(args.overlap))

    if not os.path.isfile(fastafile):
        die('"{}" is not a file'.format(fastafile))

    #if not overlap.isdigit(): 
    #    die('-k "{}" must be a positive integer'.format(overlap))

    if overlap < 1:
        die('-k "{}" must be a positive integer'.format(overlap))

    head_kmers = dict()
    tail_kmers = dict()
    kmer_match = []

    for i, record in enumerate(SeqIO.parse(fastafile, 'fasta'), start=1):
        #print(i, record.id, record.seq)
        kmers = find_kmers(s1=record.seq, k=overlap)
        head_kmers[record.id]=kmers[0] 
        tail_kmers[record.id]=kmers[-1]


    for hkmers in head_kmers.items():
        for tkmers in tail_kmers.items():
            #print(hkmers[0], tkmers[0])
            if hkmers[0] != tkmers[0] and hkmers[1] == tkmers[1]:
                print('{} {}'.format(tkmers[0], hkmers[0]))
                i#kmer_match.append((tkmers[0], hkmers[0]))           

    #print(sorted(kmer_match))
    #print('{}\n{}'.format(head_kmers, tail_kmers))
        

#---------------------------------------------------------
def find_kmers(s1, k):

    if len(s1) < k:
        print('length of sequence less than k-mer length')

    kmer_list = []
    num_kmers = len(s1) - k + 1

    for kmer in [s1[i:i+k] for i in range(0, num_kmers)]:
        kmer_list.append(kmer)

    return kmer_list
#---------------------------------------------------------
if __name__ == '__main__':
    main()
