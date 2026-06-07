from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA key pair
key = RSA.generate(2048)

# Create cipher using public key
cipher = PKCS1_OAEP.new(key.publickey())

message = b"HELLO RSA"
encrypted = cipher.encrypt(message)

print("Encrypted:", encrypted)
