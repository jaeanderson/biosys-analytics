#!/usr/bin/env python3
"""
Name: jranderson
Date: 03.17.19
Purpose: SwissProt to FASTA 
"""

import argparse
import os
import re
import sys
from Bio import SeqIO

# --------------------------------------------------------
def get_args():
    """get command-line arguments"""

    parser = argparse.ArgumentParser(
      description='Filter Swissprot file for keywords, taxa',
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
      'unifile',
      help='Uniprot file',
      metavar='FILE')

    parser.add_argument(
      '-s',
      '--skip',
      help='Skip taxa',
      nargs='+',
      metavar='STR',
      type=str,
      default='')

    parser.add_argument(
      '-k',
      '--keyword',
      help='Take on keyword',
      metavar='STR',
      required=True,
      default=None)

    parser.add_argument(
      '-o',
      '--output',
      help='Output filename',
      metavar='FILE',
      default='out.fa')

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
    """Let's get ready to code!"""

    args = get_args()
    unifile = args.unifile
    skip_taxa = list(map(lambda x:x.lower(), sorted(args.skip)))
    keyword = args.keyword.lower()
    output = args.output

    if not os.path.isfile(unifile):
        die('"{}" is not a file'.format(unifile))  

    if output != 'out.fa':
        output = output
  
    match_list = []
    rec_ctr = 0; took_ctr = 0

    print('Processing "{}"'.format(unifile))
    uni_fh = open(unifile, 'r')
    for i, unirecord in enumerate(SeqIO.parse(uni_fh, 'swiss'), start=1):
        kw_list = list(map(lambda x:x.lower(), sorted(unirecord.annotations['keywords'])))
        taxonomy = list(map(lambda x:x.lower(), sorted(unirecord.annotations['taxonomy'])))
        rec_ctr += 1
        for kw in kw_list:
            match = re.match((keyword), kw)
            if match:
                if set(skip_taxa).intersection(set(taxonomy)) == set():
                    took_ctr += 1 
                    match_list.append(unirecord)
    out_fh = open(output, 'w')
    SeqIO.write(match_list, out_fh, 'fasta')

    num_skipped = rec_ctr - took_ctr
    print('Done, skipped {} and took {}. See output in "{}".'.format(num_skipped, took_ctr, output))

#---------------------------------------------------------
if __name__ == '__main__':
    main()
