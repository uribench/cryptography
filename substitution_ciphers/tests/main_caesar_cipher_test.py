"""Functional test of the 'main_caesar_cipher.py' sample program"""
import pytest
from subprocess import Popen, PIPE

def test_output_of_main():
    program = 'substitution_ciphers/src/main_caesar_cipher.py'
    output = Popen([program], stdout=PIPE).communicate()[0]
    assert b'Hqjfs' in output
    assert b'Clean Code' in output
    assert b'Random Output' not in output