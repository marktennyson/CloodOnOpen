from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db:SQLAlchemy = SQLAlchemy()

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255))
    flag = db.Column(db.String(255))
    population = db.Column(db.Integer)
    capital = db.Column(db.String(255))
    continent = db.Column(db.String(255))
    area = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.now)