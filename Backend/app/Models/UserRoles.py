# Models/UserRoles.py
from .. import db

class UserRoles(db.Model):
    __tablename__ = 'User_Roles'
    id = db.Column('IDRole', db.Integer, primary_key=True)
    role_name = db.Column('RoleName', db.String(50))
    users = db.relationship('User', back_populates='roles')

    def __repr__(self):
        return f'<UserRole {self.role_name}>'