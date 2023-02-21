"""
Mallory7: adversary for ShiftLazyOTP
"""

def plaintexts():
    return ("aaaaaa","aaaaab")

def guess(y):
    if y[5]=="a":
        bm = 0
    else:
        bm = 1
    return bm
