def ceaser_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        if 'a' <= c <= 'z':  # For lowercase letters
            c_encoded = ord('a') + (ord(c) - ord('a') + shift) % 26
        elif 'A' <= c <= 'Z':  # For uppercase letters, if needed
            c_encoded = ord('A') + (ord(c) - ord('A') + shift) % 26
        else:
            c_encoded = ord(c)  # For non-alphabetical characters
        cipher_text += chr(c_encoded)
    return cipher_text
