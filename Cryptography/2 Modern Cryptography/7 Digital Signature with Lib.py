from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import base64


# PART 2 — DIGITAL SIGNATURE/VERIFICATION
#
# PURPOSE:
#   - Digital signatures ensure AUTHENTICITY (sender identity) and INTEGRITY (message unchanged).
#   - The sender (Alice) signs with her PRIVATE key.
#   - The receiver (Bob) verifies using Alice’s PUBLIC key.
#
# SCENARIO:
#   Bob not only wants to read the message but also confirm:
#     1. It really came from Alice.
#     2. It was not altered in transit.

# Step 1: Alice prepares her message
message = b"Hello Bob, this is a secret from Alice!"

# Step 2: Alice generates her RSA key pair
# Alice keeps her PRIVATE key secret and shares her PUBLIC key for verification.
alice_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
alice_public_key = alice_private_key.public_key()

# Step 3: Alice signs the message
# Signing process:
#   1. The message is hashed with SHA-256.
#   2. The hash is then encrypted with Alice’s PRIVATE key.
#   3. The result is the digital signature.
signature = alice_private_key.sign(
    message,
    padding.PSS(  # PSS (Probabilistic Signature Scheme) is recommended for RSA signatures
        mgf=padding.MGF1(hashes.SHA256()),  # Mask generation function based on SHA-256
        salt_length=padding.PSS.MAX_LENGTH  # Random salt for stronger security
    ),
    hashes.SHA256()  # Hashing algorithm used during signing
)

print("\n=== Digital Signature ===")
print("Message:", message.decode())
print("Signature (created with Alice's private key):", base64.b64encode(signature).decode())

# Step 4: Bob verifies the signature using Alice’s PUBLIC key
# Verification process:
#   1. Bob decrypts the signature using Alice’s PUBLIC key to recover the original hash.
#   2. Bob hashes the received message himself.
#   3. If both hashes match, then:
#        - The message is authentic (came from Alice).
#        - The message is intact (not altered).
try:
    alice_public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is VALID → Message is authentic and intact.")
except Exception:
    print("Signature verification FAILED → Message may be forged or altered.")