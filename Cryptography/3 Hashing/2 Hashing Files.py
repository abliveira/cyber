"""
When handling files, hashing is a crucial tool for verifying that file contents have 
not been altered or corrupted. This is especially important in file transfers, backups, 
and software distribution, where even a single-bit change can cause failure or security issues.

For small data, hashing can be done all at once, but with large files or streaming data, 
loading everything into memory at once is impractical and inefficient. Therefore, hashing 
is performed incrementally—processing the data piece by piece in chunks. This approach 
ensures low memory usage while still producing the correct hash value for the entire file.

This script demonstrates how to compute the hash of a file incrementally using Python's 
hashlib library, supporting different hashing algorithms such as SHA-256, SHA-1, MD5, etc.
"""

import hashlib

def hash_file(filename, algorithm='sha256'):
    hash_func = hashlib.new(algorithm)
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_func.update(chunk)
    return hash_func.hexdigest()

# Example usage:
if __name__ == "__main__":
    filename = '2 Hashing Files.py'
    file_hash = hash_file(filename, 'sha256')
    print(f"SHA-256 hash of '{filename}': {file_hash}")
