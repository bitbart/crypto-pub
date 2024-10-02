# Cryptanalysis of the shift cipher in ECB mode

import sys

# encrypts a string x with key k
# note: we use chr, rather than Z26
def encrypt(x, k):
	y = ""
	for xi in x:
		if xi!='\n':
			base = ord('a')
			yi = chr(base + ((ord(xi) - base) + (ord(k) - base)) % 26)
			y = y + yi
	return y

def decrypt(y, k):
	x = ""
	for yi in y:
		base = ord('a')
		xi = chr(base + ((ord(yi) - base) - (ord(k) - base)) % 26)
		x = x + xi
	return x


# constructs a dictionary with english letter frequencies
def freq_monograms():
  print("English letter frequencies:")
  f = open("monograms_en.txt", "r")
  l = f.readlines()
  for s in l:
    (i, p) = s.split()
    freq_en[i] = float(p)
  print(freq_en)


# computes a dictionary containing the indexes of mutual coincidence of x
def mutualCoincidence(x):
  freq_x = {}
  for c in range(ord('a'), ord('z') + 1):
    freq_x[chr(c)] = 0
  for c in x:
    freq_x[c] = freq_x[c] + 1
  #print (freq_x)

  for g in range(ord('a'), ord('z') + 1):
    gC = chr(g)
    M[gC] = 0
    for i in range(ord('a'), ord('z') + 1):
      iC = chr(i)
      # j = i+g % 26
      jC = chr(ord('a') + (i + g - 2 * ord('a')) % 26)
      M[gC] = M[gC] + freq_en[iC] * freq_x[jC]
    M[gC] = M[gC] / len(x)


# Global variables

freq_en = {}
M = {}


def main(args):  
	if len(args) != 4 or args[0] != "-key" or args[2] != "-plaintext":
		print("""\
Usage: python shift.py -key k -plaintext file    
        """)
		sys.exit(0)

	k = args[1]
	freq_monograms()

	filename = args[3]
	# change first argument to choose a different plaintext file
	f = open(filename, "r")
	s = f.readline()

	# remove punctuation from plaintext
	s = s.translate({
	ord(' '): None,
		ord('.'): None,
		ord(','): None,
		ord("'"): None,
		ord('’'): None,
		ord('-'): None
	})

	# lowercase
	x = s.lower()
	print("\nPlaintext:\n" + x)

	# encrypt the plaintext with key k
	y = encrypt(x, k)
	print("Ciphertext:\n" + y)

	# computes the index of mutual coincidence
	mutualCoincidence(y)
	print("\nIndex of mutual coincidence:")
	for (c, Mg) in M.items():
		print(c, Mg)
	print()

	# computes the maximum index of mutual coincidence
	(k, p) = max(M.items(), key=lambda k: k[1])
	
	print("Most likely key", k, "with index of mutual coincidence", p)
	
	print("\nDecrypted text:")
	print(decrypt(y, k))
	
if __name__ == '__main__':
    main(sys.argv[1:])
