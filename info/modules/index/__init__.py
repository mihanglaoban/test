from flask import Blueprint

# create a blue print
index_blue = Blueprint("index", __name__)

# register the view functions
from . import views
