// src/pages/Login.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        setError(null);

        try {
            const response = await fetch('http://127.0.0.1:5000/api/login/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password }),
            });

            const data = await response.json();
            console.log('Response data:', data); // Log the entire response data

            if (!response.ok) {
                setError(data.msg || 'Something went wrong');
                return;
            }

            // Save the token and user information in localStorage
            localStorage.setItem('token', data.access_token);
            localStorage.setItem('userId', data.user.id); // Save user ID
            localStorage.setItem('user', JSON.stringify(data.user)); // Save full user data

            // Navigate to the AboutUser page
            navigate(`/AboutUser/${data.user.id}`);
        } catch (err) {
            console.error('Error during fetch:', err);
            setError('Network error. Please try again.');
        }
    };

    return (
        <div>
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Username:</label>
                    <input
                        type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Password:</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                {error && <p style={{ color: 'red' }}>{error}</p>}
                <button type="submit">Login</button>
            </form>
        </div>
    );
}

export default Login;
