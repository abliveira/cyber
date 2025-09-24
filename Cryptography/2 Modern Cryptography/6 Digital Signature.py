"""
Digital Signatures with RSA

Imagine that Alice wants to send a message to Bob. While RSA encryption ensures
that no one else can read the message, Bob still needs a way to confirm that
the message truly came from Alice. This is where digital signatures are used.

A digital signature is a mathematical scheme that provides authentication and
integrity for digital messages or documents. A valid signature proves that the
message was created by a known sender (authentication) and that it has not been
altered (integrity). Digital signatures are widely used in cryptographic
protocols, software distribution, financial transactions, and secure
communications.

How it works:
- The sender creates a hash of the message.
- The hash is encrypted with the sender’s private key, producing the signature.
- The signature is sent together with the message.
- The receiver decrypts the signature using the sender’s public key and compares
  the result with a freshly computed hash of the received message.
- If both match, the message is verified as authentic and untampered.

This process ensures authentication and non-repudiation, but not confidentiality.
To achieve complete security, a digitally signed message is usually combined
with encryption (e.g., in protocols such as PGP).

About this code:

The implementation below demonstrates this process using RSA. Alice generates
a key pair, signs her message with her private key, and sends the message along
with the signature. Bob receives the message, verifies the signature using
Alice’s public key, and confirms both the authenticity of the sender and the
integrity of the message.

In this example, we use very small prime numbers for clarity.
Because of that, we reduce the hash modulo n before signing and verifying.
This keeps the demo correct for small numbers but is NOT secure in practice.
"""

import hashlib

# RSA HELPER FUNCTIONS (Simplified for Demonstration)

def gcd(a, b):
    """Greatest Common Divisor using Euclidean Algorithm."""
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    """Find modular inverse of a under modulo m (Extended Euclidean Algorithm)."""
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(p, q):
    """Generate RSA keypair from two primes p and q."""
    n = p * q
    phi = (p - 1) * (q - 1)

    # Common choice for e is 65537
    e = 65537
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2

    d = modinv(e, phi)
    return (e, n), (d, n)  # (public_key, private_key)

def sign(msg, private_key):
    """Create a digital signature:
    - Hash the message with SHA-256
    - Reduce hash modulo n (for demo with small n)
    - Encrypt with private key
    """
    d, n = private_key
    msg_hash = int.from_bytes(hashlib.sha256(msg.encode()).digest(), 'big') % n
    return pow(msg_hash, d, n)

def verify(msg, signature, public_key):
    """Verify a digital signature:
    - Hash the message again and reduce modulo n
    - Decrypt signature with public key
    - Compare values
    """
    e, n = public_key
    msg_hash = int.from_bytes(hashlib.sha256(msg.encode()).digest(), 'big') % n
    hash_from_sig = pow(signature, e, n)
    return msg_hash == hash_from_sig

# DEMONSTRATION OF DIGITAL SIGNATURES

# Step 1: Alice generates her RSA keypair (using small primes for simplicity)
p, q = 61, 53
alice_public, alice_private = generate_keypair(p, q)

# Step 2: Alice writes her message
message = "Hi Bob, this is Alice!"

# Step 3: Alice signs the message with her private key
signature = sign(message, alice_private)

print("Alice sends the message and the signature...")
print("Message:", message)
print("Signature:", signature)

# Step 4: Bob verifies the signature using Alice’s public key
is_authentic = verify(message, signature, alice_public)

print("\nBob verifies the signature...")
print("Signature valid?", is_authentic)
