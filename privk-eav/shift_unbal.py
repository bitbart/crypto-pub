### Shift cipher in with non-uniform keys and plaintexts of length 1

import sys
import secrets

def int_of_chr(n):
    return ord(n)-ord('a')

def chr_of_int(n):
    return chr(n + ord('a'))
    
def gen():
    a = secrets.choice([0,1])
    if a==0:
        k=25
    else:
        k = secrets.randbelow(25)
    return k

def enc(x,k):
    assert(len(x)==1),"Plaintext must have length 1"
    return  ''.join(map(lambda n : chr_of_int((int_of_chr(n) + k)%26), x))

def dec(y,k):
    assert(len(x)==1),"Ciphertext must have length 1"    
    return  ''.join(map(lambda n : chr_of_int((int_of_chr(n) - k)%26), y))



def main(args):  
    if len(args) < 2:
        print("""\
        Usage:
        shift_ecb -gen keyfile    generates a key and writes it to file
        shift_ecb -enc keyfile x  encrypts plaintext x with key (in ECB mode)
        shift_ecb -dec keyfile y  decrypts ciphertext y with key (in ECB mode)
        """)
        sys.exit(0)

    if args[0] == "-gen":
        # print("Generating key...")
        k = gen()
        with open(args[1], 'w') as f:
            f.write(str(k) + "\n")
            print(k)

    elif args[0] == "-enc":
        # print("Encrypting " + args[2] + " with key in " + args[1] + "...")
        with open(args[1], 'r') as f:
            k = int(f.read())
            y = enc(args[2],k)
            print(y)

    elif args[0] == "-dec":
        # print("Decrypting " + args[2] + " with key in " + args[1] + "...")
        with open(args[1], 'r') as f:
            k = int(f.read())
            x = dec(args[2],k)
            print(x)

if __name__ == '__main__':
    main(sys.argv[1:])
