from flask import Blueprint

# create a blue print
passport_blue = Blueprint("passport", __name__)

# register the view functions
from . import views
