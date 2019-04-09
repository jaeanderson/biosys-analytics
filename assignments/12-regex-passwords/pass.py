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
      'alt',
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
    alt = args.alt 

    capltr_pwd = ''.join(pwd[0].upper() + pwd[1:] for pwd in pwd.split())
    #print(capltr_pwd)
    #capltr_re = re.compile('^(?P<capltr>([A-Z]{1})([a-z]+))$')
    #match2 = capltr_re.match(alt) 
    #charchk_re = re.compile(r'(?P<charchk>([^\w\s]{1})?' + alt + '([^\w\s]{1})?)?')
    #match4 = charchk_re.search(alt)
    match = re.search(pwd, alt)

    #print(pwd, alt)   
 
    if pwd == alt:
        #print('match1 exactly ok')
        print('ok')

    elif capltr_pwd == alt: 
        #print('match2 upper 1st letter ok')
        #tmp_pwd = ''.join(pwd[0].upper() + pwd[1:] for pwd in pwd.split())
        #print(tmp_pwd, str(match2.group('capltr')))

        #if tmp_pwd == str(match2.group('capltr')):
        #    print('ok')
        #else:
        #    print('nah')
        #print(pwd, alt)
        print('ok')

    elif pwd.upper() == alt:
        #print('match 3 all uppercase ok')
        print('ok')

    elif match:
        #print('match4 ok {}'.format(match4)) 
        #print(str(match4.group('charchk')))
        #temp_alt = ' '.join(alt[0:] for alt in alt.split())
        #if pwd == str(match4.group('charchk')):
            #print(temp_alt, pwd, str(match4.group('charchk')))
        print('ok')
        #else:
        #    print('nah')
        #print(pwd, alt)

    else:
        print('nah')
        #print(pwd, alt)

#---------------------------------------------------------
if __name__ == '__main__':
    main()
