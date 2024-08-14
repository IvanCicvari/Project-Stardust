import pytest
from flask import url_for
from Backend.app.Models.User import User

@pytest.mark.usefixtures("client", "db_session")
def test_get_user(client, db_session,jwt_token):
    # Setup: Create a user in the database
    user = User(username="testuser", email="test@example.com")
    user.set_password("password123")
    db_session.add(user)
    db_session.commit()
    
    # Exercise: Call the endpoint or function
    response = client.get(
        url_for('api.get_user', user_id=user.id),
        headers={'Authorization': f'Bearer {jwt_token}'}
    )    
    # Verify: Check the response and database state
    assert response.status_code == 200
    assert b'testuser' in response.data
    assert b'test@example.com' in response.data
