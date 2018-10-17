import unittest
from substitution_ciphers.src.decoder import decode

class TestDecoder(unittest.TestCase):

    def test_decode_with_caesar_cipher_and_custom_message(self):
        cipher = 'fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde'
        self.assertEqual(decode('mjqqtBtwqi', cipher), 'helloworld', 'Custom Message Decode')

    def test_decode_with_caesar_cipher_and_actual_message(self):
        MESSAGE = 'Clean Code'
        cipher = 'fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde'
        secret = 'Hqjfs Htij'
        self.assertEqual(decode(secret, cipher), MESSAGE, 'Actual Message Decode')

    def test_decode_with_caesar_cipher_and_salt_equal_zero(self):
        cipher = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.assertEqual(decode('abc', cipher), 'abc')

if __name__ == '__main__':
    unittest.main(warnings='ignore')