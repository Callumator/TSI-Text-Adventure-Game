import unittest

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from LogIn import *

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = user("testuser", "password123")

    def test_login(self):
        self.assertEqual(self.login.login(), "You are logged in")

    def test_get_password(self):
        self.assertEqual(self.login.get_password(), "testuser")

if __name__ == '__main__':
    unittest.main()