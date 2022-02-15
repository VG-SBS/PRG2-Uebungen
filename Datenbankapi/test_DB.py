import unittest
from datenbankapi import DB
from main import *
global first

class TestDB(unittest.TestCase):
    def setUp(self):
        self.db = DB()
        self.ret = ""
        self.ret2 = 0

    def test_createPlayer(self):

        self.ret = self.db.createPlayer("Hans")
        second = -1
        message = "pk user Hans wrong"

        self.assertGreater(self.ret, second, message)

    def test_getPlayer(self):
        self.db2 = DB()
        self.ret = self.db.createPlayer("Hans")
        test = self.db2.getPlayer(self.ret)
        second = "Hans"
        message = "Name Falsch"
        self.assertEqual(test,second,message)




if __name__ == '__main__':
    unittest.main()