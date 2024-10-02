"""
Mallory2: adversary for Shift1Unbal
"""

def plaintexts():
    return ('a','b')

def guess(y):
    if y=='z':
        bm = 0
    else:
        bm = 1
    return bm
