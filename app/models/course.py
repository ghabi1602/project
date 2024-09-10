from .base_model import BaseModel
from ..db_storage import db


class CLASSES(BaseModel):
    __tablename__ = "classes"
    name = db.Column(db.String(60), nullable=False)
    professor_id = db.Column(db.String(60), db.ForeignKey('professor.id'), nullable=False)
    students = db.relationship('STUDENT', secondary="enrollment", backref='clss', lazy=True)