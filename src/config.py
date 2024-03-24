from decouple import config

class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = config('MYSQL_HOST')
    MYSQL_DB = config('MYSQL_DB')
    MYSQL_USER = config('MYSQL_USER')
    MYSQL_PASSWORD = config('MYSQL_PASSWORD')

config = {
    'development' : DevelopmentConfig
}