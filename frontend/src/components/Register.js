```javascript
import React, { useState } from 'react';
import axios from 'axios';

const Register = () => {
    const [userData, setUserData] = useState({
        username: '',
        password: '',
        email: '',
    });

    const [message, setMessage] = useState(null);

    const handleInputChange = (event) => {
        setUserData({
            ...userData,
            [event.target.name]: event.target.value,
        });
    };

    const handleUserRegistration = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('/api/register', userData);
            setMessage(response.data.message);
            if (response.data.success) {
                setUserData({
                    username: '',
                    password: '',
                    email: '',
                });
            }
        } catch (error) {
            setMessage('Registration failed. Please try again.');
        }
    };

    return (
        <div id="registerForm">
            <h2>Register</h2>
            <form onSubmit={handleUserRegistration}>
                <label>
                    Username:
                    <input
                        type="text"
                        name="username"
                        value={userData.username}
                        onChange={handleInputChange}
                        required
                    />
                </label>
                <label>
                    Email:
                    <input
                        type="email"
                        name="email"
                        value={userData.email}
                        onChange={handleInputChange}
                        required
                    />
                </label>
                <label>
                    Password:
                    <input
                        type="password"
                        name="password"
                        value={userData.password}
                        onChange={handleInputChange}
                        required
                    />
                </label>
                <button type="submit">Register</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default Register;
```