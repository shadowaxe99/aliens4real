```javascript
import React, { useState } from 'react';
import axios from 'axios';

const Login = () => {
    const [userData, setUserData] = useState({
        username: '',
        password: ''
    });

    const [message, setMessage] = useState(null);

    const handleInputChange = (event) => {
        setUserData({
            ...userData,
            [event.target.name]: event.target.value
        });
    };

    const handleUserLogin = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('/api/login', userData);
            if (response.data.success) {
                setMessage('loginSuccess');
            } else {
                setMessage('loginFailure');
            }
        } catch (error) {
            setMessage('loginFailure');
        }
    };

    return (
        <div id="loginForm">
            <h2>Login</h2>
            <form onSubmit={handleUserLogin}>
                <label>
                    Username:
                    <input type="text" name="username" onChange={handleInputChange} />
                </label>
                <label>
                    Password:
                    <input type="password" name="password" onChange={handleInputChange} />
                </label>
                <input type="submit" value="Login" />
            </form>
            {message === 'loginSuccess' && <p>Login successful!</p>}
            {message === 'loginFailure' && <p>Login failed. Please try again.</p>}
        </div>
    );
};

export default Login;
```