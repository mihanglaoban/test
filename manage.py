import base64
import os

from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask_script import Manager


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


app = Flask(__name__)

# 2. the app loads config the class object
app.config.from_object(Config)
# 3. add mySQL
db = SQLAlchemy(app)
# 5. initialize redis object
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 7. start CSRF protection for server validation
CSRFProtect(app)
# 8. set session to be stored in redis
Session(app)
# 11. create manager to enable command line control
manager = Manager(app)


@app.route('/')
def index():
    session['name'] = "itheima"
    return "success!"


def main():
    #12. use manager to run the app
    manager.run()


if __name__ == "__main__":
    main()
