def rc4(key, plaintext):
    """
    RC4 Stream Cipher Simulation
    :param key: string key
    :param plaintext: string message
    :return: ciphertext as list of integers
    """
    # Key Scheduling Algorithm (KSA)
    key = [ord(c) for c in key]
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = j = 0
    keystream = []
    for _ in range(len(plaintext)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)

    # XOR plaintext with keystream
    ciphertext = [ord(p) ^ k for p, k in zip(plaintext, keystream)]
    return ciphertext


def rc4_decrypt(key, ciphertext):
    """
    RC4 Decryption (same as encryption, since XOR is symmetric)
    """
    # Run RC4 again to regenerate keystream
    plaintext = "".join(chr(c ^ k) for c, k in zip(ciphertext, rc4(key, "".join(chr(0) for _ in ciphertext))))
    return plaintext


# Example usage
key = "secret"
message = "HELLO"

cipher = rc4(key, message)
print("Cipher (numeric values):", cipher)

decrypted = rc4_decrypt(key, cipher)
print("Decrypted:", decrypted)
