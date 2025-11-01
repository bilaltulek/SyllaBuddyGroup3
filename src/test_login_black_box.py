import unittest
from login import Login 


class blackBoxLogin(unittest.TestCase):

    def test_loginBCUsernameTC1(self):
        self.assertEqual(Login.login("John", "Password123!"), "Login Successful")
    
    def test_loginBCUsernameTC2(self):
        self.assertEqual(Login.login("Johnny123", "Password123!"), "Username doesnt exist")

    def test_loginBCUsernameTC3(self):
        self.assertEqual(Login.login("", "Password123!"), "Invalid Username")

    def test_loginBCUsernameTC4(self):
        self.assertEqual(Login.login("Joh", "Password123!"), "Invalid Username")

    def test_loginBCPasswordTC5(self):
        self.assertEqual(Login.login("John", "P$"), "Invalid Password")

    def test_loginBCPasswordTC6(self):
        self.assertEqual(Login.login("John", ""), "Invalid Password")

if __name__ == "__main__":
    unittest.main()
    

    

