def vigenere_encrypt(text, key):
    encrypted = ""

    for i in range(len(text)):
        t = ord(text[i].upper()) - 65
        k = ord(key[i % len(key)].upper()) - 65

        encrypted += chr((t + k) % 26 + 65)

    return encrypted

print(vigenere_encrypt("HELLO", "KEY"))