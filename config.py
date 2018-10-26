import base64
import os

from redis import StrictRedis


class Config(object):
    # 1.create a config class
    DEBUG = True
    # 4. configure mySQL
    SQLALCHEMY_DATABASE_URI = "mysql://tar:tar@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 10. set a secret key for session
    SECRET_KEY = base64.b16encode(os.urandom(48)).decode("utf8")

    # 6. configure redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"

    # 9. session configuration
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400 * 2

# 17. create different configuration for different mode
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    DEBUG = True
    TESTING = True

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}
