from .. import db


class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column('IDUser', db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column('FirstName', db.String(50))
    last_name = db.Column('LastName', db.String(50))
    username = db.Column('UserName', db.String(50), unique=True)
    email = db.Column('Email', db.String(100), unique=True)
    password_hash = db.Column('Password', db.String(255))
    country_id = db.Column('CountryID', db.Integer, db.ForeignKey('Country.IDCountry'))
    city_id = db.Column('CityID', db.Integer, db.ForeignKey('City.IDCity'))
    coordinates_id = db.Column('CoordinatesID', db.Integer, db.ForeignKey('Coordinates.IDCoordinates'))
    roles_id = db.Column('RolesID', db.Integer, db.ForeignKey('User_Roles.IDRole'))

    # Relationships
    country = db.relationship('Country', back_populates='users')
    city = db.relationship('City', back_populates='users')
    coordinates = db.relationship('Coordinates', back_populates='users')
    roles = db.relationship('UserRoles', back_populates='users')

    def __repr__(self):
        return f'<User {self.username}>'

    def to_dict(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'country_id': self.country_id,
            'city_id': self.city_id,
            'coordinates_id': self.coordinates_id,
            'roles_id': self.roles_id
        }