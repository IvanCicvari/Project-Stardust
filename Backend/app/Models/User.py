from Init import db

class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column('IDUser', db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column('FirstName', db.String(50))
    last_name = db.Column('LastName', db.String(50))
    username = db.Column('UserName', db.String(50), unique=True)
    email = db.Column('Email', db.String(100), unique=True)
    password = db.Column('Password', db.String(255))
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
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'country_id': self.country_id,
            'city_id': self.city_id,
            'coordinates_id': self.coordinates_id,
            'roles_id': self.roles_id
        }

class Country(db.Model):
    __tablename__ = 'Country'

    id = db.Column('IDCountry', db.Integer, primary_key=True)
    name = db.Column(db.String(100))  # Assuming there's a name field
    users = db.relationship('User', back_populates='country')

    def __repr__(self):
        return f'<Country {self.name}>'

class City(db.Model):
    __tablename__ = 'City'

    id = db.Column('IDCity', db.Integer, primary_key=True)
    name = db.Column(db.String(100))  # Assuming there's a name field
    users = db.relationship('User', back_populates='city')

    def __repr__(self):
        return f'<City {self.name}>'

class Coordinates(db.Model):
    __tablename__ = 'Coordinates'

    id = db.Column('IDCoordinates', db.Integer, primary_key=True)
    latitude = db.Column(db.Float)  # Assuming latitude and longitude fields
    longitude = db.Column(db.Float)
    users = db.relationship('User', back_populates='coordinates')

    def __repr__(self):
        return f'<Coordinates ({self.latitude}, {self.longitude})>'

class UserRoles(db.Model):
    __tablename__ = 'User_Roles'

    id = db.Column('IDRole', db.Integer, primary_key=True)
    role_name = db.Column(db.String(50))  # Assuming a role name field
    users = db.relationship('User', back_populates='roles')

    def __repr__(self):
        return f'<UserRole {self.role_name}>'
