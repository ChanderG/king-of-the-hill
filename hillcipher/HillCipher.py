""" Main Hill Cipher object."""

import numpy as np
import helpers

class HillCipher():

    def __init__(self):
        """ Setup the object."""
        self.key = np.matrix('11 8; 3 7')

    def getKey(self):
        """ Return key being used for encryption."""
        return self.key

    def setKey(self, key):
        """ Set key matrix."""
        self.key = key

    def setRandomKey(self, dim=2):
        """ Set a random encryption key of specified dimension.

        INPUT
        ---------
        dim -- the dimension of matrix

        Creates a valid random key for encryption. Here, valid means that the matrix is invertible.
        """

        self.key = np.random.randint(29, size=(dim, dim))
        inv = helpers.inversematrix(self.key, 29)
        if inv == None:
            self.setRandomKey(dim)

    def encryptText(self, plaintext):
        """ Encrypt a given plaintext string using key. 

        INPUT
        ---------
        plaintext -- string plaintext

        Returns the cipher text. The cipher text, for historic reasons is completely in UPPER case. That is, the operation does not preserve case of the input.

        Also, any and all special characters, numbers and in fact anything other than alpha characters are completely removed/ignored.

        For now assumes that the length of input plaintext is a multiple of key dimension.
        """
        return self._encrypt(plaintext, self.key)

    def decryptText(self, ciphertext):
        """ decrypt a given ciphertext string using key. 

        INPUT
        ---------
        ciphertext -- string ciphertext

        Returns the plain text. The plain text, for historic reasons is completely in LOWER case. That is, the operation does not preserve case of the input.

        Also, any and all special characters, numbers and in fact anything other than alpha characters are completely removed/ignored.

        For now assumes that the length of input ciphertext is a multiple of key dimension.
        """

        key = helpers.inversematrix(self.key, 29)
        if key == None:
            # key is not invertible
            print "Key is not valid."
            return None
        print key
        return self._encrypt(ciphertext, key)

    def _encrypt(self, plaintext, key):
        """ Actual encryption function.
        """

        # filter out special characters, numbers etc
        #alphachars = filter(lambda x: x.isalpha(), list(plaintext))
        #plaintext = "".join(alphachars)

        # if length is not a perfect multiple, don't handle it 
        if len(plaintext) % key.shape[0] != 0 and key.shape[0] % len(plaintext) != 0:
            print "Length is not perfect multiple of key dimension."
            return None

        plaintext = plaintext.lower()

        # convert to numbers in range [0, 25]
        ptchars = list(plaintext)
        ptnos = map(lambda x: ord(x) - ord('a'),ptchars)

        dim = key.shape[0]

        # array of cpher
        ctnos = []

        for i in xrange(0, len(ptchars), dim):
            # blocks of dim size
            block = ptnos[i:i+dim]

            # make a matrix out of the array
            plainblock = np.matrix(block)

            # encrypt the block
            cipherblock = plainblock*key

            # extract the numbers
            ciphernos = cipherblock.getA1().tolist()

            # add to ciphertext full list
            ctnos += ciphernos

        # apply mod to numbers
        ctnos = map(lambda x: x%29, ctnos)

        # map back to characters
        ctchars = map(lambda x: chr(x + ord('a')), ctnos)

        # create the text back from the characters
        ciphertext = "".join(ctchars)

        return ciphertext
