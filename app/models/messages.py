from app.db import db


class Messages(db.Model):
    __tablename__ = 'messages'
    hash_digest = db.Column(db.String(100), primary_key=True)
    text = db.Column(db.String(255))