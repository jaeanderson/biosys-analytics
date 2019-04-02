#!/usr/bin/env python3
"""
Name: jranderson
Date: 03.30.19
Purpose: Regular Expression Date Parsing 
"""

import os
import re
import sys

#---------------------------------------------------------
def main():
    """Main Codin!"""

    args = sys.argv[1:]
    #print(args)

    if len(args) != 1:
        print('Usage: {} DATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    input = args[0]
    mth_dict = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6,                       'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}    


    sep = '[-\S*]'
    year = '(?P<year>\d{4})'
    short_year = '(?P<syear>\d{2})'
    month = '(?P<month>\d{1,2})'
    day = '(?:-(?P<day>\d{1,2}?))'
    written_mth = '(?P<mth>Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)'

    #print(written_mth) 

    date_re1 = re.compile('^(?P<year>\d{4})[-](?P<month>\d{1,2})(?:-(?P<day>\d{1,2})?)')
    match1 = date_re1.match(input)
#    print('1: {}'.format(match1))
    
    date_re2 = re.compile('^(?P<year>\d{4})[-/](?P<month>\d{1,2})')
    match2 = date_re2.match(input)
#    print('2: {}'.format(match2))

    date_re3 = re.compile('^(?P<month>\d{1,2})[/](?P<year>\d{2})')
    match3 = date_re3.match(input)
#    print('3: {}'.format(match3))

    #match4 = date_re4.match(input)
    #print('4: {}'.format(match4))

    date_re5 = re.compile(written_mth + '[,-]\s?' + year)
    match5 = date_re5.search(input)
    #print(match5)

    if match1:
        y1 = int(match1.group('year'))
        m1 = int(match1.group('month'))
        d1 = int(match1.group('day'))
        print('{}-{:02d}-{:02d}'.format(y1, m1, d1))
    elif match2: 
        y2 = int(match2.group('year'))
        m2 = int(match2.group('month'))
        print('{}-{:02}-01'.format(y2, m2))
    elif match3:
        m3 = int(match3.group('month'))
        y3 = int(match3.group('year'))
        print('20{:02}-{:02}-01'.format(y3, m3))
    elif match5:
        m5 = match5.group('mth')
        m5_num = int(mth_dict[str(m5[:3])])
        y5 = int(match5.group('year'))
        print('{:4}-{:02}-01'.format(y5, m5_num))
    else:
        print('No match')

    

#---------------------------------------------------------
if __name__ == '__main__':
    main()

