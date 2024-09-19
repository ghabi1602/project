from .base_model import BaseModel
from ..db_storage import db
from .association import enrollment


class CLASSES(BaseModel):
    __tablename__ = "classes"
    name = db.Column(db.String(300), nullable=False)
    field = db.Column(db.String(300), nullable=False)
    maximum_number_of_students = db.Column(db.Integer, nullable=False)
    professor_id = db.Column(db.String(60), db.ForeignKey('professor.id'), nullable=False)
    students = db.relationship('STUDENT', secondary=enrollment, cascade="all, save-update", lazy=True, viewonly=True)