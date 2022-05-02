class user:
    def __init__(self, name, ID, role, username, password):
        self.name = name
        self.ID = ID
        self.role = role
        self.username = username
        self.password = password
    
    def get_name(self):
        return self.name
    
    def set_name(self, new):
        self.name = new

    def get_ID(self):
        return self.ID
    
    def set_ID(self, new):
        self.ID = new
    
    def get_username(self):
        return self.username
    
    def set_username(self, new):
        self.username = new
    
    def get_password(self):
        return self.password

    def set_password(self, new):
        self.password = new

    def get_role(self):
        return self.role