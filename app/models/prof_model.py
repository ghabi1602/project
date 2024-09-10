from flask_login import UserMixin
from ..db_storage import db
from .base_model import BaseModel


class PROFESSOR(UserMixin, BaseModel):
    __tablename__ = "professor"
    fulPROFESSORlname = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    Specialization = db.Column(db.String(300), nullable=False)
    expert_at = db.Column(db.String(300), nullable=False)
    years_of_experience = db.Column(db.Integer, nullable=False)
    classes = db.relationship('classes', backref='prof', lazy=True)