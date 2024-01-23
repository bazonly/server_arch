from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    publish_year = db.Column(db.DateTime, nullable=False, default=func.now())
    pages_count = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
