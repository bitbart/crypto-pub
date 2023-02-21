"""
Mallory0: random guess
"""

import random

def plaintexts():
	return ("a","b")

# E_25(a) = "z"

def guess(y):
	if y=='z':
		bm = 0
	else:
		bm = 1
		
	# bm = random.randint(0,1)
	return bm
