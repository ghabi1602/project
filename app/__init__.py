from flask import Flask
from .db_storage import db, init_db
from flask_login import login_manager


login = login_manager()
def create_app():
    app = Flask(__name__, static_folder='./web_flask/static', template_folder='./web_flask/templates')
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://tvs_admin:betty@localhost/tvs_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    init_db(app)
    login.init_app(app)
    login.login_view = '.web_flask.authentication.login'

    return app
