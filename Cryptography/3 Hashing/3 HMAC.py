"""
HMAC (Hash-based Message Authentication Code) is a mechanism for message authentication using cryptographic hash functions and a secret key. It is used to verify both the integrity and the authenticity of a message.

Unlike plain hashing, HMAC incorporates a secret key into the hash calculation. This means that even if an attacker sees the hash value,
they cannot reproduce it without the secret key. HMAC is designed to be secure even when the hash function used is not collision-resistant.

Typical use cases include verifying data transmission over insecure channels (e.g., HTTP APIs, cookies, or tokens), and it's commonly
used in protocols such as TLS, SSH, and IPsec.

Key Properties:
- The same message with the same key always produces the same HMAC.
- Changing the message or key results in a different HMAC.
- HMAC is resistant to length-extension attacks.
- HMACs should be compared using constant-time functions (e.g., compare_digest) to avoid timing attacks.
"""

import hmac
import hashlib

# Secret key shared between sender and receiver
key = b'super_secret_key'

# Message whose integrity we want to protect
message = b'Important message'

# Generate HMAC using SHA-256
hmac_hash = hmac.new(key, message, hashlib.sha256).hexdigest()
print(f"HMAC-SHA256: {hmac_hash}")

# Simulate message verification by regenerating the HMAC
received_hmac = hmac_hash
expected_hmac = hmac.new(key, message, hashlib.sha256).hexdigest()

# Use constant-time comparison to prevent timing attacks
if hmac.compare_digest(received_hmac, expected_hmac):
    print("Message integrity verified.")
else:
    print("Message verification failed.")
