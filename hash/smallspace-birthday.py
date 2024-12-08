# A small-space birthday attack

import hashlib
import random
import argparse

def truncated_hash(input_hex, bit_length):
    """
    Computes a truncated hash from an input hexadecimal string.
    
    Args:
        input_hex (str): Input hexadecimal string.
        bit_length (int): Number of bits to keep from the hash.
        
    Returns:
        str: Truncated hash as a hexadecimal string.
    """
    # Ensure the input is properly formatted as a hexadecimal string
    input_bytes = bytes.fromhex(input_hex)
    
    # Compute the full SHA-256 hash of the input bytes
    full_hash = hashlib.sha256(input_bytes).hexdigest()
    
    # Convert the full hash to an integer, truncate it, and return as hex
    truncated = int(full_hash, 16) & ((1 << bit_length) - 1)
    return f"{truncated:0{bit_length // 4}x}"  # Convert to zero-padded hexadecimal

def birthday_attack(bit_length, max_attempts, input_length):
    """
    Performs a small-space birthday attack on a hash function.
    
    Args:
        bit_length (int): Bit length of the truncated hash.
        max_attempts (int): Maximum number of attempts to find a collision.
        input_length (int): Length of random input strings.
        
    Returns:
        tuple: A collision pair (x, x') if found, otherwise None.
    """

    # Generate a random input of specified length
    x_init = ''.join(random.choices('0123456789abcdef', k=input_length))
    x0 = x_init
    x1 = x_init
    i = 1

    for _ in range(max_attempts):     
        x0 = truncated_hash(x0, bit_length)
        x1 = truncated_hash(truncated_hash(x1, bit_length), bit_length)

        if x0 == x1:
            break
        i += 1

    print(f"x0 = x1 found after {i} attempts (out of {max_attempts}).")
    
    x1 = x0
    x0 = x_init

    # Check for a collision
    for j in range(1, i+1):
        h0 = truncated_hash(x0, bit_length)
        h1 = truncated_hash(x1, bit_length)
        if h0 == h1:
            return x0, x1

        x0 = truncated_hash(x0, bit_length)
        x1 = truncated_hash(x1, bit_length)

    return None  # No collision found within max_attempts

if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Birthday attack on a hash function.")
    parser.add_argument("-b", "--bit-length",   type=int, default=40,      help="Number of bits for the truncated hash (default: 24).")
    parser.add_argument("-a", "--attempts",     type=int, default=1200000, help="Number of attempts to find a collision (default: 100000).")
    parser.add_argument("-l", "--input-length", type=int, default=10,      help="Length of random input strings (default: 10).")
    
    args = parser.parse_args()
    bit_length = args.bit_length
    max_attempts = args.attempts
    input_length = args.input_length
    
    print(f"Attempting a birthday attack on a {bit_length}-bit hash...")
    print(f"Using {max_attempts} attempts with random strings of length {input_length}.")

    collision = birthday_attack(bit_length, max_attempts, input_length)
    if collision:
        print(f"Collision found!\nString 1: {collision[0]}\nString 2: {collision[1]}")
        # Directly use the result of `truncated_hash` since it's already a hexadecimal string
        print(f"Hash: {truncated_hash(collision[0], bit_length)}")
    else:
        print("No collision found within the attempt limit.")
