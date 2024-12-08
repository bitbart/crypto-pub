import hashlib
import sys

def calculate_hash(input_string):
    """
    Calculate the SHA-256 hash of a string.
    
    Args:
        input_string (str): The input string.
        
    Returns:
        str: The hash of the string in hexadecimal format.
    """
    # Encode the string to bytes
    byte_string = input_string.encode('utf-8')
    
    # Calculate the hash using SHA-256
    hash_object = hashlib.sha256(byte_string)
    
    # Return the hash in hexadecimal format
    return hash_object.hexdigest()

if __name__ == "__main__":
    # Check if the user provided a string as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <string>")
        sys.exit(1)
    
    # Get the string from the command-line argument
    input_string = sys.argv[1]
    calculated_hash = calculate_hash(input_string)
    
    print(f"The hash of the string '{input_string}' is:\n{calculated_hash}")
