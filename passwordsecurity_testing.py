import hashlib

passwords = [
    "123456",
    "password",
    "admin123",
    "MySecurePassword2026"
]

for p in passwords:
    print(p, "->", hashlib.sha256(p.encode()).hexdigest())