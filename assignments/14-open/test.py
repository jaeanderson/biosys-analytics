#!/usr/bin/env python3
"""tests for unlucky13.py"""

from subprocess import getstatusoutput

prg = './unlucky13.py'
luckynums1 = './luckynums1.txt'
luckynums2 = './luckynums2.txt'
luckynums3 = './luckynums3.txt'


def test_usage():
    rv, out = getstatusoutput('{}'.format(prg))
    assert rv != 0
    assert out.lower().startswith('usage')

def test_bad_input():
    """bad input"""
    (retval, out) = getstatusoutput('{} {}'.format(prg, 'foo'))
    assert retval > 0
    assert out == '"foo" is not a file'

def test_runs_ok():
    rv1, out1 = getstatusoutput('{} {}'.format(prg, luckynums1))
    assert rv1 == 0
    assert out1 == 'lucky sum: 6\nlucky sum: 3\nlucky sum: 2\nlucky sum: 1\nlucky sum: 6'.format(prg)

    rv2, out2 = getstatusoutput('{} {}'.format(prg, luckynums2))
    assert rv2 == 0
    assert out2 == 'lucky sum: 0\nlucky sum: 0\nlucky sum: 0'.format(prg)

    rv3, out3 = getstatusoutput('{} {}'.format(prg, luckynums3))
    assert rv3 == 0
    assert out3 == 'lucky sum: 3\nlucky sum: 6\nlucky sum: 4'.format(prg)
