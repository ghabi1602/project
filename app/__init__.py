from flask import Flask
from .db_storage import db, init_db


def create_app():
    app = Flask(__name__, static_folder='./web_flask/static', template_folder='./web_flask/templates')
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://tvs_admin:betty@localhost/tvs_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    init_db(app)

    return app
