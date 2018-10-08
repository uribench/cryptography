import unittest
from src.encoder_decoder_1 import *

class encoder_decoder_1(unittest.TestCase):

    def testEncryptWithNullString(self):
        self.assertEqual(encode('', CIPHER), '', 'Null value')

    def testEncryptWithCustomMessage(self):
        self.assertEqual(encode('helloworld', CIPHER), 'mjqqtBtwqi', 'custom message')

    def testEncryptWithActualMessage(self):
        self.assertEqual(encode(MESSAGE, CIPHER), 'Hqjfs Htij', 'actual message')

    def testCipherLength(self):
        self.assertEqual(52, len(CIPHER), 'Length mismatch')

    def testDecodeWithCustomMessage(self):
        self.assertEqual(decode('mjqqtBtwqi', CIPHER), 'helloworld', 'custom message')

    def testDecodeWithOriginalMessage(self):
        self.assertEqual(decode(SECRET, CIPHER), MESSAGE, 'original message')

    def testDecodeWithKeyEqualZero(self):
        result = make_cipher(0)
        self.assertEqual(decode('abc', result), 'abc')

    def testWithCipher(self):
        result = make_cipher(5)
        self.assertEqual(result[0], 'f')

    def testWithCipherValueChange(self):
        result = make_cipher(13)
        self.assertEqual(result[0], 'n')

    def testForMessageValue(self):
        MESSAGE = 'Clean Code'
        b = 'Clean Code'
        self.assertEqual(MESSAGE, b, 'comparison')

if __name__ == '__main__':
    unittest.main()
