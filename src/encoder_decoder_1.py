#!/usr/bin/env python3

"""Caesar cipher"""
from string import ascii_letters as letters

def encode(message, cipher):
    """encode a plain text message using a given cipher"""
    return message.translate(str.maketrans(letters, ''.join(cipher)))

def decode(secret, cipher):
    """decode an encoded secret using a given cipher"""
    return secret.translate(str.maketrans(''.join(cipher), letters))

def make_cipher(salt):
    """create a Caesar cipher using a given rotation value as salt"""
    cipher = list(letters)
    return cipher[salt:] + cipher[:salt]

MESSAGE = 'Clean Code'
CIPHER = make_cipher(5)
SECRET = encode(MESSAGE, CIPHER)
print('secret: {}'.format(SECRET))
# secret: Hqjfs Htij
print(decode(SECRET, CIPHER))
