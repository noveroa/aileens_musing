from flask import Blueprint

bp = Blueprint('main', __name__)

from flaskDemo.main import routes