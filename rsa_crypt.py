from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

# RSA Key Generation
def generate_keys() -> tuple[RSAPrivateKey, RSAPublicKey]:
    private_key: RSAPrivateKey = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key: RSAPublicKey = private_key.public_key()
    return private_key, public_key

# RSA Encryption
def encrypt(public_key: RSAPublicKey, plaintext):
    ciphertext = public_key.encrypt(
        plaintext.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

# RSA Decryption
def decrypt(private_key, ciphertext):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

# Example usage
if __name__ == "__main__":
    private_key, public_key = generate_keys()

    # Serialize keys for display
    pem_public_key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    pem_private_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    print("Public Key:")
    print(pem_public_key.decode())

    print("Private Key:")
    print(pem_private_key.decode())

    message = "Hello RSA"
    print("Original Message:", message)

    encrypted_message = encrypt(public_key, message)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted Message:", decrypted_message)