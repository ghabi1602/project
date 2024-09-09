from flask_sqlalchemy import SQLAlchemy
# initializing sqlalchemy


db = SQLAlchemy()


def init_db(app):
    """creates all instances and save to database"""
    with app.app_context():
        # Import models here to ensure they are registered with SQLAlchemy
        from .models.student_model import STUDENT
        from .models.prof_model import PROFESSOR
        from .models.course import CLASSES

        # Create all tables based on the models
        db.create_all()
