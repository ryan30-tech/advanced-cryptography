message = "Hello Hunter"

encrypted = ""

for ch in message:
    encrypted += chr(ord(ch) + 3)

print("Encrypted:", encrypted)