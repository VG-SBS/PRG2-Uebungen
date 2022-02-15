import unittest
from datenbankapi import DB
from main import *

class TestDB(unittest.TestCase):
    def setUp(self):
        self.db = DB()

    def test_createPlayer(self):
        first = self.db.createPlayer("Hans")

        second = -1

        message = "pk user Hans wrong"

        self.assertGreater(first, second, message)

if __name__ == '__main__':
    unittest.main()