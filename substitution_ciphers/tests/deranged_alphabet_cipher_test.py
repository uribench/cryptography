import pytest
from substitution_ciphers.src.ciphers.deranged_alphabet_cipher import make_cipher

def test_cipher_with_salt_equal_numeric_value():
    with pytest.raises(AttributeError):
        make_cipher(0)

def test_cipher_with_salt_equal_alphanumeric_value():
    with pytest.raises(SystemExit):
        make_cipher('A0')

def test_cipher_with_salt_equal_alphabet_no_duplicates_value():
    cipher = make_cipher('QWERTY')
    assert 'Q' == cipher[0]

def test_cipher_with_salt_equal_alphabet_with_duplicates_value():
    cipher = make_cipher('QQWERTY')
    assert 'a' == cipher[6]
