import unittest
from substitution_ciphers.src.ciphers.deranged_alphabet_cipher import make_cipher

class EncoderDecoder(unittest.TestCase):

    def test_cipher_with_salt_equal_numeric_value(self):
        with self.assertRaises(AttributeError):
            make_cipher(0)

    def test_cipher_with_salt_equal_alphanumeric_value(self):
        with self.assertRaises(SystemExit):
            make_cipher('A0')

    def test_cipher_with_salt_equal_alphabet_no_duplicates_value(self):
        cipher = make_cipher('QWERTY')
        self.assertEqual('Q', cipher[0])

    def test_cipher_with_salt_equal_alphabet_with_duplicates_value(self):
        cipher = make_cipher('QQWERTY')
        self.assertEqual('a', cipher[6])

if __name__ == '__main__':
    unittest.main()
