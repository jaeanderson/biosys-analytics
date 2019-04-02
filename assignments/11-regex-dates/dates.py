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


    sep = '[-/,]'
    year = '(?P<year>\d{4})'
    short_year = '(?P<syear>\d{2})'
    month = '(?P<month>\d{1,2})'
    written_mth = '(?P<mth>Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|                    May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?Sep(?:tember)?|Oct(?:                    ober)?|Nov(?:ember)?|Dec(?:ember)?)'

    day = '(?P<day>\d{1,2})'
    

    date_re1 = re.compile(year + month + day)
    date_re2 = re.compile(year + sep + month + sep + day)

    date_re3 = re.compile(month + sep + short_year)
    date_re4 = re.compile(year + sep + month)
    #date_re4 = re.compile('^[^/]*')

    date_re5 = re.compile(written_mth + sep + '?\s' + year)

    match1 = date_re1.match(input) or date_re2.match(input) 
    match3 = date_re3.match(input)
    match4 = date_re4.match(input)
    #print(match4)
    match5 = date_re5.search(input)

    #print(match1)

    if match1:
        y1 = int(match1.group('year'))
        m1 = int(match1.group('month'))
        d1 = int(match1.group('day'))
        print('{:4}-{:02}-{:02}'.format(y1, m1, d1)) 
    elif match3: 
        y3 = int(match3.group('syear'))
        m3 = int(match3.group('month'))
        print('20{:02}-{:02}-01'.format(y3, m3))
    elif match4:
        y4 = int(match4.group('year'))
        m4 = int(match4.group('month'))
        #d4 = int(match4.group('day'))
        print('{}-{:02}-01'.format(y4, m4))
    elif match5:
        y5 = int(match5.group('year'))
        m5 = match5.group('mth')
        m5_num = int(mth_dict[str(m5[:3])])
        print('{:4}-{:02}-01'.format(y5, m5_num))
    else:
        print('No match')

    

#---------------------------------------------------------
if __name__ == '__main__':
    main()

