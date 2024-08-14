import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function AboutUser() {
    const { userId } = useParams(); 
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchUser = async () => {
            try {
                const token = localStorage.getItem('token');
                if (!token) {
                    throw new Error('No token found. Please log in.');
                }

                const response = await fetch(`http://127.0.0.1:5000/api/users/${userId}/`, {
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
    }, [userId]);

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
                    <p><strong>Country name:</strong> {user.country_name}</p>
                    <p><strong>City name:</strong> {user.city_name}</p>
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
