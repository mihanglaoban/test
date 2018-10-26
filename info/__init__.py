# 16. extract business logic from manage.py to a new file
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis

from config import config


# 19. extract the db from create_app
db = SQLAlchemy()


# 18. encapsulate the configurations
def create_app(config_name):
    app = Flask(__name__)

    # 2. the app loads config the class object
    app.config.from_object(config[config_name])
    # 3. add mySQL
    # db = SQLAlchemy(app)

    # 19. initiate app
    db.init_app(app)
    # 5. initialize redis object
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    # 7. start CSRF protection for server validation
    CSRFProtect(app)
    # 8. set session to be stored in redis
    Session(app)

    return app
