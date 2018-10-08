#!/usr/bin/env python3

"""Substitution cipher using deranged alphabet"""
from string import ascii_letters as letters
import re
import sys

def encode(message, cipher):
    """Encode a plain text message using a given cipher"""
    return message.translate(str.maketrans(letters, ''.join(cipher)))

def decode(secret, cipher):
    """Decode an encoded secret using a given cipher"""
    return secret.translate(str.maketrans(''.join(cipher), letters))

def make_cipher(salt):
    """Create a deranged alphabet cipher using a keyword as salt"""
    if not salt.isalpha():
        print('salt must include only letters {}'.format(salt))
        sys.exit(1)

    salt = ''.join(sorted(set(salt), key=salt.index))
    pattern = '[{}]'.format(salt)
    return salt + re.sub(pattern, '', ''.join(list(letters)))

MESSAGE = 'Better Faster Forever'
cipher = make_cipher('QWERTY')
secret = encode(MESSAGE, cipher)
print('secret: {}'.format(secret))
# secret: vTnnTl zQmnTl zilTpTl
print(decode(secret, cipher))
