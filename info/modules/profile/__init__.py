from flask import Blueprint

# create a blue print
profile_blue = Blueprint("profile", __name__, url_prefix="/user")

# register the view functions
from . import views
