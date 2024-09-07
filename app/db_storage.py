from flask_sqlalchemy import SQLAlchemy
#initializing sqlalchemy

db = SQLAlchemy()

def init_db():
    """creates all instances and save to database"""
    from models.student_model import STUDENT
    from models.prof_model import PROFESSOR
    db.create_all()