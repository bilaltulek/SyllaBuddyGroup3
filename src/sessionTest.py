import unittest
from userSession import *
userInstance = UserSession()
class TestBase(unittest.TestCase):
    def test_Base(self):
        testCase = userInstance.endUserSession("Cris", True, True)
        self.assertEqual(testCase, True, 'base case, all correct inputs')
class testExpired(unittest.TestCase):
    def test_Expired(self):
        testCase = userInstance.endUserSession("Cris", False, True)
        self.assertEqual(testCase, False, 'correctly informs user to log in as there is no valid session')

class testNetwork(unittest.TestCase):
    def test_Network(self):
        testCase = userInstance.endUserSession("Cris", True, False)
        self.assertEqual(testCase, False, 'correctly ends session as there is no connection')
class nullName(unittest.TestCase):
    def test_nName(self):
        testCase = userInstance.endUserSession("NULL", True, False)
        self.assertEqual(testCase, False, 'correctly ends instance due to null exception')
class nullLogin(unittest.TestCase):
    def test_nLogin(self):
        testCase = userInstance.endUserSession("Cris", "NULL", False)
        self.assertEqual(testCase, False, 'correctly ends instance due to null exception')
class nullNetwork(unittest.TestCase):
    def test_nNetwork(self):
        testCase = userInstance.endUserSession("cris", True, "NULL")
        self.assertEqual(testCase, False, 'correctly ends instance due to null exception')
if __name__ == '__main__':

    unittest.main()

