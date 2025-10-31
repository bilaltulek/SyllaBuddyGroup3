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
if __name__ == '__main__':

    unittest.main()
