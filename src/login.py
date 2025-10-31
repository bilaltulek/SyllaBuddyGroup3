import bcrypt
class Login:
    existingUsers = {
        "John": bcrypt.hashpw(b"Password123!", bcrypt.gensalt()),
        "Mary": bcrypt.hashpw(b"This@999", bcrypt.gensalt()),
        "Coolman": bcrypt.hashpw(b"Secret&123", bcrypt.gensalt()),
    }

    def __init__(self, username, email, password):
        self._username = username
        self._password = password

    def getUsername(self):
        return self._username
    
    def checkExistingUsernames(self):
        for i, self._username in enumerate(self.existingUsernames):
            if self._username == self.existingUsernames[i]:
                return True
            
        return False

    def authenticate(self):
        if self._username not in self.existingUsers:
            return False
        
        if (bcrypt.checkpw(self._password.encode('utf-8'), self.existingUsers[self._username])):
            return True
        else:
            return False

    @staticmethod   
    def login(username, password):

        if len(username) < 4 or " " in username:
            return "Invalid Username"
            
        if username not in Login.existingUsers:
            return "Username doesnt exist"
        
        if (bcrypt.checkpw(password.encode('utf-8'), Login.existingUsers[username])):
            return "Login Successful"
        else:
            return "Invalid Password"
        
    

        
