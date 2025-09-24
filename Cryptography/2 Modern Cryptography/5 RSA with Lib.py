from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import base64

# RSA ENCRYPTION/DECRYPTION
#
# PURPOSE:
#   - Encryption ensures CONFIDENTIALITY of a message.
#   - Only the intended recipient (Bob) can read the message.
#   - This is achieved because Bob's PUBLIC key is used for encryption,
#     and only Bob's PRIVATE key can decrypt it.
#
# SCENARIO:
#   Alice wants to send a private message to Bob.
#   She encrypts it using Bob’s PUBLIC key.
#   Bob decrypts it using his PRIVATE key.

# Step 1: Bob generates his RSA key pair
# Bob will keep his PRIVATE key secret and share his PUBLIC key openly.
bob_private_key = rsa.generate_private_key(
    public_exponent=65537,   # Commonly used RSA public exponent
    key_size=2048            # 2048-bit RSA key (considered secure today)
)
bob_public_key = bob_private_key.public_key()  # Extract the public key from the pair

# Step 2: Alice prepares her message
message = b"Hello Bob, this is a secret from Alice!"

# Step 3: Alice encrypts the message with Bob’s PUBLIC key
# NOTE: OAEP padding is used for secure encryption (Optimal Asymmetric Encryption Padding).
ciphertext = bob_public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Mask generation function based on SHA-256
        algorithm=hashes.SHA256(),                    # Hash function for padding
        label=None                                    # Optional label (not used here)
    )
)

print("=== RSA Encryption/Decryption ===")
print("Original message:", message.decode())
print("Ciphertext (encrypted with Bob's public key):", base64.b64encode(ciphertext).decode())

# Step 4: Bob decrypts the ciphertext with his PRIVATE key
# Since only Bob’s private key can decrypt what was encrypted with his public key,
# confidentiality is ensured.
decrypted_message = bob_private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Decrypted message (using Bob's private key):", decrypted_message.decode())