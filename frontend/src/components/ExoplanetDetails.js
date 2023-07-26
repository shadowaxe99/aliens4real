```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ExoplanetDetails = () => {
    const [exoplanetData, setExoplanetData] = useState([]);

    useEffect(() => {
        fetchExoplanetData();
    }, []);

    const fetchExoplanetData = async () => {
        try {
            const response = await axios.get('/api/exoplanetData');
            setExoplanetData(response.data);
        } catch (error) {
            console.error(`Error fetching exoplanet data: ${error}`);
        }
    };

    return (
        <div id="exoplanetDetails">
            <h2>Exoplanet Details</h2>
            {exoplanetData.length > 0 ? (
                exoplanetData.map((planet) => (
                    <div key={planet.id}>
                        <h3>{planet.name}</h3>
                        <p>Size: {planet.size}</p>
                        <p>Distance from Star: {planet.distanceFromStar}</p>
                        <p>Atmospheric Composition: {planet.atmosphericComposition}</p>
                        <p>Habitability Score: {planet.habitabilityScore}</p>
                    </div>
                ))
            ) : (
                <p>No exoplanet data available.</p>
            )}
        </div>
    );
};

export default ExoplanetDetails;
```