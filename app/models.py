from flask import app
from app import db
from flask_login import UserMixin

#db.init_app(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class IPv6Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(39), unique=True, nullable=False)
    description = db.Column(db.String(100))