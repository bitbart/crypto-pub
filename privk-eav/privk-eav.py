#!/usr/bin/env python

import sys
import logging
from cipher import *

# choose the adversary
from mallory2 import *

# Adv: mallory1
# P = ShiftECB()

# Adv: mallory2
P = Shift1Unbal()

# Adv: mallory7
# P = ShiftLazyOTP(5)

# Adv: mallory3
# P = Vigenere2Unbal()

# Adv: mallory5
# P = TwoTP(4)

# Adv: mallory6
# P = QuasiOTP(4)

# Adv = mallory4
# P = OTPlastXor(3)

assert (len(sys.argv)==2 and int(sys.argv[1])>0),"Usage: privk-eav n_experiments"

logging.basicConfig(format='%(message)s', filename='log', level=logging.INFO)

S = 0                 # number of experiments where the adversary wins
N = int(sys.argv[1])  # total number of experiments

for i in range(N):
    logging.info("Experiment " + str(i+1))

    # M -> A : x0, x1
    (x0,x1) = plaintexts()
    logging.info("x0 = " + x0)
    logging.info("x1 = " + x1)

    # A -> M : y = Ek(x[b])
    (b,y) = P.exp(x0,x1)
    logging.info("b = " + str(b))   
    logging.info("y = " + y)

    # M : bm   
    bm = guess(y)
    logging.info("bm = " + str(bm))
    
    if bm==b:
        logging.info("PrivK = 1 (Mallory wins)")
        S = S+1
    else:
        logging.info("PrivK = 0 (Mallory loses)")

print("Percentage of success: " + str(S*100./N))
