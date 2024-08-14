# Models/City.py
from .. import db

class City(db.Model):
    __tablename__ = 'City'
    id = db.Column('IDCity', db.Integer, primary_key=True)
    name = db.Column('Name', db.String(100))  
    users = db.relationship('User', back_populates='city')

    def __repr__(self):
        return f'<City {self.name}>'