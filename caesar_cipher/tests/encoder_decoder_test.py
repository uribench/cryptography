import unittest
from caesar_cipher.src.encoder_decoder import *

class EncoderDecoder1(unittest.TestCase):

    def test_encode_with_null_string(self):
        self.assertEqual(encode('', cipher), '', 'Null Value')

    def test_encode_with_custom_message(self):
        self.assertEqual(encode('helloworld', cipher), 'mjqqtBtwqi', 'Custom Message')

    def test_encode_with_actual_message(self):
        self.assertEqual(encode(MESSAGE, cipher), 'Hqjfs Htij', 'Actual Message')

    def test_cipher_length(self):
        self.assertEqual(52, len(cipher), 'Length mismatch')

    def test_decode_with_custom_message(self):
        self.assertEqual(decode('mjqqtBtwqi', cipher), 'helloworld', 'Custom Message Decode')

    def test_decode_with_original_message(self):
        self.assertEqual(decode(secret, cipher), MESSAGE, 'Original Message Decode')

    def test_decode_with_salt_equal_zero(self):
        result = make_cipher(0)
        self.assertEqual(decode('abc', result), 'abc')

if __name__ == '__main__':
    unittest.main(warnings='ignore')