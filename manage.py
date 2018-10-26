from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis


class Config(object):
    # 1.create a config class
    DEBUG = True
    # 4. configure mySQL
    SQLALCHEMY_DATABASE_URI = "mysql://tar:tar@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 6. configure redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"


app = Flask(__name__)

# 2. the app loads config the class object
app.config.from_object(Config)
# 3. add mySQL
db = SQLAlchemy(app)
# 5. initialize redis object
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 7. start CSRF protection for server validation
CSRFProtect(app)


@app.route('/')
def index():
    return "success!"


def main():
    app.run()


if __name__ == "__main__":
    main()
