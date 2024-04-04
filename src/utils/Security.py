import uuid
from decouple import config

import datetime
import jwt
import pytz

class Security():

    tz = pytz.timezone("America/Lima")

    @classmethod
    def generate_token(cls,authenticated_user,segundos):
        try:
            payload = {
                'iat': datetime.datetime.now(tz=cls.tz),
                'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(seconds=segundos),
                'Oid': authenticated_user[0],
                'Usuario': authenticated_user[1],
            }
            return jwt.encode(payload, config('JWT_SECRET_KEY'), algorithm='HS256')
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def verify_token(cls, headers):
        try:
            if 'Authorization' in headers.keys():
                authorization = headers['Authorization']                
                try:
                    payload = jwt.decode(authorization, config('JWT_SECRET_KEY'), algorithms=["HS256"])
                    
                    return payload
                except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                    return None

            return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def validar_uuid(cadena):
        try:
            print(uuid.UUID(cadena))
            # Intenta analizar la cadena como un UUID
            uuid_obj = uuid.UUID(cadena)
            return True
        except ValueError:
            # Si ocurre un error, la cadena no es un UUID válido
            return False