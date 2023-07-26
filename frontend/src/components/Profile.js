```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Profile = () => {
    const [userData, setUserData] = useState({});

    useEffect(() => {
        const fetchUserData = async () => {
            try {
                const response = await axios.get('/api/user');
                setUserData(response.data);
            } catch (error) {
                console.error('Error fetching user data:', error);
            }
        };

        fetchUserData();
    }, []);

    return (
        <div id="profile">
            <h2>User Profile</h2>
            <div>
                <label>Name: </label>
                <span>{userData.name}</span>
            </div>
            <div>
                <label>Email: </label>
                <span>{userData.email}</span>
            </div>
            <div>
                <label>Subscription Plan: </label>
                <span>{userData.subscriptionPlan}</span>
            </div>
            <div>
                <label>Custom Queries: </label>
                <span>{userData.customQueries}</span>
            </div>
        </div>
    );
};

export default Profile;
```