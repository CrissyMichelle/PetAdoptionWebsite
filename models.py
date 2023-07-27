from flask_sqlalchemy import SQLAlchemy

db =  SQLAlchemy()

def connect_db(app):
    """Wraps logic into a function connecting app to database"""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Models a pet in adoption agency"""
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable = False, default=True)
