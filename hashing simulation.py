import hashlib

message = "Advanced Cryptography"

hash_object = hashlib.sha256(message.encode())

print("Hash Value:")
print(hash_object.hexdigest())