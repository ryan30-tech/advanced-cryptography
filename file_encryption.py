from Crypto.Cipher import AES
import os

key = os.urandom(16)
iv = os.urandom(16)
cipher = AES.new(key, AES.MODE_CBC, iv)

with open("unsupervised.py", "rb") as f:
    data = f.read()

pad_len = 16 - (len(data) % 16)
padded = data + bytes([pad_len]) * pad_len
encrypted = cipher.encrypt(padded)

with open("encrypted.bin", "wb") as f:
    f.write(encrypted)

print("File encrypted successfully!")
