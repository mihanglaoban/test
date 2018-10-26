# extract config class from manage.py to a new file
from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import Config

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
# 13. use migrate to relate the app and mySQL
Migrate(app, db)
# 14. add migrate command to manager
manager.add_command('db', MigrateCommand)

@app.route('/')
def index():
    session['name'] = "itheima"
    return "success!"


def main():
    #12. use manager to run the app
    manager.run()


if __name__ == "__main__":
    main()
