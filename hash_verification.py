import hashlib

text = "CyberSecurity"

hash1 = hashlib.sha256(text.encode()).hexdigest()
hash2 = hashlib.sha256(text.encode()).hexdigest()

print(hash1)
print(hash2)

if hash1 == hash2:
    print("Verification Successful")