import unittest
from login import Login 

class concreteCasesLogin(unittest.TestCase):

    def test_loginUsernameTC1(self):
        self.assertEqual(Login.login("John", "Password123!"), "Login Successful")
    
    def test_loginUsernameTC2(self):
        self.assertEqual(Login.login("Johnny123", "Password123!"), "Username doesnt exist")

    def test_loginUsernameTC3(self):
        self.assertEqual(Login.login("", "Password123!"), "Invalid Username")

if __name__ == "__main__":
    unittest.main()