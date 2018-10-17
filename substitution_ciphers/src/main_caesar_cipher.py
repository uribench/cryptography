#!/usr/bin/env python3

"""Sample code demonstrating usage of the Caesar cipher"""
from ciphers.caesar_cipher import make_cipher
from encoder import encode
from decoder import decode

MESSAGE = 'Clean Code'
cipher = make_cipher(5)
secret = encode(MESSAGE, cipher)
print('secret: {}'.format(secret))
# secret: Hqjfs Htij
print(decode(secret, cipher))
