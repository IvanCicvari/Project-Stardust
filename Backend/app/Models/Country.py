# Models/Country.py
from .. import db

class Country(db.Model):
    __tablename__ = 'Country'
    id = db.Column('IDCountry', db.Integer, primary_key=True)
    name = db.Column('Name', db.String(100))  
    users = db.relationship('User', back_populates='country')

    def __repr__(self):
        return f'<Country {self.name}>'