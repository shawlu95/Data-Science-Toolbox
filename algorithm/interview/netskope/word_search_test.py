# python3 -m unittest word_search_test.py
import unittest
from word_search import exist

class TestWordSearch(unittest.TestCase):
    board = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

    def test_true(self):
        self.assertTrue(exist(self.board, ""))
        self.assertTrue(exist(self.board, "ESE"))
        self.assertTrue(exist(self.board, "ASA"))

        self.assertTrue(exist(self.board, "ABCE"))
        self.assertTrue(exist(self.board, "ADEE"))

        self.assertTrue(exist(self.board, "AFE"))
        self.assertTrue(exist(self.board, "BCE"))

        self.assertTrue(exist(self.board, "BFCE"))
        self.assertTrue(exist(self.board, "BFEE"))

    def test_false(self):
        self.assertFalse(exist(self.board, "ECCE"))
        self.assertFalse(exist(self.board, "ADFC"))
        self.assertFalse(exist([], "ADFC"))
        self.assertFalse(exist([[]], "ADFC"))
