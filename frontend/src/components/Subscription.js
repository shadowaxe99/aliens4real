```javascript
import React, { useState } from 'react';

const Subscription = () => {
    const [subscription, setSubscription] = useState('Free');

    const handleSubscriptionChange = (event) => {
        setSubscription(event.target.value);
    };

    return (
        <div id="subscription">
            <h2>Subscription Plan</h2>
            <p>Select your subscription plan to access advanced features and real-time data.</p>
            <form>
                <label>
                    <input
                        type="radio"
                        value="Free"
                        checked={subscription === 'Free'}
                        onChange={handleSubscriptionChange}
                    />
                    Free
                </label>
                <label>
                    <input
                        type="radio"
                        value="Premium"
                        checked={subscription === 'Premium'}
                        onChange={handleSubscriptionChange}
                    />
                    Premium
                </label>
                <label>
                    <input
                        type="radio"
                        value="Pro"
                        checked={subscription === 'Pro'}
                        onChange={handleSubscriptionChange}
                    />
                    Pro
                </label>
            </form>
            <p>Your current plan: {subscription}</p>
        </div>
    );
};

export default Subscription;
```