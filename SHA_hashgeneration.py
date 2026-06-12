import hashlib

message = "Hunter123"

hash_value = hashlib.sha256(message.encode()).hexdigest()

print("Original:", message)
print("SHA-256:", hash_value)