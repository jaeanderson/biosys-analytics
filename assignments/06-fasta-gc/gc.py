#!/usr/bin/env python3

"""
Name:     jranderson
Date:     2019-02-22
Purpose:  Fasta- GC
"""

import argparse
import sys
import os
from Bio import SeqIO


# --------------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
      description='Segregate FASTA sequences by GC content',
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
      'fasta', 
      help='Input FASTA file(s)', nargs='+', metavar='FASTA')

    parser.add_argument(
      '-o',
      '--outdir',
      help='Output directory',
      metavar='str',
      type=str,
      default='out'
    )

    parser.add_argument(
      '-p',
      '--pct_gc',
      help='Dividing line for percent GC',       
      metavar='int',
      type=int,
      default=50)

    return parser.parse_args()
# -------------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)
#--------------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
#--------------------------------------------------------
def main():
    """Let the coding begin!"""

    args =  get_args()
    fastalist = args.fasta
    gc_pct = args.pct_gc
    outdir = args.outdir

    high_seq_flag = 0
    num_seqs_written = 0

    if gc_pct not in range(0, 101):
        die('--pct_gc "{}" must be between 0 and 100'.format(gc_pct))
        sys.exit(1)

    for i, fastafile in enumerate(fastalist, start=1):
        if not os.path.isfile(fastafile):
            die('"{}" is not a file'.format(fastafile))
        else:         
            high_seqs = []
            low_seqs = []
            gc_ctr = 0
  
            print('{:3d}: {}'.format(i, os.path.basename(fastafile)))
            for record in SeqIO.parse(fastafile, 'fasta'):
                for letter in record.seq:
                    if letter in 'cCgG':
                        gc_ctr += 1
            
                gc_calc = int((gc_ctr / len(record.seq)) * 100)
                if gc_calc >= gc_pct:
                    high_seq_flag = 1
                    high_seqs.append(record)
                    num_seqs_written += process(file=fastafile, out_dir=outdir, seqs_per_file=high_seqs, seq_flag=high_seq_flag)
                else:
                    high_seq_flag = 0
                    low_seqs.append(record)
                    num_seqs_written += process(file=fastafile, out_dir=outdir, seqs_per_file=low_seqs, seq_flag=high_seq_flag)
                gc_ctr = 0
   
    die('Done, wrote {} sequences to out dir "{}"'.format(num_seqs_written, outdir))

#--------------------------------------------------------
def process (file, out_dir, seqs_per_file, seq_flag):

    basename, ext = os.path.splitext(os.path.basename(file))

    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    
    if seq_flag == 1:
        outfile = os.path.join(out_dir, basename + '_high' + ext)
    else:
        outfile = os.path.join(out_dir, basename + '_low' + ext)    
    out_fh = open(outfile, 'wt') 
    SeqIO.write(seqs_per_file, out_fh, 'fasta')

    return 1
#--------------------------------------------------------
if __name__=='__main__':
    main()
