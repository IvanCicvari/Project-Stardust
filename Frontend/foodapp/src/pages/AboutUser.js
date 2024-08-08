// src/pages/AboutUser.js
import React, { useState, useEffect } from 'react';

function AboutUser() {
    // State to store user data
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Fetch user data when the component mounts
    useEffect(() => {
        const fetchUser = async () => {
            try {
                // Get the token from localStorage
                const token = localStorage.getItem('token');
                if (!token) {
                    throw new Error('No token found. Please log in.');
                }

                // Make the request to the API with the Authorization header
                const response = await fetch('/api/user', {
                    headers: {
                        'Authorization': `Bearer ${token}`,
                    },
                });

                if (!response.ok) {
                    if (response.status === 401) {
                        throw new Error('Unauthorized. Please log in again.');
                    }
                    throw new Error('Network response was not ok');
                }

                const data = await response.json();
                setUser(data);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        };

        fetchUser();
    }, []);

    if (loading) {
        return <p>Loading...</p>;
    }

    if (error) {
        return <p>Error: {error}</p>;
    }

    return (
        <div>
            <h1>About User</h1>
            {user ? (
                <div>
                    <p><strong>First Name:</strong> {user.first_name}</p>
                    <p><strong>Last Name:</strong> {user.last_name}</p>
                    <p><strong>Username:</strong> {user.username}</p>
                    <p><strong>Email:</strong> {user.email}</p>
                    <p><strong>Country ID:</strong> {user.country_id}</p>
                    <p><strong>City ID:</strong> {user.city_id}</p>
                    <p><strong>Coordinates ID:</strong> {user.coordinates_id}</p>
                    <p><strong>Role ID:</strong> {user.roles_id}</p>
                </div>
            ) : (
                <p>No user data available.</p>
            )}
        </div>
    );
}

export default AboutUser;
