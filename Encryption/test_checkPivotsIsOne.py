from unittest import TestCase

import numpy as np

from Encryption import Matrix


class TestCheckPivotsIsOne(TestCase):
    def test_checkPivots1(self):
        I = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]])
        self.assertTrue(Matrix.checkPivots(I))

    def test_checkPivots2(self):
        M = np.array([
            [1, 0, 0, 0],
            [0, 1, 6, 0],
            [0, 0, 0, 0]])
        self.assertFalse(Matrix.checkPivots(M))

