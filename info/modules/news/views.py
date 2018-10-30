from flask import render_template, current_app

from info import constants
from info.models import News
from info.modules.news import news_blue


@news_blue.route("/<int:news_id>")
def news_detail(news_id):
    # 右侧的新闻排行的逻辑
    news_list = []
    try:
        news_list = News.query.order_by(News.clicks.desc()).limit(constants.CLICK_RANK_MAX_NEWS)
    except Exception as e:
        current_app.logger.error(e)

    # 定义一个空的字典列表，里面装的就是字典
    news_dict_li = []
    # 遍历对象列表，将对象的字典添加到字典列表中
    for news in news_list:
        news_dict_li.append(news.to_basic_dict())

    data = {
        "news_dict_li": news_dict_li,
    }

    return render_template("news/detail.html", data=data)
