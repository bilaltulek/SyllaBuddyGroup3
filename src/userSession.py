import os
import platform
import subprocess



#this is a vertical slice of the usersession class, does not contain every other component that will
#interact with the function in the future

class UserSession:
    def endUserSession(self, userName, isLoggedIn, networkState):
        if isLoggedIn and networkState != False and networkState != "NULL":
            print("Logged out")
            return True
        elif( isLoggedIn == False):
            print("No valid session, please log in")
            return False
        elif(networkState == False):
            print("Connection lost, please check connection")
            return False
        elif networkState == "NULL" or userName == "NULL" or isLoggedIn == "NULL":
            print("Exceptional error, please try again")
            return False
    def testConnection(self) -> bool:
        params = ['-c', '1', '-w', '2']
        command = ['ping'] + params + ['google.com']
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if result.returncode == 0:
            print("Stable connection")
            return True
        else:
            print("Connection lost, please check connection")
            return False


#instance = UserSession()
#instance.testConnection()




