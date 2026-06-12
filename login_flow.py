import hashlib

stored_hash = hashlib.sha256("admin123".encode()).hexdigest()

password = input("Login Password: ")

entered_hash = hashlib.sha256(password.encode()).hexdigest()

if entered_hash == stored_hash:
    print("Login Successful")
else:
    print("Invalid Password")