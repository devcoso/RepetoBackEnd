import uuid
#Database
from src.database.db_mysql import get_connection
#Models
from src.models.User import User
#Utils
from src.utils.Security import Security
from src.utils.EmailSender import EmailSender


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
    @classmethod
    def forgot_password(self, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql="SELECT id FROM users WHERE email=%s"
                cursor.execute(sql, (user.email,))
                connection.commit()
                row=cursor.fetchone()
            connection.close()
            if row != None:
                token = uuid.uuid4().hex
                connection = get_connection()
                with connection.cursor() as cursor:
                    sql="UPDATE users SET token=%s WHERE email=%s"
                    cursor.execute(sql, (token, user.email))
                    connection.commit()
                    row=cursor.fetchone()
                connection.close()
                EmailSender.send_recovery_email(user.email, token)
                return {
                    'error': False,
                    'message': 'Se ha enviado un correo con las instrucciones'
                }
            else:
                return {
                    'error': True,
                    'message': 'El correo no está registrado'
                }
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def reset_password(self, token, password):
        if(len(password) < 8 or len(password) > 16):
            return {
                'error': True,
                'message': 'Contraseña inválido'
            }
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql="SELECT id, email  FROM users WHERE token=%s"
                cursor.execute(sql, (token))
                connection.commit()
                row=cursor.fetchone()
            connection.close()
            if row != None:
                user = User(row[0], None, row[1], None)
                user.password = user.hash_password(password)
                connection = get_connection()
                with connection.cursor() as cursor:
                    sql="UPDATE users SET password=%s, token=NULL WHERE id=%s"
                    cursor.execute(sql, (user.password, user.id))
                    connection.commit()
                    row=cursor.fetchone()
                connection.close()
                return {
                    'error': False,
                    'message': 'Contraseña actualizada'
                }
            else:
                return {
                    'error': True,
                    'message': 'Token inválido'
                }
        except Exception as ex:
            raise Exception(ex)