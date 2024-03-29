#Database
from src.database.db_mysql import get_connection

from src.models.User import User
from src.utils.Security import Security

class AuthService():
    @classmethod
    def login(self, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql="SELECT id, name, email, password, points FROM users WHERE email=%s"
                cursor.execute(sql, (user.email,))
                connection.commit()
                row=cursor.fetchone()
            connection.close()
            if row != None:
                userDB = User(row[0], row[1], row[2], row[3], row[4])
                if(userDB.check_password(user.password)):
                    token = Security.generate_token(userDB)
                    return {
                        'id': userDB.id,
                        'name': userDB.name,
                        'email': userDB.email,
                        'points': userDB.points,
                        'jwt': token
                    }
                else:
                    return None
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def register(self,  user):
        if(not user.verify_user()):
            return {
                'error': True,
                'message': 'Datos no válidos'
            }
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql="SELECT id FROM users WHERE email=%s"
                cursor.execute(sql, (user.email,))
                connection.commit()
                row=cursor.fetchone()
            connection.close()
            if row == None:
                user.password = user.hash_password(user.password)
                connection = get_connection()
                with connection.cursor() as cursor:
                    sql="INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (user.name, user.email, user.password))
                    connection.commit()
                    user.id = cursor.lastrowid
                connection.close()
                token = Security.generate_token(user)
                return {
                    'error': False,
                    'user': {
                        'id': user.id,
                        'name': user.name,
                        'email': user.email,
                        'points': 0,
                        'jwt': token
                    },
                }
            else:
                return {
                    'error': True,
                    'message': 'El correo ya está registrado'
                }
        except Exception as ex:
            raise Exception(ex)