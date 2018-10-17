#!/usr/bin/env python3

"""Caesar cipher"""
from string import ascii_letters as letters

def encode(message, cipher):
    """Encode a plain text message using a given cipher"""
    return message.translate(str.maketrans(letters, ''.join(cipher)))

def decode(secret, cipher):
    """Decode an encoded secret using a given cipher"""
    return secret.translate(str.maketrans(''.join(cipher), letters))

def make_cipher(salt):
    """Create a Caesar cipher using a given rotation value as salt"""
    cipher = list(letters)
    return cipher[salt:] + cipher[:salt]

MESSAGE = 'Clean Code'
cipher = make_cipher(5)
secret = encode(MESSAGE, cipher)
print('secret: {}'.format(secret))
# secret: Hqjfs Htij
print(decode(secret, cipher))
