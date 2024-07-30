from flask import Blueprint, jsonify
from Models.User import User  # Ensure correct import

bp = Blueprint('api', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])
    except Exception as e:
        # Use current_app.logger instead of blueprint's logger
        from flask import current_app
        current_app.logger.error(f"Failed to get users: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500
