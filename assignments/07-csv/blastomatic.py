#!/usr/bin/env python3
"""
NAME: jranderson
DATE: 03-01-19
PURPOSE: Python CSV Parsing
"""

import argparse
import sys
import csv
import os
import re
from collections import defaultdict

# --------------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
      description='Annotate BLAST output',
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
      'blast_output',
      help='BLAST output (-outfmt 6)', metavar='FILE')

    parser.add_argument(
      '-a',
      '--annotations',
      help='Annotation file',
      metavar='FILE',
      type=str,
      default='')

    parser.add_argument(
      '-o',
      '--outfile',
      help='Output file',
      metavar='FILE',
      type=str,
      default='')

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
    """Let the coding begin!"""

    args = get_args()
    blastfile = args.blast_output
    annotations = args.annotations
    outfile = args.outfile

    blast_headers = 'qseqid sseqid pident length mismtch gapopen qstrt qend sstrt send evalue bitscore'.split()

#    anno_headers = 'centroid domain kingdom phylum class order genus species'.split()

    if not os.path.isfile(blastfile):
        die('"{}" is not a file'.format(blastfile))

    if not os.path.isfile(annotations):
        die('"{}" is not a file'.format(annotations))

    anno_dict = {}; anno_list = []
    with open(annotations, 'r') as afile:
        anno_reader = csv.DictReader(afile, delimiter=',')
        for anno_row in anno_reader:
            centroid = anno_row['centroid']
            genus = anno_row['genus'] or 'NA'
            species = anno_row['species'] or 'NA'
            anno_list = [genus, species]
            anno_dict[centroid] = anno_list
    afile.close()

    match_dict = {};  match_list = []
    with open(blastfile, 'r') as bfile:
        blast_reader = csv.reader(bfile, delimiter='\t')
        for bline in blast_reader:
            blastrow = dict(zip(blast_headers, bline))
            sseqid = blastrow['sseqid']
            pident = float(blastrow['pident'])
            if sseqid in anno_dict:
                anno_values = anno_dict.get(sseqid)
                g = anno_values[0]
                s = anno_values[1]
                match_dict = {'seq':sseqid, 'pid':pident, 'genus':g, 'species':s}
                match_list.append(match_dict)
            else:               
                print('Cannot find seq "{}" in lookup'.format(sseqid), file=sys.stderr)
    bfile.close()

    output_matches(filename=outfile, mlist=match_list)

#---------------------------------------------------------
def output_matches(filename, mlist):

    output_headers = 'seq_id pident genus species'.split()
    sorted_mlist = sorted(mlist, key=lambda x: x['pid'], reverse=True)

    if filename != '':
        sys.stdout = open(filename, 'w')

    sys.stdout.write('\t'.join(output_headers) + '\n')
    for matches in sorted_mlist:
        sys.stdout.write('{}\t{}\t{}\t{}\n'.format(matches.get('seq'), matches.get('pid'), matches.get('genus'), matches.get('species'))) 
    sys.stdout.close()
#---------------------------------------------------------
if __name__=='__main__':
    main()
