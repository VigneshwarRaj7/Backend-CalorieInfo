#This class provides a model to create a user with properties of username and password.
class User:
    def __init__(self, userName, password):
        self._userName = userName
        self._password = password

    def get_userName(self):
        return self._userName  
        
    def get_password(self):
        return self._password    