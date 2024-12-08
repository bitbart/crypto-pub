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
    h = f"{truncated:0{bit_length // 4}x}"  # Convert to zero-padded hexadecimal
    # Ensure the length is even by padding with '0' if necessary
    if len(h) % 2 != 0:
        h = '0' + h
    return h

def birthday_attack(bit_length, max_attempts):
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
    num_hex_digits = bit_length // 4 if bit_length % 4 == 0 else 1 + bit_length // 4
    print(f"Number of hexadecimal digits: {num_hex_digits}.")
    x0 = ''.join(random.choices('0123456789abcdef', k=num_hex_digits))
    # Ensure the length is even by padding with '0' if necessary
    if len(x0) % 2 != 0:
        x0 = '0' + x0

    print(f"Initial string: {x0}")
    x = x0
    z = x0

    for i in range(max_attempts):     
        x = truncated_hash(x, bit_length)
        z = truncated_hash(truncated_hash(z, bit_length), bit_length)

        if x == z:
            break

    if i == max_attempts-1:
        return None

    print(f"x = z found after {i} attempts (out of {max_attempts}).")

    z = x
    x = x0

    # Check for a collision
    for j in range(1, i+1):
        h_x = truncated_hash(x, bit_length)
        h_z = truncated_hash(z, bit_length)
        if h_x == h_z:
            return x, z

        x = h_x
        z = h_z

    return None  # No collision found within max_attempts

if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Birthday attack on a hash function.")
    parser.add_argument("-b", "--bit-length",   type=int, default=40,      help="Number of bits for the truncated hash (default: 24).")
    parser.add_argument("-a", "--attempts",     type=int, default=1200000, help="Number of attempts to find a collision (default: 100000).")
    
    args = parser.parse_args()
    bit_length = args.bit_length
    max_attempts = args.attempts
    
    print(f"Attempting a birthday attack on a {bit_length}-bit hash...")
    print(f"Using {max_attempts} attempts with random strings.")

    collision = birthday_attack(bit_length, max_attempts)
    if collision:
        print(f"Collision found!\nString 1: {collision[0]}\nString 2: {collision[1]}")
        # Directly use the result of `truncated_hash` since it's already a hexadecimal string
        print(f"Hash: {truncated_hash(collision[0], bit_length)}")
    else:
        print("No collision found within the attempt limit.")
