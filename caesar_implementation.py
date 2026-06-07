def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            result += chr((ord(char.upper()) - 65 + shift) % 26 + 65)
        else:
            result += char

    return result

msg = input("Message: ")

print(caesar_encrypt(msg, 3))