from flask import Blueprint, current_app, request
from flask_restx import Api, Resource, fields
from Models import User  
from Init import db

bp = Blueprint('api', __name__)
api = Api(bp, version='1.0', title='Access API', description='API for user management')

user_model = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'username': fields.String(required=True, description='The username of the user'),
    'email': fields.String(required=True, description='The email of the user'),
    'first_name': fields.String(required=True, description='The first name of the user'),
    'last_name': fields.String(required=True, description='The last name of the user'),
    'country_id': fields.Integer(description='The country ID of the user'),
    'city_id': fields.Integer(description='The city ID of the user'),
    'coordinates_id': fields.Integer(description='The coordinates ID of the user'),
    'roles_id': fields.Integer(description='The roles ID of the user')
})

@api.route('/users')
class UserList(Resource):
    @api.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        try:
            users = User.query.all()
            return [user.to_dict() for user in users]
        except Exception as e:
            current_app.logger.error(f"Failed to get users: {e}")
            return {'error': 'Internal Server Error'}, 500

    @api.expect(user_model)
    @api.marshal_with(user_model, code=201)
    def post(self):
        """Create a new user"""
        try:
            data = request.get_json()
            required_fields = ['username', 'email', 'first_name', 'last_name', 'password']
            if not data or not all(field in data for field in required_fields):
                return {'error': 'Bad Request', 'message': 'Missing required fields'}, 400
            
            if User.query.filter_by(email=data['email']).first() or User.query.filter_by(username=data['username']).first():
                return {'error': 'Conflict', 'message': 'User already exists'}, 409

            new_user = User(
                username=data['username'],
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                password_hash=(data['password']),
                country_id=data.get('country_id'),
                city_id=data.get('city_id'),
                coordinates_id=data.get('coordinates_id'),
                roles_id=data.get('roles_id')
            )
            
            db.session.add(new_user)
            db.session.commit()
            return new_user.to_dict(), 201
        except Exception as e:
            current_app.logger.error(f"Failed to create user: {e}")
            return {'error': 'Internal Server Error'}, 500

@api.route('/users/<int:id>')
@api.response(404, 'User not found')
@api.param('id', 'The user identifier')
class UserResource(Resource):
    @api.marshal_with(user_model)
    def get(self, id):
        """Fetch a user given its identifier"""
        try:
            user = User.query.get(id)
            if user:
                return user.to_dict()
            return {'error': 'User not found'}, 404
        except Exception as e:
            current_app.logger.error(f"Failed to get user with id {id}: {e}")
            return {'error': 'Internal Server Error'}, 500

    @api.response(204, 'User deleted')
    def delete(self, id):
        """Delete a user given its identifier"""
        try:
            user = User.query.get(id)
            if user is None:
                return {'error': 'User not found'}, 404
            
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted successfully'}, 200
        except Exception as e:
            current_app.logger.error(f"Failed to delete user with id {id}: {e}")
            return {'error': 'Internal Server Error'}, 500

