# python3 -m unittest word_search_test.py
import unittest
from word_search import exist

class TestWordSearch(unittest.TestCase):
    board1 = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    
    board2 = [
        ["C", "B", "A", "N"],
        ["A", "O", "O", "L"],
        ["N", "N", "N", "A"]
    ]

    def test_true(self):
        self.assertTrue(exist(self.board1, ""))
        self.assertTrue(exist(self.board1, "ESE"))
        self.assertTrue(exist(self.board1, "ASA"))

        self.assertTrue(exist(self.board1, "ABCE"))
        self.assertTrue(exist(self.board1, "ADEE"))

        self.assertTrue(exist(self.board1, "AFE"))
        self.assertTrue(exist(self.board1, "BCE"))

        self.assertTrue(exist(self.board1, "BFCE"))
        self.assertTrue(exist(self.board1, "BFEE"))

        self.assertTrue(exist(self.board2, "BON"))
        self.assertTrue(exist(self.board2, "BAN"))
        self.assertTrue(exist(self.board2, "COOL"))
        self.assertTrue(exist(self.board2, "ANNA"))
        self.assertTrue(exist(self.board2, "ANNNA"))

    def test_false(self):
        self.assertFalse(exist([], "ADFC"))
        self.assertFalse(exist([[]], "ADFC"))

        self.assertFalse(exist(self.board1, "ECCE"))
        self.assertFalse(exist(self.board1, "ADFC"))

        self.assertFalse(exist(self.board1, "LOOB"))
