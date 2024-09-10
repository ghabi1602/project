from ..db_storage import db
from .base_model import BaseModel


class ENROLLMENT(BaseModel):
    __tablename__ = "enrollment"
    class_id = db.Column(db.String(60), db.ForeignKey('classes.id'))
    student_id = db.Column(db.String(60), db.ForeignKey('student.id'))
