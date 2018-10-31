import pytest
from substitution_ciphers.src.encoder import encode

def test_encode_with_caesar_cipher_and_null_string():
    cipher = 'fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde'
    assert encode('', cipher) == ''

def test_encode_with_caesar_cipher_and_custom_message():
    cipher = 'fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde'
    assert encode('helloworld', cipher) == 'mjqqtBtwqi'

def test_encode_with_caesar_cipher_and_actual_message():
    message = 'Clean Code'
    cipher = 'fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde'
    assert encode(message, cipher) == 'Hqjfs Htij'

def test_encode_with_deranged_alphabet_cipher_and_actual_message():
    message = 'Better Faster Forever'
    cipher = 'QWERTYabcdefghijklmnopqrstuvwxyzABCDFGHIJKLMNOPSUVXZ'
    assert encode(message, cipher) == 'vTnnTl zQmnTl zilTpTl'
