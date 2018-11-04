from flask import Blueprint, session, request, url_for, redirect

# create a blue print
admin_blue = Blueprint("admin", __name__)

# register the view functions
from . import views


@admin_blue.before_request
def check_admin():
    # 如果不是管理员，那么直接跳转到主页
    is_admin = session.get("is_admin", False)
    # 不是管理员 and 当前访问的url不是管理登录页:
    if not is_admin and not request.url.endswith(url_for('admin.login')):
        return redirect('/')
