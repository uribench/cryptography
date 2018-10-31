import pytest
from substitution_ciphers.src.decoder import decode

def test_decode_with_caesar_cipher_and_custom_message():
    cipher = 'fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde'
    assert decode('mjqqtBtwqi', cipher) == 'helloworld'

def test_decode_with_caesar_cipher_and_actual_message():
    message = 'Clean Code'
    cipher = 'fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde'
    secret = 'Hqjfs Htij'
    assert decode(secret, cipher) == message

def test_decode_with_caesar_cipher_and_salt_equal_zero():
    cipher = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert decode('abc', cipher) == 'abc'
