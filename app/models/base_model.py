from ..db_storage import db
from uuid import uuid4
from datetime import datetime

class BaseModel(db.Model):
    """base model to be inherited by child models"""
    __abstract__ = True

    id = db.Column(db.String(60), primary_key=True, default=lambda: str(uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)