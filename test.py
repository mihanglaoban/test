# -*- coding: utf-8 -*-
# @Author  : junjunzai
# @Email   : junjunzai@163.com
# @File    : test.py
# @Software: PyCharm
import datetime
import random

from info import db
from info.models import User
from manage import app


def add_test_users():
    users = []
    now = datetime.datetime.now()
    for num in range(0, 10000):
        try:
            user = User()
            user.nick_name = "%011d" % num
            user.mobile = "%011d" % num
            #密码11111111
            user.password_hash = "pbkdf2:sha256:50000$yfNUh8hF$457ca3de6b07e288e0a3051dcd2dfe7a446c01dd4979a8a66b294cdd6eef9e5e"
            user.last_login = now - datetime.timedelta(seconds=random.randint(0, 2678400))
            users.append(user)
            print(user.mobile)
        except Exception as e:
            print(e)
    # 手动开启一个app的上下文
    with app.app_context():
        db.session.add_all(users)
        db.session.commit()
    print('OK')


if __name__ == '__main__':
    add_test_users()
