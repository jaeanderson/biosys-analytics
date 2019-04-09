#!/usr/bin/env python3
"""
Name: jranderson
Date: 04.05.19
Purpose: Regex-Passwords 
"""

import argparse
import os
import re
import sys

#---------------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
      description='Regex-Passwords')

    parser.add_argument(
      'password',
      help='Original Password', metavar='PASSWORD')

    parser.add_argument(
      'alternate',
      help='Alternate Password', metavar='ALT')

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
    pwd = args.password
    alt = args.alternate 

    if pwd == '' and alt == '':
        sys.exit(1)

    capltr_pwd = ''.join(pwd[0].upper() + pwd[1:] for pwd in pwd.split())

    char_chk = r'(?P<cchk>/[^ -~\\"\'`\s]/)?'
    #print(char_chk)
    char_chk_re1 = re.compile(char_chk + pwd)
    char_chk_re2 = re.compile(pwd + char_chk)
    #print(char_chk_re1, char_chk_re2)
    match1 = char_chk_re1.search(alt)
    match2 = char_chk_re2.search(alt)
    #match3 = re.match(pwd, alt)

    
    #print(pwd, alt)    
    #print(match1, match2)

    if pwd == alt:
        print('ok')

    elif capltr_pwd == alt: 
        print('ok')

    elif pwd.upper() == alt:
        print('ok')

    elif match1 or match2:
        print('ok')
    
    else:
        print('nah')

#---------------------------------------------------------
if __name__ == '__main__':
    main()
