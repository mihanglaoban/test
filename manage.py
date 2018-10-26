from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    # 1.create a config class
    DEBUG = True
    # 4. configure mySQL
    SQLALCHEMY_DATABASE_URI = "mysql://tar:tar@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)

# 2. the app loads config the class object
app.config.from_object(Config)
# 3. add mySQL
db = SQLAlchemy(app)


@app.route('/')
def index():
    return "success!"


def main():
    app.run()


if __name__ == "__main__":
    main()
