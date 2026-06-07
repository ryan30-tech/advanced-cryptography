from Crypto.Cipher import AES
import os

key = os.urandom(16)   # 128-bit key
iv = os.urandom(16)    # Initialization vector
cipher = AES.new(key, AES.MODE_CBC, iv)

message = b"HELLO WORLD"
pad_len = 16 - (len(message) % 16)
padded = message + bytes([pad_len]) * pad_len

encrypted = cipher.encrypt(padded)
print("Encrypted:", encrypted)
