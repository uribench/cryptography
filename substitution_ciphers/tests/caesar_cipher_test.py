import pytest
from substitution_ciphers.src.ciphers.caesar_cipher import make_cipher

def test_cipher_length():
    cipher = make_cipher(5)
    assert 52 == len(cipher)

def test_cipher_with_salt_equal_zero():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert letters == ''.join(make_cipher(0))

def test_cipher_with_salt_equal_five():
    letters = 'fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde'
    assert letters == ''.join(make_cipher(5))

def test_cipher_with_salt_equal_negative_five():
    letters = 'VWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU'
    assert letters == ''.join(make_cipher(-5))

def test_cipher_with_salt_equal_100():
    cipher = make_cipher(100)
    assert cipher[0] == 'a'

def test_cipher_with_salt_equal_negative_100():
    cipher = make_cipher(-100)
    assert cipher[0] == 'a'
