""" Test suite for the HillCipher module."""

from unittest import TestCase

import hillcipher
import numpy as np

class TestHillCipher(TestCase):

    def test_key_is_valid(self):
        hc = hillcipher.HillCipher()
        hc.setRandomKey(2)
        self.assertTrue(hillcipher.helpers.inversematrix(hc.getKey(), 29) != None)

    def test_known_2_key(self):
        hc = hillcipher.HillCipher()
        hc.setKey(np.matrix('11 8; 3 7'))
        text = 'july'
        self.assertTrue(text == hc.decryptText(hc.encryptText(text)))
        hc.setKey(np.matrix('3 3; 2 5'))
        self.assertTrue(text == hc.decryptText(hc.encryptText(text)))

    def test_known_3_key(self):
        hc = hillcipher.HillCipher()
        hc.setKey(np.matrix('6 24 1; 13 16 10; 20 17 15'))
        text = 'actbatman'
        self.assertTrue(text == hc.decryptText(hc.encryptText(text)))
        hc.setKey(np.matrix('9 21 1; 13 12 10; 23 17 15'))
        self.assertTrue(text == hc.decryptText(hc.encryptText(text)))

    def test_known_4_key(self):
        hc = hillcipher.HillCipher()
        hc.setKey(np.matrix('9 21 1 2; 13 12 10 5; 23 17 15 7;7 6 27 3'))
        text = 'johnmaryshawjeff'
        self.assertTrue(text == hc.decryptText(hc.encryptText(text)))

    def test_known_5_key(self):
        hc = hillcipher.HillCipher()
        hc.setKey(np.matrix('9 21 1 2 7; 13 12 10 5 2; 23 17 15 7 4;7 6 27 3 5;3 5 17 12 24'))
        text = 'chuckcaseysarah'
        self.assertTrue(text == hc.decryptText(hc.encryptText(text)))
