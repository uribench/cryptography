import unittest
from src.encoder_decoder_2 import *

class encoder_decoder_1(unittest.TestCase):

    def testEncodeWithNullString(self):
        self.assertEqual(encode('', CIPHER), '', 'Null value')

    def testEncodeWithCustomMessage(self):
        self.assertEqual(encode('helloworld', CIPHER), 'bTffiqilfR', 'custom message')

    def testEncodeWithActualMessage(self):
        self.assertEqual(encode(MESSAGE, CIPHER), 'vTnnTl zQmnTl zilTpTl', 'actual Message')

    def testDecodeWithCustomMessage(self):
        self.assertEqual(decode('bTffi Kbcfcjm', CIPHER), 'hello Philips')

    def testDecodeWithOriginalMessage(self):
        self.assertEqual(decode(SECRET,CIPHER), MESSAGE, 'original message')

    def testCipherFunctionWithNumericValue(self):
        with self.assertRaises(AttributeError): make_cipher(0)

    def testCipherFunctionWithAlphanumericValue(self):
        with self.assertRaises(SystemExit): make_cipher('A0')

    def testCipherWithCorrectValue(self):
        result = make_cipher('QWERTY')
        self.assertEqual('Q', result[0], 'Correct Value')

    def testCipherWithDifferentValue(self):
        result = make_cipher('PHILIPS')
        self.assertEqual('b', result[6])

if __name__ == '__main__':
    unittest.main()
