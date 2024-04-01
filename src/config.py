from decouple import config


class Config:
    SECRET_KEY=config('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUF= True


config = {
    'development': DevelopmentConfig
}