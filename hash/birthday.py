# A big-space birthday attack

import hashlib
import random
import argparse

def truncated_hash(input_string, bit_length):
    """
    Computes a truncated hash of a string.
    
    Args:
        input_string (str): Input string to hash.
        bit_length (int): Number of bits to keep from the hash.
        
    Returns:
        int: Truncated hash as an integer.
    """
    full_hash = hashlib.sha256(input_string.encode()).hexdigest()
    truncated = int(full_hash, 16) & ((1 << bit_length) - 1)
    return truncated

def birthday_attack(bit_length, max_attempts, input_length):
    """
    Performs a big-space birthday attack on a hash function.
    
    Args:
        bit_length (int): Bit length of the truncated hash.
        max_attempts (int): Maximum number of attempts to find a collision.
        input_length (int): Length of random input strings.
        
    Returns:
        tuple: A collision pair (x, x') if found, otherwise None.
    """
    hash_table = {}  # Mapping hash values -> preimage
    
    for _ in range(max_attempts):
        # Generate a random input of specified length
        x = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=input_length))
        
        # Compute its truncated hash
        h_x = truncated_hash(x, bit_length)
        
        # Check for a collision
        if h_x in hash_table and hash_table[h_x] != x:
            return hash_table[h_x], x  # Collision found
        
        # Store the hash value and input
        hash_table[h_x] = x
    
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
        print(f"Hash: {truncated_hash(collision[0], bit_length):06x}")
    else:
        print("No collision found within the attempt limit.")