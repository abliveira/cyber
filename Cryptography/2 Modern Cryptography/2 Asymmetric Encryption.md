# Public-Key Cryptography (Asymmetric Cryptography)

Public-key cryptography (asymmetric cryptography) is any cryptographic system that uses pairs of keys:
- **Public keys**, which may be disseminated widely
- **Private keys**, which are known only to the owner

This accomplishes two core functions:
- **Authentication**: The public key verifies that a holder of the paired private key sent the message.
- **Encryption**: Only the paired private key holder can decrypt the message encrypted with the public key.

Public key algorithms are fundamental security ingredients in cryptosystems, applications, and protocols.
Some encryption schemes can be proven secure on the basis of the presumed difficulty of a mathematical problem, such as:
- Factoring the product of two large prime numbers
- Computing discrete logarithms

Some examples of asymmetric key encryption include:
- Diffie-Hellman key exchange protocol
- DSS (Digital Signature Standard)
- Various password-authenticated key agreement techniques
- RSA encryption algorithm

Asymmetric key encryption is more secure than symmetric because you can safely share your public key with anyone, while keeping your private key secret. This enables secure communication without the need to exchange secrets over insecure channels. However, asymmetric algorithms are slower and more computationally intensive than symmetric algorithms.

Because of this, real-world systems typically use **hybrid encryption**:
- A symmetric key encrypts the actual data (fast and efficient)
- The symmetric key itself is then encrypted using asymmetric encryption and shared securely

---

## Core Cryptographic Operations

### 1. Encryption and Decryption
Used to ensure **confidentiality** of messages.  

**Steps:**
1. Sender retrieves the recipient’s **public key**.  
2. Sender encrypts the plaintext with the public key → ciphertext is generated.  
3. Recipient uses their **private key** to decrypt the ciphertext.  
4. The original plaintext is recovered.  

---

### 2. Signing and Verification
Used to ensure **authenticity** and **integrity**.  

**Steps:**
1. Sender hashes the message content.  
2. Sender encrypts the hash with their **private key**, producing a **digital signature**.  
3. Recipient independently hashes the received plaintext.  
4. Recipient decrypts the digital signature using the sender’s **public key**.  
5. If both hashes match, the message is verified as authentic and unmodified.  

---

### 3. Combined Encryption + Authentication
Both confidentiality and authenticity can be achieved in a single workflow.  

**Steps:**
1. **Signing**: Sender hashes the message and signs it with their **private key**.  
2. **Encryption**: The message + signature are encrypted with the recipient’s **public key**.  
3. **Decryption**: Recipient uses their **private key** to decrypt and recover the plaintext + signature.  
4. **Verification**: Recipient validates the signature using the sender’s **public key**, ensuring integrity and authenticity.  

This combined process ensures that only the intended recipient can read the message (confidentiality), and the recipient can be confident about who sent it (authenticity).  