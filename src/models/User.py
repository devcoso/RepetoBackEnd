from werkzeug.security import generate_password_hash, check_password_hash

class User () :
    def __init__(self, id, name, email, password, points=0,):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.points = points
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def hash_password(self, password):
        return generate_password_hash(password, method='pbkdf2')
    def verify_user(self):
        if(len(self.password) < 8 or len(self.password) > 16):
            return False
        if(len(self.name) < 3 or len(self.name) > 61):
            return False
        if(len(self.email) > 61):
            return False
        return True