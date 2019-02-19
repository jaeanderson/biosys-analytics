#!/usr/bin/env python3
"""
Author : jranderson
Date   : 2019-02-14
Purpose: Translate DNA/RNA to proteins
"""

import sys
import os
import re
import argparse

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument(
        'positional', metavar='STR', help='DNA/RNA sequence')

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codon translation',
        metavar='FILE',
        type=str,
        required=True,
        default=None)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output filename',
        metavar='FILE',
        type=str,
        default='out.txt')

    return parser.parse_args()
#------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)
#------------------------------------
def die(msg='Something bad happend'):
    """warn() and exit with error """
    warn(msg)
    sys.exit(1)
#------------------------------------
def main():

    args = get_args()
    codons = args.codons
    outfile = args.outfile
    sequence = args.positional.upper()
 
    if not os.path.isfile(codons):
       die('--codons "{}" is not a file'.format(codons))

    if outfile != 'out.txt':
           outfile = outfile

    codon_dict = {}
    codon_length = 3
    for line in open(codons):
       codon, protein = line.split()
       codon_dict[codon] = protein

    protein_translate = ''
    sequence_codon = []
    out_fh = open(outfile,'wt')

    for i in range(0, len(sequence), codon_length):
        sequence_codon = sequence[i:i+codon_length]
        if codon_dict.get(sequence_codon) != None:
            protein_translate += codon_dict[sequence_codon]
        else:
            protein_translate += '-'

    out_fh.write(protein_translate + '\n')
    print('Output written to "{}"'.format(outfile))
    out_fh.close()

#------------------------------------
if __name__ == '__main__':
     main()
