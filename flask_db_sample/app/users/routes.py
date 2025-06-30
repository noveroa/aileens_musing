from flask import render_template
from . import bp
from app.database.sqlAlchemy import session
from app.models.tables import User

@bp.route('/', methods=['GET'])
def users():
    users = User.query.all()
    return render_template('users.html', users=users)
