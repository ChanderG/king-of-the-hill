""" Main Hill Cipher object."""

import numpy as np

class HillCipher():

    def __init__(self):
        """ Setup the object."""
        self.key = np.matrix('1 2; 3 4')

    def getKey(self):
        """ Return key being used for encryption."""
        return self.key
