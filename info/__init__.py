# 16. extract business logic from manage.py to a new file
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, g, render_template
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_wtf.csrf import generate_csrf
from redis import StrictRedis
from config import config


# 19. extracthttp://58.222.34.72:8080/# the db from create_app

db = SQLAlchemy()
redis_store = None # type: StrictRedis


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
    global redis_store
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT, decode_responses=True)
    # 7. start CSRF protection for server validation
    CSRFProtect(app)
    # 8. set session to be stored in redis
    Session(app)
    #添加自定义过滤器
    from info.utils.common import do_index_class
    app.add_template_filter(do_index_class, "index_class")

    from info.utils.common import user_login_data
    @app.errorhandler(404)
    @user_login_data
    def page_not_fount(e):
        user = g.user
        data = {"user": user.to_dict() if user else None}
        return render_template('news/404.html', data=data)


    @app.after_request
    def after_request(response):
        # 生成随机的csrf_token的值
        csrf_token = generate_csrf()
        # 设置一个cookie
        response.set_cookie("csrf_token", csrf_token)
        return response

    from info.modules.index import index_blue
    app.register_blueprint(index_blue)

    from info.modules.passport import passport_blue
    app.register_blueprint(passport_blue)

    from info.modules.news import news_blue
    app.register_blueprint(news_blue)

    from info.modules.profile import profile_blue
    app.register_blueprint(profile_blue)

    from info.modules.admin import admin_blue
    app.register_blueprint(admin_blue, url_prefix="/admin")

    return app
