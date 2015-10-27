""" Main Hill Cipher object."""

import numpy as np

class HillCipher():

    def __init__(self):
        """ Setup the object."""
        self.key = np.matrix('1 2; 3 4')

    def getKey(self):
        """ Return key being used for encryption."""
        return self.key

    def setRandomKey(self, dim=2):
        """ Set a random encryption key of specified dimension.

        INPUT
        ---------
        dim -- the dimension of matrix

        Creates a valid random key for encryption. Here, valid means that the matrix is invertible.
        """

        self.key = np.random.randint(25, size=(dim, dim))
        if not np.linalg.det(self.key):
            self.setRandomKey(dim)
