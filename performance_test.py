import time

def xor_encrypt(key, plaintext):
    return bytes([p ^ key[i % len(key)] for i, p in enumerate(plaintext)])

def rc4(key, plaintext):
    key = [ord(c) for c in key]
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    i = j = 0
    keystream = []
    for _ in range(len(plaintext)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)
    return bytes([p ^ k for p, k in zip(plaintext, keystream)])

# Test message
message = b"HELLO WORLD" * 1000
key_xor = b"secret"
key_rc4 = "secret"

# XOR timing
start = time.time()
xor_encrypt(key_xor, message)
print("XOR time:", time.time() - start)

# RC4 timing
start = time.time()
rc4(key_rc4, message.decode())
print("RC4 time:", time.time() - start)
