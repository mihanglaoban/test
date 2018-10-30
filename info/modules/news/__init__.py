from flask import Blueprint

# create a blue print
news_blue = Blueprint("news", __name__, url_prefix="/news")

# register the view functions
from . import views
