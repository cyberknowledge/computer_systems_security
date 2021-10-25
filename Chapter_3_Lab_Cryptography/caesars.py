#!/usr/bin/env python
# coding: utf-8

# A python function for Caesar Cipher - Encrypt
def encrypt(text,s):
    result = ""
    
    # Read the plain text
    for i in range(0,len(text)):
        char = text[i]

        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
        
    return result

# A python function for Caesar Cipher - Decrypt
def decrypt(ciphertext,s):
    result = ""
    
    # Read the plain text
    for i in range(0,len(ciphertext)):
        char = ciphertext[i]

        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)
        
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
        
    return result