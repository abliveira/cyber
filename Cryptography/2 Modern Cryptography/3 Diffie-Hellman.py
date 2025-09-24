"""

Diffie-Hellman is a method that allows two people, like Alice and Bob, to create a shared secret key over an unsecure channel, such as the internet. This key can then be used to encrypt their communications, ensuring that only they can read the messages. The protocol's genius lies in the fact that the key itself is never actually sent.

The process combines an easy-to-understand concept with complex, one-way math.

Imagine Alice and Bob want to create a secret color together.

1. Public Agreement: They first agree on a common public color, like yellow, that everyone can see. This corresponds to them agreeing on two large public numbers: a prime n and a base g.
2. Private Secret: Alice chooses a secret color (e.g., blue) that only she knows. Bob does the same with his own secret color (e.g., red). Mathematically, this is where Alice picks a secret number x and Bob picks a secret number y.
3. The Public Mix: Next, Alice mixes her secret blue with the public yellow and sends the resulting greenish-yellow mixture to Bob. Bob does the same, mixing his secret red with the public yellow and sending the resulting orangish-yellow mixture to Alice. This is the core of the exchange:
  * Alice computes her public key, X = g^x mod n, and sends it to Bob.
  * Bob computes his public key, Y = g^y mod n, and sends it to Alice.

An eavesdropper can see these "mixed" public values (X and Y) but cannot easily "un-mix" them to discover the original secret numbers (x and y). This is because it is computationally very difficult to solve what is known as the Discrete Logarithm Problem for large numbers.

4. The Final Secret: When Alice receives Bob's mixture, she adds her secret blue to it. When Bob receives Alice's mixture, he adds his secret red to it. They both arrive at the same final secret color. Mathematically, the process is:
* Alice computes the final key, k = Y^x mod n, using Bob's public key and her own secret number.
* Bob computes the final key, k' = X^y mod n, using Alice's public key and his own secret number.

Both of their calculations result in the same final key, k = k' = g^{xy} mod n. The security of the protocol relies on the fact that only Alice and Bob have their private secrets (x and y) to perform the final calculation.

"""
import random as rnd

def is_prime(num):
    """
    Checks if a number is prime.
    A number is prime if it's greater than 1 and has no divisors other than 1 and itself.
    """
    if num <= 1:
        return False
    # Check for divisibility from 2 up to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def dhkep(g, p):
    """
    Performs the Diffie-Hellman Key Exchange.
    g and p must be a primitive root modulo p and a prime number, respectively.
    """
    if not is_prime(p):
        print(f"Error: {p} is not a prime number.")
        return

    # Alice's secret key
    a = rnd.randint(2, p - 1)
    # Bob's secret key
    b = rnd.randint(2, p - 1)

    # Alice's public key (A)
    # Note: Use a double asterisk (**) for exponentiation
    A = (g ** a) % p

    # Bob's public key (B)
    B = (g ** b) % p

    # Alice computes the shared secret key
    key1 = (B ** a) % p

    # Bob computes the shared secret key
    key2 = (A ** b) % p

    print(f"Alice's private key: {a}")
    print(f"Bob's private key: {b}")
    print(f"Publicly exchanged values: (g={g}, p={p})")
    print(f"Alice's public key (A): {A}")
    print(f"Bob's public key (B): {B}")
    print("-" * 30)
    print(f"Alice's shared secret key: {key1}")
    print(f"Bob's shared secret key: {key2}")

    if key1 == key2:
        print("\nSuccess! The keys match.")
    else:
        print("\nError! The keys do not match.")

# Example usage
try:
    g = int(input("Enter a value for g (base): "))
    p = int(input("Enter a prime number for p: "))
    dhkep(g, p)
except ValueError:
    print("Error: Invalid input. Please enter integer values.")