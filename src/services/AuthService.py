from models.User import User
import uuid

class AuthService():
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql="SELECT id, name, email, password, points FROM users WHERE email=%s"
            cursor.execute(sql, (user.email,))
            row=cursor.fetchone()
            if row != None:
                userDB = User(row[0], row[1], row[2], row[3], row[4])
                if(userDB.check_password(user.password)):
                    token = uuid.uuid4().hex
                    update_sql = "UPDATE users SET remember_token=%s WHERE id=%s"
                    cursor.execute(update_sql, (token, userDB.id))
                    db.connection.commit()
                    return {
                        'id': userDB.id,
                        'name': userDB.name,
                        'email': userDB.email,
                        'points': userDB.points,
                        'remember_token': token
                    }
                else:
                    return None
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def register(self, db,  user):
        if(not user.verify_user()):
            return {
                'error': 'Invalid user data'
            }
        try:
            cursor = db.connection.cursor()
            sql="SELECT id FROM users WHERE email=%s"
            cursor.execute(sql, (user.email,))
            row=cursor.fetchone()
            if row == None:
                user.password = user.hash_password(user.password)
                token = uuid.uuid4().hex
                sql="INSERT INTO users (name, email, password, remember_token) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (user.name, user.email, user.password, token))
                db.connection.commit()
                return {
                    'id': cursor.lastrowid,
                    'name': user.name,
                    'email': user.email,
                    'points': 0,
                    'remember_token': token
                }
            else:
                return None
        except Exception as ex:
            raise Exception(ex)