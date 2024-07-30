from Init import db

class UserRoles(db.Model):
    __tablename__ = 'User_Roles'

    id = db.Column('IDRole', db.Integer, primary_key=True)
    role_name = db.Column(db.String(50))  # Assuming a role name field
    users = db.relationship('User', back_populates='roles')

    def __repr__(self):
        return f'<UserRole {self.role_name}>'
