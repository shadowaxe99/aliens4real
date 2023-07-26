```javascript
import React from 'react';

class EducationalContent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            content: []
        };
    }

    componentDidMount() {
        this.fetchEducationalContent();
    }

    fetchEducationalContent() {
        // Fetch educational content from the server
        // This is a placeholder and should be replaced with actual server request
        fetch('/api/educationalContent')
            .then(response => response.json())
            .then(data => this.setState({ content: data }));
    }

    render() {
        return (
            <div id="educationalContent">
                <h2>Educational Content</h2>
                {this.state.content.map((item, index) => (
                    <div key={index}>
                        <h3>{item.title}</h3>
                        <p>{item.description}</p>
                    </div>
                ))}
            </div>
        );
    }
}

export default EducationalContent;
```