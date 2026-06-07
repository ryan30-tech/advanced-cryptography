# RSA Simulation

p = 17
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 7
d = 23

message = 88

# Encryption
cipher = (message ** e) % n
print("Encrypted:", cipher)

# Decryption
plain = (cipher ** d) % n
print("Decrypted:", plain)