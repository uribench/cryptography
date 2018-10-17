import unittest
from deranged_alphabet_cipher.src.encoder_decoder import *

class EncoderDecoder(unittest.TestCase):

    def test_cipher_with_salt_equal_numeric_value(self):
        with self.assertRaises(AttributeError):
            make_cipher(0)

    def test_cipher_with_salt_equal_alphanumeric_value(self):
        with self.assertRaises(SystemExit):
            make_cipher('A0')

    def test_cipher_with_salt_equal_alphabet_no_duplicates_value(self):
        result = make_cipher('QWERTY')
        self.assertEqual('Q', result[0])

    def test_cipher_with_salt_equal_alphabet_with_duplicates_value(self):
        result = make_cipher('QQWERTY')
        self.assertEqual('a', result[6])

    def test_encode_with_null_string(self):
        self.assertEqual(encode('', cipher), '', 'Null Value')

    def test_encode_with_custom_message(self):
        self.assertEqual(encode('helloworld', cipher), 'bTffiqilfR', 'Custom Message')

    def test_encode_with_original_message(self):
        self.assertEqual(encode(MESSAGE, cipher), 'vTnnTl zQmnTl zilTpTl', 'Actual Message')

    def test_decode_with_custom_message(self):
        self.assertEqual(decode('bTffiqilfR', cipher), 'helloworld')

    def test_decode_with_original_message(self):
        self.assertEqual(decode(secret, cipher), MESSAGE, 'Original Message')

if __name__ == '__main__':
    unittest.main()
