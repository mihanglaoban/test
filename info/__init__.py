# 16. extract business logic from manage.py to a new file
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from config import config

from info.modules.index import index_blue

# 19. extract the db from create_app
db = SQLAlchemy()


# 21. set up log
def setup_log(config_name):
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


# 18. encapsulate the configurations
def create_app(config_name):
    app = Flask(__name__)

    # 22. start setting up log
    setup_log(config_name)
    # 2. the app loads config the class object
    app.config.from_object(config[config_name])
    # 3. add mySQL
    # db = SQLAlchemy(app)

    # 20. initiate app
    db.init_app(app)
    # 5. initialize redis object
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    # 7. start CSRF protection for server validation
    CSRFProtect(app)
    # 8. set session to be stored in redis
    Session(app)

    app.register_blueprint(index_blue)

    return app
