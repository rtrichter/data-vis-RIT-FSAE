from flask import Blueprint

blueprint = Blueprint("home", __name__)

@blueprint.route("/")
def home():
    return "<h1>Welcome to data with RIT Racing</h1>"