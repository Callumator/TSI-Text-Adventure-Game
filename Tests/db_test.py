import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ReadDB import database_manager



class TestDB(unittest.TestCase):

    def setUp(self):
        self.db = database_manager(":memory:")

    def tearDown(self):
        self.db.close_connection()

    def test_insert_user(self):
        self.db.insert_user('email1', 'Fname1', 'Lname1', 'password1')
        self.db.insert_user('email2', 'Fname2', 'Lname2', 'password2')
        Customers = self.db.get_users()
        self.assertEqual(len(Customers), 2)
        self.assertEqual(Customers[0][0], 'email1')
        self.assertEqual(Customers[1][0], 'email2')
        self.assertEqual(Customers[0][1], 'Fname1')
        self.assertEqual(Customers[1][1], 'Fname2')
        self.assertEqual(Customers[0][2], 'Lname1')
        self.assertEqual(Customers[1][2], 'Lname2')
        self.assertEqual(Customers[0][3], 'password1')
        self.assertEqual(Customers[1][3], 'password2')

if __name__ == '__main__':
    unittest.main()