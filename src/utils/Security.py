import pytz
import datetime
import jwt
from decouple import config

class Security() :

    tz = pytz.timezone('America/Mexico_City')


    @classmethod
    def generate_token(cls, authenticate_user):
        payload = {
            'id': authenticate_user.id,
            'name': authenticate_user.name,
            'email': authenticate_user.email,
            'points': authenticate_user.points,
            'iat': datetime.datetime.now(tz=cls.tz),
            'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(days=1),
        }
        return jwt.encode(payload, config('JWT_SECRET_KEY'), algorithm='HS256')
    
    @classmethod
    def verify_token(cls, headers):
        if 'Authorization' not in headers:
            return None
        autorization = headers['Authorization']
        encoded_token = autorization.split(' ')[1]
        print (encoded_token)
        try:
            return jwt.decode(encoded_token, config('JWT_SECRET_KEY'), algorithms=['HS256'])
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, jwt.DecodeError):
            return None