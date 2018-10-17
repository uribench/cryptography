#!/usr/bin/env python3

"""Sample code demonstrating usage of the deranged alphabet cipher"""
from ciphers.deranged_alphabet_cipher import make_cipher
from encoder import encode
from decoder import decode

MESSAGE = 'Better Faster Forever'
cipher = make_cipher('QWERTY')
secret = encode(MESSAGE, cipher)
print('secret: {}'.format(secret))
# secret: vTnnTl zQmnTl zilTpTl
print(decode(secret, cipher))
