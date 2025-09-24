
"""
Password Hashing with Salt and Pepper

This script demonstrates a secure approach to storing passwords by combining:
- Salt: A unique, random string generated for each password. It is concatenated to the password before hashing 
  and is stored alongside the resulting hash. The purpose of the salt is to ensure that identical passwords 
  produce different hashes, thereby preventing the use of precomputed hash databases such as rainbow tables.
  
- Pepper: A fixed secret value known only to the application (not stored in the database). The pepper is also 
  combined with the password before hashing. Even if an attacker obtains the database with all the hashes and salts, 
  they cannot recompute the hash without knowing the pepper, adding a second layer of protection.

- Hash Function: A cryptographic one-way function (such as SHA-256 or SHA-512 in this educational example) 
  used to transform the salted and peppered password into a fixed-size digest. In real-world applications, 
  specialized password hashing algorithms such as bcrypt, scrypt, or Argon2 are preferred due to their resistance 
  to brute-force and GPU-based attacks.

Why this matters:
- Hashing passwords makes it infeasible to recover the original password from the hash.
- Adding a unique salt ensures that identical passwords result in different hashes, protecting against 
  attacks that rely on known hash-password mappings.
- Adding a pepper ensures that an attacker cannot easily test password guesses offline, even with access to 
  the salt and hash.
- This layered approach increases the difficulty of successful attacks against a password database.

Note:
This example uses SHA-256 with salt and pepper for educational purposes. In production systems, always use 
well-established password hashing libraries (e.g., bcrypt, scrypt, or Argon2), which include built-in support for 
salting and cost factors to slow down brute-force attempts.
"""

import hashlib
import os
import hmac
import bcrypt  # Requires: pip install bcrypt


PEPPER = b'supersecretpepper'  # In practice, store securely outside code


def generate_salt(length: int = 16) -> str:
    """Generates a cryptographically secure random salt."""
    return os.urandom(length).hex()


def hash_password(password: str, salt: str, pepper: bytes) -> str:
    """
    Hashes the password using SHA-256, with salt and pepper.

    Parameters:
    - password: User password as string
    - salt: Unique salt for this password (hex string)
    - pepper: Secret value added to all passwords (bytes)

    Returns:
    - Hexadecimal digest of hash
    """
    combined = (salt + password).encode('utf-8')
    return hmac.new(pepper, combined, hashlib.sha256).hexdigest()


def verify_password(input_password: str, stored_salt: str, stored_hash: str, pepper: bytes) -> bool:
    """
    Verifies a password by recomputing the hash and comparing to stored hash.
    """
    recomputed_hash = hash_password(input_password, stored_salt, pepper)
    return hmac.compare_digest(recomputed_hash, stored_hash)

# --- Example: Hashing a Password ---

print("=== SHA-256 Hashing with Salt + Pepper ===")
user_password = "CorrectHorseBatteryStaple"
salt = generate_salt()
hash_digest = hash_password(user_password, salt, PEPPER)

print(f"Password   : {user_password}")
print(f"Salt       : {salt}")
print(f"Hash (SHA) : {hash_digest}")

# --- Example: Verifying Password ---

print("\n=== Verifying the Password ===")
input_attempt = "CorrectHorseBatteryStaple"  # Same as original password
is_valid = verify_password(input_attempt, salt, hash_digest, PEPPER)
print("Password valid!" if is_valid else "Invalid password!")

# --- BONUS: Secure Hashing with bcrypt (Recommended) ---

print("\n=== Hashing with bcrypt (Recommended) ===")
bcrypt_password = b"Tr0ub4dor&3"  # Password to hash
bcrypt_hash = bcrypt.hashpw(bcrypt_password, bcrypt.gensalt())

print(f"bcrypt password : {bcrypt_password.decode()}")
print(f"bcrypt hash     : {bcrypt_hash.decode()}")

bcrypt_check = b"Tr0ub4dor&3"  # Attempt to verify with same password
if bcrypt.checkpw(bcrypt_check, bcrypt_hash):
    print("bcrypt password valid!")
else:
    print("bcrypt password invalid!")
