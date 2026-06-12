import hashlib

password = input("Enter Password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("Stored Hash:", hashed_password)