"""
Mallory5: adversary for TwoTP
"""

def plaintexts():
    return ("0000","0010")

def guess(y):
    if y[0]==y[2]:
        bm = 0
    else:
        bm = 1
    return bm
