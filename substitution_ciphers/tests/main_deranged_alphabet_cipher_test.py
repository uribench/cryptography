"""Functional test of the 'main_deranged_alphabet_cipher.py' sample program"""
import pytest
from subprocess import Popen, PIPE

def test_output_of_main():
    program = 'substitution_ciphers/src/main_deranged_alphabet_cipher.py'
    output = Popen([program], stdout=PIPE).communicate()[0]
    assert b'vTnnTl' in output
    assert b'Better Faster Forever' in output
    assert b'Random Output' not in output