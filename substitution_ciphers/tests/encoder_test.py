import unittest
from substitution_ciphers.src.encoder import encode

class TestEncoder(unittest.TestCase):

    def test_encode_with_caesar_cipher_and_null_string(self):
        cipher = 'fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde'
        self.assertEqual(encode('', cipher), '', 'Null Value')

    def test_encode_with_caesar_cipher_and_custom_message(self):
        cipher = 'fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde'
        self.assertEqual(encode('helloworld', cipher), 'mjqqtBtwqi', 'Custom Message')

    def test_encode_with_caesar_cipher_and_actual_message(self):
        message = 'Clean Code'
        cipher = 'fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde'
        self.assertEqual(encode(message, cipher), 'Hqjfs Htij', 'Actual Message')

    def test_encode_with_deranged_alphabet_cipher_and_actual_message(self):
        message = 'Better Faster Forever'
        cipher = 'QWERTYabcdefghijklmnopqrstuvwxyzABCDFGHIJKLMNOPSUVXZ'
        self.assertEqual(encode(message, cipher), 'vTnnTl zQmnTl zilTpTl', 'Actual Message')

if __name__ == '__main__':
    unittest.main(warnings='ignore')