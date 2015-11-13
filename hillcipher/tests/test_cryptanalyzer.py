""" Test suite for the HillCipher module."""

from unittest import TestCase

import hillcipher
import numpy as np

class TestCryptanalyzer(TestCase):

    plaintext28 = "hitherehowareyou|iamfine|sendmanymenttothebatteredplainstonight|theambushisabouttogodown" 
    plaintext30 = "hithere|howareyou|iamfine|sendmanymenttothebatteredplainstonight|theambushisabouttogodown|" 

    def check_cryptanalysis(self, hc, plaintext):
        ciphertext = hc.encryptText(plaintext)
        key = hillcipher.cryptanalyzer.cryptanalyzeHillcipher(plaintext, ciphertext)
        self.assertTrue((key == hc.getKey()).all())

    def test_2_key_crptanalysis(self):
        hc = hillcipher.HillCipher()
        hc.setKey(np.matrix('11 8; 3 7'))
        self.check_cryptanalysis(hc, self.plaintext28)
        hc.setKey(np.matrix('3 3; 2 5'))
        self.check_cryptanalysis(hc, self.plaintext30)

    def test_known_3_key(self):
        hc = hillcipher.HillCipher()
        hc.setKey(np.matrix('6 24 1; 13 16 10; 20 17 15'))
        self.check_cryptanalysis(hc, self.plaintext30)
        hc.setKey(np.matrix('9 21 1; 13 12 10; 23 17 15'))
        self.check_cryptanalysis(hc, self.plaintext30)

    """
    def test_known_4_key(self):
        hc = hillcipher.HillCipher()
        hc.setKey(np.matrix('9 21 1 2; 13 12 10 5; 23 17 15 7;7 6 27 3'))
        self.check_cryptanalysis28(hc)
    """

    def test_known_5_key(self):
        hc = hillcipher.HillCipher()
        hc.setKey(np.matrix('9 21 1 2 7; 13 12 10 5 2; 23 17 15 7 4;7 6 27 3 5;3 5 17 12 24'))
        self.check_cryptanalysis(hc, self.plaintext30)
