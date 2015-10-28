""" Test suite for the HillCipher module."""

from unittest import TestCase

import hillcipher
import numpy as np

class TestHillCipher(TestCase):

    def test_key_is_valid(self):
        hc = hillcipher.HillCipher()
        hc.setRandomKey(2)
        self.assertTrue(np.linalg.det(hc.getKey()))

