#!/usr/bin/env python3
"""
Name: jranderson
Date: 04.05.19
Purpose: Unclustered Proteins 
"""

import argparse
import os
import re
import sys
from Bio import SeqIO

#---------------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
      description='Find unclustered proteins',
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
      '-c',
      '--cdhit',
      help='Output file from CD-HIT (clustered proteins)',
      metavar='str',
      type=str,
      required=True,
      default=None)

    parser.add_argument(
      '-p',
      '--proteins',
      help='Proteins FASTA',
      metavar='str',
      type=str,
      required=True,
      default=None)

    parser.add_argument(
      '-o',
      '--outfile',
      help='Output file',
      metavar='str',
      type=str,
      default='unclustered.fa')

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
    cdhit = args.cdhit
    proteins = args.proteins
    outfile = args.outfile

    if not os.path.isfile(proteins):
        die('--proteins "{}" is not a file'.format(proteins))
    
    if not os.path.isfile(cdhit):
        die('--cdhit "{}" is not a file'.format(cdhit))

    outfile if outfile == '' else outfile

    cdhit_list = []
    cdhit_re = '[|](?P<gi>\d+)[|]'
    
    for line in open(cdhit):
        cd_match = re.search(cdhit_re, line)
        if cd_match:
            cdhit_list.append(cd_match.group('gi')) 
    clustered_proteins = set(cdhit_list)

    unclustered_protein_ctr = 0
    out_fh =  open(outfile, 'wt')
    for i, record in enumerate(SeqIO.parse(proteins, 'fasta'), start=1):
        proteinID = re.sub('[|].*', '', record.id)
        if proteinID not in clustered_proteins:
            unclustered_protein_ctr += 1
            SeqIO.write(record, out_fh, 'fasta')            
    out_fh.close()

    print('Wrote {:,} of {:,} unclustered proteins to "{}"'.format(unclustered_protein_ctr, i, outfile))

#---------------------------------------------------------
if __name__ == '__main__':
    main()
