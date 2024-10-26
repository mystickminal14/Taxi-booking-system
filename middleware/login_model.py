class CustomerLogin:
    def __init__(self, _username=None, _password=None):
       
        self.username = _username
        self.password = _password

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password
