# Models/Coordinates.py
from .. import db
class Coordinates(db.Model):
    __tablename__ = 'Coordinates'
    id = db.Column('IDCoordinates', db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    users = db.relationship('User', back_populates='coordinates')

    def __repr__(self):
        return f'<Coordinates ({self.latitude}, {self.longitude})>'