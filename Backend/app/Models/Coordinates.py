# Models/Coordinates.py
from Init import db

class Coordinates(db.Model):
    __tablename__ = 'Coordinates'

    id = db.Column('IDCoordinates', db.Integer, primary_key=True)
    latitude = db.Column(db.Float)  # Ensure this matches your schema
    longitude = db.Column(db.Float)
    users = db.relationship('User', back_populates='coordinates')

    def __repr__(self):
        return f'<Coordinates ({self.latitude}, {self.longitude})>'
