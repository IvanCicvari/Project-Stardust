from flask_jwt_extended import create_access_token
import pytest
from Backend.app import create_app, db  # Assuming db is imported from your app
from Backend.app.Models.User import User
from Backend.app.config import TestingConfig

@pytest.fixture(scope='session')
def app():
    """Session-wide test `Flask` application."""
    app = create_app(TestingConfig)
    with app.app_context():
        yield app  # Provide the app context for the tests

@pytest.fixture(scope='session')
def client(app):
    """Session-wide test client."""
    return app.test_client()

@pytest.fixture(scope='function')
def db_session(app):
    """Creates a new database session for each test."""
    # Ensure the database is empty before each test
    db.create_all()

    yield db.session  # Provide the session for the test

    db.session.remove()  # Clean up session after each test
    db.drop_all()  # Drop all tables after each test
    
@pytest.fixture(scope='function')
def jwt_token(client):
    """Generate a JWT token for authentication."""
    # Create a test user and generate a token
    user = User(username="testuser", email="test@example.com")
    user.set_password("password123")
    db_session = client.application.extensions['sqlalchemy'].db.session
    db_session.add(user)
    db_session.commit()

    access_token = create_access_token(identity=user.id)
    return access_token