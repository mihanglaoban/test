# 16. extract business logic from manage.py to a new file
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis

from config import config

app = Flask(__name__)

# 2. the app loads config the class object
app.config.from_object(config['development'])
# 3. add mySQL
db = SQLAlchemy(app)
# 5. initialize redis object
redis_store = StrictRedis(host=config['development'].REDIS_HOST, port=config['development'].REDIS_PORT)
# 7. start CSRF protection for server validation
CSRFProtect(app)
# 8. set session to be stored in redis
Session(app)
