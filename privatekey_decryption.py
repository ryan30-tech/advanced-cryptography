from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA key pair
key = RSA.generate(2048)

# Encrypt using public key
encrypt_cipher = PKCS1_OAEP.new(key.publickey())

message = b"HELLO RSA"

encrypted = encrypt_cipher.encrypt(message)

print("Encrypted:", encrypted)

# -------------------------
# Decrypt using private key
# -------------------------

decrypt_cipher = PKCS1_OAEP.new(key)

decrypted = decrypt_cipher.decrypt(encrypted)

print("Decrypted:", decrypted.decode())