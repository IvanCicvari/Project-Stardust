from flask import Blueprint, current_app, request
from flask_restx import Api, Resource, fields
from Models import User

bp = Blueprint('api', __name__)
api = Api(bp, version='1.0', title='Access API', description='API for user management')

user_model = api.model('User', {
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
