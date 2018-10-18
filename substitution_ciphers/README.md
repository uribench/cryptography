# Substitution Ciphers

In cryptography, a substitution cipher is an encryption technique based on a lookup-table
translating from the letters of a plain message to a predefined set of other letters, called cipher.

The decryption is done using the same lookup-table in the reverse direction.

## Cipher Composition

If we think of the lookup-table for encryption and decryption as a map of key-value pairs,
then for encryption, the keys are the alphabet of the language being used in the plain message, and 
the values are the cipher.

For decryption, the lookup-table maps in the reverse direction, in which the keys are the cipher and 
the values are the alphabet of the language being used in the plain message.

The source code provided here for substitution ciphers demonstrate the use of several common method
to compose the cipher for the encryption and decryption:

1. Caesar cipher
2. Deranged alphabet cipher

## Encoder and Decoder Source Code

The source code for the encoder and decoder using this technique is common for all the different 
ciphers that are provided here to demonstrate the substitution ciphers.

The main line of the encoder in `encoder.py` is:

```python
    return message.translate(str.maketrans(letters, ''.join(cipher)))
```

This code does the heavy lifting of the encoder. It uses the Python `translate` method that gets
a lookup-table from the English alphabet (lower-case letters followed by upper-case letters) to a 
given cipher that was composed elsewhere in the code (described separately).

Not surprisingly, the main line of the decoder in `decoder.py` does the opposite:

```python
    return secret.translate(str.maketrans(''.join(cipher), letters))
```

Here, the translation is from the cipher to the English alphabet.

## Simple Complete Example Programs

The following example programs are provided:

1. `main_caesar_cipher.py`
2. `main_deranged_alphabet_cipher.py`

They simply show the usage of composing a cipher in one of the provided substitution ciphers, then 
using the encryption on a simple message with the generated cipher, and finally decrypting the 
secret back using the same cipher.