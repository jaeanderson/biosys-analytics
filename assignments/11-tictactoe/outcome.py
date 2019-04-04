#!/usr/bin/env python3
"""
Name: jranderson
Date: 04.02.19
Purpose: Tic-Tac-Toe Outcome-Regex 
"""

import os
import re
import sys

#---------------------------------------------------------
def main():
    """Sko-Codin!"""

    args = sys.argv[1:]
    
    if len(args) != 1:
        print('Usage: {} STATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    state = args[0].upper()

    win_dict = {'XXX......':'X', 'OOO......':'O', '...XXX...':'X',
                '...OOO...':'O', '......XXX':'X', '......OOO':'O', 
                'X..X..X..':'X', 'O..O..O..':'O', '.X..X..X.':'X', 
                '.O..O..O.':'O', '..X..X..X':'X', '..O..O..O':'O', 
                'X...X...X':'X', 'O...O...O':'O', '..X.X.X..':'X', 
                '..O.O.O..':'O'}

    instate_re = re.compile('^[.XO]{9}')
    good_input = instate_re.match(state)

    win_sublist = []
    if good_input:
        win1 = re.compile('(?P<win1>XXX|OOO)')
        w1 = win1.search(state)
        #print(w1)

        win2 = re.compile('(?P<win2>[X](?:[\.O]){1,2}[X](?:[\.O]){1,2}[X]|[O](?:[\.X]){1,2}[O](?:[\.X]){1,2}[O])') 
        w2 = win2.search(state)
        #print(w2)
 

        for move, winner in win_dict.items():
            match = re.fullmatch(move, state)
            if match:
                print('{} has won'.format(winner))
                sys.exit(1)
        print('No winner')
 
        #if w1:
        #    for move1, winner1 in win_dict.items():
                #s = ''
                #for i in range(w1.span()[0], w1.span()[1]):
                #    s += move1[i]
                
                #print(s, str(w1.group('win1')))
                 
        #        match = re.fullmatch(move1, state)
                #print(move1, match)
                #if s == str(w1.group('win1')):
         #       if match:
          #          print('{} has won'.format(winner1))
    
        #elif w2:  
            #sub_state = re.sub('[O]{1}', '.', str(w2.group('win2')))
            #print(sub_state)

            #xcount = (str(w2.group('win2'))).count('X')
            #ycount = (str(w2.group('win2'))).count('O')
            
            #print('x: {}  o: {}'.format(xcount, ycount))

            #if xcount > ycount:
            #    sub_state = re.sub('[O]{1,2}', '.', str(w2.group('win2')))
            #else:
            #    sub_state = re.sub('[X]{1,2}', '.', str(w2.group('win2')))

         #   for move2, winner2 in win_dict.items(): 
                #ss = ''
                #for i in range(w2.span()[0], w2.span()[1]):
                #    ss += move2[i]
                #print(ss, str(w2.group('win2')))
                
        #        match2 = re.fullmatch(move2, state)
                #print(move2, match2)
        #        if match2:
        #            print('{} has won'.format(winner2))
 
        #else:
        #    print('No winner') 

    else:
        print('State "{}" must be 9 characters of only ., X, O'.format(state))

#---------------------------------------------------------
if __name__ == '__main__':
    main()
