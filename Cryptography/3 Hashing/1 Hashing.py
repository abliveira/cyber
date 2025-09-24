"""
Hashing is the process of generating a fixed-size value (hash) from input data
using a mathematical function called a hash function.

It plays a key role in securing data transmission by enabling verification that
a message was not altered during transit. When sending a secure message, the sender
generates a hash of the message, encrypts it, and sends both the message and the
encrypted hash to the recipient.

The recipient decrypts the hash and recomputes the hash from the received message.
If both hashes match, the message is verified as authentic and untampered.

Beyond security, hashing is widely used for efficient data retrieval in databases
because searching by a fixed-size hash is faster than by the original data.

Essential Properties of a Secure Cryptographic Hash Function:

1. Determinism:
   For any given input, the hash function must always produce the same output.
   This ensures consistency and reliability in hashing operations.

2. Fixed Output Length:
   Regardless of the input size, the hash function produces an output of fixed length.
   This standardization aids storage, comparison, and cryptographic protocol design.

3. Collision Resistance:
   It should be computationally infeasible to find two distinct inputs producing the same hash output.
   This prevents attackers from substituting messages without detection.

4. Pre-image Resistance:
   Given a hash output, it should be practically impossible to find the original input.
   This protects against reversing the hash to discover the input.

5. Second Pre-image Resistance:
   Given a specific input, it should be infeasible to find another input with the same hash output.
   This prevents forging alternate messages that hash to the same value.

6. Avalanche Effect:
   Small changes in input cause significant, unpredictable changes in the hash output.
   This makes it difficult to infer input similarities from the hash.

"""

import hashlib
import hmac

input_data = b"Hello World"

# MD5 - Legacy hash function, fast but insecure for cryptographic use
md5_hash = hashlib.md5(input_data).hexdigest()
print(f"MD5       : {md5_hash}")

# SHA-1 - Older standard, vulnerabilities discovered, avoid for security-critical use
sha1_hash = hashlib.sha1(input_data).hexdigest()
print(f"SHA-1     : {sha1_hash}")

# SHA-256 - Strong and widely used, recommended for most security applications
sha256_hash = hashlib.sha256(input_data).hexdigest()
print(f"SHA-256   : {sha256_hash}")

# SHA-512 - Part of SHA-2 family, outputs longer hash, suitable for high-security needs
sha512_hash = hashlib.sha512(input_data).hexdigest()
print(f"SHA-512   : {sha512_hash}")

# SHA3-256 - Newer standard designed to be resistant to length-extension attacks
sha3_256_hash = hashlib.sha3_256(input_data).hexdigest()
print(f"SHA3-256  : {sha3_256_hash}")

# SHA3-512 - Like SHA3-256 but with longer output and increased security margin
sha3_512_hash = hashlib.sha3_512(input_data).hexdigest()
print(f"SHA3-512  : {sha3_512_hash}")

# Ensure all hashes are unique for the same input across different algorithms
hashes = {md5_hash, sha1_hash, sha256_hash, sha512_hash, sha3_256_hash, sha3_512_hash}
assert len(hashes) == 6, "Hashes should all be unique for different algorithms."


# Example: How to verify a received hash to ensure data integrity

print("\n--- Hash Verification Example ---")
data_received = b"Important message"

# Hardcoded received hash (simulating a hash sent by the sender)
received_hash = "d7e0a92a7bb8e1e9b3e5f8e30e4356d2be0c2c1a9e79b2c45b1f6c3b91c9f4d5"
print(f"Received Hash: {received_hash}")

# Recompute the hash locally from the received data
computed_hash = hashlib.sha256(data_received).hexdigest()
print(f"Computed Hash: {computed_hash}")

# Secure comparison function
def verify_hash(hash1, hash2):
    return hmac.compare_digest(hash1, hash2)

# Verify authenticity of the received data
if verify_hash(computed_hash, received_hash):
    print("Verification result: Data is authentic and unchanged.")
else:
    print("Verification result: Data has been altered or corrupted.")
