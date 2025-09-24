"""
RSA is one of the first public-key (asymmetric) cryptosystems and is widely used for secure data transmission. RSA stands for Rivest-Shamir-Adleman, initial letters of the surnames of its creators. This asymmetry is based on the practical difficulty of the factorization of the product of two large prime numbers, the "factoring problem".

Here's how key generation works:
1. Choose two distinct prime numbers, p, and q.
2. Compute n = p * q. n is used as the modulus for both the public and private keys. Its length, usually expressed in bits, is the key length.
3. Compute λ(n) = least_common_multiple(p − 1, q − 1). This value is private.
4. Choose an integer e such that 1 < e < λ(n), e and λ(n) are coprime.
5. Determine d from d * e ≡ 1 (mod λ(n)).

e is released as the public key exponent.
d is kept as the private key exponent.

Key pair
public key: (e, n)
private key: (d, n)

Currently, the standard sizes for RSA keys are as follows:
512 bits - Low-strength key
1024 bits - Medium-strength key
2048 bits - High-strength key
4096 bits - Very high-strength key

Suppose that Bob wants to send information to Alice. If they decide to use RSA, Bob must know Alice's public key to encrypt the message and Alice must use her private key to decrypt the message. To enable Bob to send his encrypted messages, Alice transmits her public key (n, e) to Bob via a reliable (not necessarily secret) channel. Alice's private key (d) is never distributed.

Let's try to generate very simple key pair:
1. p = 61 and q = 53
2. n = 61 * 53 =  3233
3. λ(n) = lcm(p-1, q-1) = lcm(60, 52) = 780
4. e = 17  (1 < e < λ(n), e and λ(n) are coprime)
5. d = 413  (d * e mod λ(n) = 1)

public key: (n = 3233, e = 17)
private key: (n = 3233, d = 413)

We generated the key pair. We need the public key (n, e) to encrypt plaintext. Let's assign plaintext to m and the ciphertext to c; then ciphertext will be:
c = m ^ e mod n

For example, if our plaintext m = 65, then:
c(m) = 65 ^ 17 mod 3233 = 2790

To decrypt the ciphertext with the private key (n, d), we should use this:
m(c) = c ^ d mod n = 2790 ^ 413 mod 3233 = 65

"""


import random, math, sys, codecs

# Configure output encoding to UTF-16 for better Unicode handling in some environments
sys.stdout = codecs.getwriter('utf_16')(sys.stdout.buffer, 'strict')

# --- Check if a number is prime ---
def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    # Trial division: check divisibility from 2 up to num-1
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# --- RSA Encryption ---
def encrypt(msg, n, e):
    msg = [ord(i) ** e % n for i in list(msg)]
    return ' '.join(map(str, msg))  # return space-separated ciphertext numbers

# --- RSA Decryption ---
def decrypt(msg, n, d):
    msg = [chr((int(i) ** d) % n) for i in msg.split()]
    return ''.join(msg)

# --- RSA Key Generation ---
print("\n=== RSA Key Generation ===")

# Step 1: Generate primes
prime_list = list(i for i in range(127, 500+1) if prime(i) )# Note: In real applications, use much larger primes for security
p = random.choice(prime_list)
q = random.choice(prime_list)
print(f"Prime p: {p}")
print(f"Prime q: {q}")

# Step 2: Compute modulus n
n = p * q
print(f"n = p * q = {p} * {q} = {n}")

# Step 3: Compute Euler's totient function phi(n)
phi_n = (p - 1) * (q - 1)
print(f"phi(n) = (p-1)*(q-1) = ({p}-1)*({q}-1) = {phi_n}")

# Step 4: Choose public exponent e
e = random.choice([i for i in range(2, n) if math.gcd(i, phi_n) == 1])
print(f"Public exponent e chosen: {e} (coprime with phi(n))")

# Step 5: Compute private exponent d
d = 1
while (e * d) % phi_n != 1:
    d += 1
print(f"Private exponent d calculated: {d}")

# Step 6: Define public and private key pairs
public_key = (n, e)
private_key = (n, d)
print(f"Public key: {public_key}")
print(f"Private key: {private_key}")

# --- Encryption & Decryption Demo ---
print("\n=== Encryption & Decryption Demo ===")
msg = input("Enter a message: ") or 'Some message'
print(f"Plaintext message: {msg}")
print(f"Plaintext as Unicode values: {' '.join(map(str, [ord(i) for i in msg]))}")

# Encrypt with public key
encrypted = encrypt(msg, *public_key)
print(f"Encrypted ciphertext: {encrypted}")

# Decrypt with private key
decrypted = decrypt(encrypted, *private_key)
print(f"Decrypted with private key: {decrypted}")
print(f"Decryption successful? {decrypted == msg}")

# Incorrect attempt: "decrypting" with public key
decrypted_false = decrypt(encrypted, *public_key)
print(f"\n[Check] If someone tries to decrypt with the public key: {decrypted_false}")
