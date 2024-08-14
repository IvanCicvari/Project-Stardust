from flask import Blueprint, jsonify, request
from Backend.app import db
from Backend.app.Models.User import User
from flask_jwt_extended import jwt_required, create_access_token
from sqlalchemy.orm import joinedload

# Create a Blueprint for the API
bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users/', methods=['GET'])
@jwt_required()
def get_users():
    """Get all users"""
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200


@bp.route('/register/', methods=['POST'])
def register():
    data = request.get_json()
    
    # Basic validation
    required_fields = ['username', 'password', 'email']
    for field in required_fields:
        if not data.get(field):
            return jsonify({"msg": f"Missing {field}"}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({"msg": "Username already exists"}), 400

    try:
        new_user = User(
            username=data['username'],
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            country_id=data.get('country_id'),
            city_id=data.get('city_id'),
            coordinates_id=data.get('coordinates_id'),
            roles_id=data.get('roles_id')
        )
        new_user.set_password(data['password'])

        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": f"Error creating user: {str(e)}"}), 500

    return jsonify({"msg": "User created successfully"}), 201

@bp.route('/login/', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"msg": "Missing username or password"}), 400

    # Include the join to load the Country relationship
    user = User.query.options(joinedload(User.country)).filter_by(username=data['username']).first()

    if user is None or not user.check_password(data['password']):
        return jsonify({"msg": "Bad username or password"}), 401

    # Generate JWT token
    access_token = create_access_token(identity=user.id)
    
    # Optionally return some user info along with the token
    return jsonify(access_token=access_token, user=user.to_dict()), 200

@bp.route('/users/<int:user_id>/', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    if 'password' in data:
        user.set_password(data['password'])

    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.email = data.get('email', user.email)

    db.session.commit()
    return jsonify(user.to_dict()), 200

@bp.route('/users/<int:user_id>/', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"msg": "User deleted successfully"}), 200


@bp.route('/users/<int:user_id>/', methods=['GET'])
@jwt_required()
def get_user(user_id):
    """Get a single user by ID"""
    user = User.query.options(
        joinedload(User.country),
        joinedload(User.city)
    ).get_or_404(user_id)
    return jsonify(user.to_dict()), 200
