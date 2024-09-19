from .base_model import BaseModel
from flask_login import UserMixin
from ..db_storage import db
from .association import enrollment

class STUDENT(UserMixin, BaseModel):
    __tablename__ = "student"
    fullname = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    highest_school_level = db.Column(db.String(300), nullable=False)
    field_of_studies = db.Column(db.String(300), nullable=False)
    interested_at = db.Column(db.String(300), nullable=False)
    classes = db.relationship('CLASSES', secondary=enrollment, cascade="all, save-update", lazy=True)
