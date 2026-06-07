from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA key pair
key = RSA.generate(2048)

# Create encryptor (public key)
encrypt_cipher = PKCS1_OAEP.new(key.publickey())

# Create decryptor (private key)
decrypt_cipher = PKCS1_OAEP.new(key)

# Test messages
messages = [
    b"HELLO RSA",
    b"Advanced Cryptography",
    b"Secure Communication"
]

for msg in messages:
    encrypted = encrypt_cipher.encrypt(msg)
    decrypted = decrypt_cipher.decrypt(encrypted)

    print("Original :", msg.decode())
    print("Recovered:", decrypted.decode())
    print("-" * 30)