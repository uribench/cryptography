import unittest
from caesar_cipher.src.encoder_decoder import *

class encoder_decoder(unittest.TestCase):

    def testEncryptWithNullString(self):
        self.assertEqual(encode('', cipher), '', 'Null value')

    def testEncryptWithCustomMessage(self):
        self.assertEqual(encode('helloworld', cipher), 'mjqqtBtwqi', 'custom message')

    def testEncryptWithActualMessage(self):
        self.assertEqual(encode(MESSAGE, cipher), 'Hqjfs Htij', 'actual message')

    def testcipherLength(self):
        self.assertEqual(52, len(cipher), 'Length mismatch')

    def testDecodeWithCustomMessage(self):
        self.assertEqual(decode('mjqqtBtwqi', cipher), 'helloworld', 'custom message')

    def testDecodeWithOriginalMessage(self):
        self.assertEqual(decode(secret, cipher), MESSAGE, 'original message')

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
