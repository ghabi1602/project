from flask import Flask, session
from .db_storage import db, init_db
from flask_login import LoginManager


login_manager = LoginManager()
def create_app():
    app = Flask(__name__, static_folder='./web_flask/static', template_folder='./web_flask/templates')
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://tvs_admin:betty@localhost/tvs_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    init_db(app)
    login_manager.init_app(app)
    login_manager.login_view = '.web_flask.authentication.login'


    with app.app_context():
        from .web_flask import authentication
        from .web_flask import routes
        app.register_blueprint(authentication.bp)
        app.register_blueprint(routes.bp)


    @login_manager.user_loader
    def load_user(user_id):
        if session['user_type'] == 'std':
            from .models.student_model import STUDENT
            return STUDENT.query.get(user_id)
        from .models.prof_model import PROFESSOR
        return PROFESSOR.query.get(user_id)

    return app

