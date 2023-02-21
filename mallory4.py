"""
Mallory4: adversary for OTPlastXor
"""

def plaintexts():
    return ("000","001")

def guess(y):
    n = 0
    for bi in y[:-1]:
        n = n ^ int(bi)
    if n==int(y[2]):
        bm = 0
    else:
        bm = 1
    return bm
