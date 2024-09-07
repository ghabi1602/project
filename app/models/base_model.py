from ..db_storage import db
from uuid import uuid4
from datetime import datetime

class BaseModel(db.Model):
    """base model to be inherited by child models"""
    __abstract__ = True

    id = db.column(db.String(60), PRIMARY_KEY = True, default=lambda: str(uuid4()))
    created_at = db.column(db.Datetime, default=datetime.utcnow)
    updated_at = db.column(db.Datetime, default=datetime.utcnow, onupdate=datetime.utcnow)