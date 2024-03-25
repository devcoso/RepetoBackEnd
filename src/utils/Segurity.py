from decouple import config

import datetime
import jwt
import pytz
import traceback

# Logger
from src.utils.Logger import Logger


class Security():

    secret = config('JWT_KEY')

    @classmethod
    def generate_token(data,segundos_validos=60*60):
        try:
            fecha_expiracion = datetime.datetime.utcnow() + datetime.timedelta(seconds=segundos_validos)
            payload = {
                'usuario': data,
                'exp': fecha_expiracion,
            }
            token = jwt.encode(payload, secret_key, algorithm='HS256')
            return token
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

    @classmethod
    def verify_token(token):
        try:
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            print("El token ha expirado.")
            return None
        except jwt.InvalidTokenError:
            print("El token es inválido.")
            return None