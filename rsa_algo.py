import random
from sympy import isprime, mod_inverse

def generate_keypair(p, q):
    if not (isprime(p) and isprime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be the same')
    
    N = p * q
    PHI = (p-1) * (q-1)

    e = random.randrange(1, PHI)
    e = 5
    g = gcd(e, PHI)
    while g != 1:
        e = random.randrange(1, PHI)
        g = gcd(e, PHI)

    d = mod_inverse(e, PHI)
    
    return ((e, N), (d, N))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def encrypt(pk, plaintext):
    key, N = pk
    cipher = [(ord(char) ** key) % N for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, N = pk
    plain = [chr((char ** key) % N) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    p = 17
    q = 19
    public, private = generate_keypair(p, q)
    print("Public Key: ", public)
    print("Private Key: ", private)
    
    message = "Hello"
    encrypted_msg = encrypt(public, message)
    print("Encrypted Message: ", encrypted_msg)
    
    decrypted_msg = decrypt(private, encrypted_msg)
    print("Decrypted Message: ", decrypted_msg)