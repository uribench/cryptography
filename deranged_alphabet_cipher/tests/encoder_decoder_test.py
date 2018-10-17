import unittest
from deranged_alphabet_cipher.src.encoder_decoder import *

class EncoderDecoder(unittest.TestCase):

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
