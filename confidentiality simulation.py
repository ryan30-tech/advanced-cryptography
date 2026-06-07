message = "Hello Hunter"

encrypted = ""

for char in message:
    encrypted += chr(ord(char) + 3)

print("Encrypted:", encrypted)

decrypted = ""

for char in encrypted:
    decrypted += chr(ord(char) - 3)

print("Decrypted:", decrypted)