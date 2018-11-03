from flask import g, render_template, redirect

from info.modules.profile import profile_blue
from info.utils.common import user_login_data


@profile_blue.route("/info")
@user_login_data
def user_info():
    user = g.user

    if not user:
        #代表没有登录，重定向到首页
        return redirect("/")
    data = {
        "user": user.to_dict()
    }

    return render_template("news/user.html", data = data)

