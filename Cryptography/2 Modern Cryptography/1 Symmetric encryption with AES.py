"""
Symmetric Encryption with AES-GCM (Advanced Encryption Standard - Galois/Counter Mode)

Symmetric encryption uses the same secret key for both encrypting and decrypting data.
It is efficient for large amounts of data but requires secure key management to prevent unauthorized access.

AES (Advanced Encryption Standard) is a symmetric encryption algorithm standardized by NIST in 2001.
It is widely adopted in both commercial and governmental systems for securing sensitive information
due to its efficiency and strong security.

It operates on fixed-size blocks of 128 bits and supports three key lengths:
- AES-128: 128-bit key, 10 rounds
- AES-192: 192-bit key, 12 rounds
- AES-256: 256-bit key, 14 rounds

Each encryption round consists of the following transformations:

- **SubBytes**: A non-linear substitution step where each byte in the state is replaced with another according to a fixed S-box (substitution box). This introduces non-linearity and confusion into the cipher.
  
- **ShiftRows**: A transposition step where each row of the state is cyclically shifted to the left by a certain number of positions. This ensures interdependence among columns and improves diffusion.

- **MixColumns**: A mixing operation that transforms each column of the state matrix using linear algebra over a finite field. This step further spreads the influence of each byte over the block.

- **AddRoundKey**: A bitwise XOR operation between the current state and a round-specific portion of the expanded cipher key. This step injects the cryptographic key material into the encryption process.

AES is used in various modes of operation; in this example, we use **GCM (Galois/Counter Mode)**, which provides both:
- Confidentiality through AES in counter mode
- Integrity and authenticity through a Galois field-based MAC (Message Authentication Code)

The example will:
- Generate a secure 256-bit AES key
- Encrypt plaintext using AES-GCM with a unique nonce
- Decrypt ciphertext and verify integrity using the authentication tag

"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os

# Generate a random 256-bit (32 bytes) key for AES-256
key = os.urandom(32)

# Generate a random 96-bit (12 bytes) nonce for AES-GCM
nonce = os.urandom(12)

# The plaintext message to be encrypted (hardcoded for example purposes)
plaintext = b"Confidential data that needs to be encrypted."

# Create AES-GCM cipher object
aesgcm = Cipher(
    algorithms.AES(key),
    modes.GCM(nonce),
    backend=default_backend()
).encryptor()

# Encrypt the plaintext
ciphertext = aesgcm.update(plaintext) + aesgcm.finalize()

# Retrieve the authentication tag generated during encryption
tag = aesgcm.tag

print("Symmetric Encryption with AES-GCM")
print(f"Key (hex)      : {key.hex()}")
print(f"Nonce (hex)    : {nonce.hex()}")
print(f"Ciphertext (hex): {ciphertext.hex()}")
print(f"Tag (hex)      : {tag.hex()}")

# --- Decryption process ---

# Create a decryptor with the same key, nonce, and authentication tag
decryptor = Cipher(
    algorithms.AES(key),
    modes.GCM(nonce, tag),
    backend=default_backend()
).decryptor()

# Decrypt the ciphertext
decrypted_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

print("\nDecrypted plaintext:")
print(decrypted_plaintext.decode())
