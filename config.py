from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY ="CLAVESECRETA"
    SESSION_COOKIE_SECURE=False
    
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="mysql+pymsql://root:root@127.0.0.1/bdigs803"
    SQLALCHEMY_TRACK_MODIFICATIONS=False