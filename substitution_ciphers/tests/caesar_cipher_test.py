import unittest
from substitution_ciphers.src.ciphers.caesar_cipher import make_cipher

class EncoderDecoder(unittest.TestCase):

    def test_cipher_length(self):
        cipher = make_cipher(5)
        self.assertEqual(52, len(cipher), 'Length mismatch')

    def test_cipher_with_salt_equal_zero(self):
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.assertEqual(letters, ''.join(make_cipher(0)), 'Cipher Test with salt=0')     

    def test_cipher_with_salt_equal_five(self):
        letters = 'fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcde'
        self.assertEqual(letters, ''.join(make_cipher(5)), 'Cipher Test with salt=5')     

    def test_cipher_with_salt_equal_negative_five(self):
        letters = 'VWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU'
        self.assertEqual(letters, ''.join(make_cipher(-5)), 'Cipher Test with salt=-5')     

    def test_cipher_with_salt_equal_100(self):
        cipher = make_cipher(100)
        self.assertEqual(cipher[0], 'a', 'Cipher Test with salt=100')     

    def test_cipher_with_salt_equal_negative_100(self):
        cipher = make_cipher(-100)
        self.assertEqual(cipher[0], 'a', 'Cipher Test with salt=-100')     

if __name__ == '__main__':
    unittest.main(warnings='ignore')