```javascript
import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';

const Visualization = () => {
    const [chartData, setChartData] = useState({});

    const chart = () => {
        setChartData({
            labels: ['Exoplanets', 'Habitable Zones', 'Life Signatures', 'Statistical Predictions'],
            datasets: [
                {
                    label: 'Probability',
                    data: [65, 59, 80, 81],
                    backgroundColor: [
                        'rgba(75, 192, 192, 0.6)',
                        'rgba(153, 102, 255, 0.6)',
                        'rgba(255, 159, 64, 0.6)',
                        'rgba(255, 99, 132, 0.6)'
                    ],
                    borderWidth: 4
                }
            ]
        });
    };

    useEffect(() => {
        chart();
    }, []);

    return (
        <div className="visualization" id="visualization">
            <h3>Data Visualization</h3>
            <div>
                <Bar
                    data={chartData}
                    options={{
                        responsive: true,
                        title: { text: "AI Alien Life Predictor", display: true },
                        scales: {
                            yAxes: [
                                {
                                    ticks: {
                                        autoSkip: true,
                                        maxTicksLimit: 10,
                                        beginAtZero: true
                                    },
                                    gridLines: {
                                        display: false
                                    }
                                }
                            ],
                            xAxes: [
                                {
                                    gridLines: {
                                        display: false
                                    }
                                }
                            ]
                        }
                    }}
                />
            </div>
        </div>
    );
};

export default Visualization;
```