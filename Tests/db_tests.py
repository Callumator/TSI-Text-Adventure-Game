import unittest
from ReadDB import *

class TestDB(unittest.TestCase):

    def setUp(self):
        self.db = database_manager(":memory:")

    def tearDown(self):
        self.db.tearDown()