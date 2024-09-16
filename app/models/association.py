from ..db_storage import db

enrollment = db.Table('enrollment',
                        db.Column('student_id', db.String(60), db.ForeignKey('student.id'), primary_key=True),
                        db.Column('class_id', db.String(60), db.ForeignKey('classes.id'), primary_key=True))
