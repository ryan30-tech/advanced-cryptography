from Crypto.Cipher import AES

# Use the SAME key and IV used during encryption
key = b'1234567890123456'
iv = b'6543210987654321'

decipher = AES.new(key, AES.MODE_CBC, iv)

with open("encrypted.bin", "rb") as f:
    encrypted = f.read()

decrypted = decipher.decrypt(encrypted)

# Remove padding
pad_len = decrypted[-1]
decrypted = decrypted[:-pad_len]

print(decrypted)
