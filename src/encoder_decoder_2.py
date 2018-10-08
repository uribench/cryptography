#!/usr/bin/env python3

"""Substitution cipher using deranged alphabet"""
from string import ascii_letters as letters
import re
import sys

def encode(message, cipher):
    """encode a plain text message using a given cipher"""
    return message.translate(str.maketrans(letters, ''.join(cipher)))

def decode(secret, cipher):
    """decode an encoded secret using a given cipher"""
    return secret.translate(str.maketrans(''.join(cipher), letters))

def make_cipher(salt):
    """create a deranged alphabet cipher using a given rotation value as salt"""
    if not salt.isalpha():
        print('salt must include only letters {}'.format(salt))
        sys.exit(1)

    salt = ''.join(sorted(set(salt), key=salt.index))
    pattern = '[{}]'.format(salt)
    return salt + re.sub(pattern, '', ''.join(list(letters)))

MESSAGE = 'Better Faster Forever'
CIPHER = make_cipher('QWERTY')
SECRET = encode(MESSAGE, CIPHER)
print('secret: {}'.format(SECRET))
# secret: vTnnTl zQmnTl zilTpTl
print(decode(SECRET, CIPHER))
