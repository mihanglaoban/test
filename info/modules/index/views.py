from flask import render_template, current_app, session

from info.models import User
from . import index_blue

@index_blue.route('/')
def index():
    user_id = session.get("user_id", None)
    user = None
    if user_id:
        # 尝试查询用户的模型
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)

    data = {
        "user": user.to_dict() if user else None,
        # "news_dict_li": news_dict_li,
        # "category_li": category_li
    }


    return render_template("news/index.html", data=data)

@index_blue.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/favicon.ico')
