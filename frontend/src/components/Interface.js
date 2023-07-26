```javascript
import React from 'react';
import Header from './Header.js';
import Footer from './Footer.js';
import CustomQueries from './CustomQueries.js';
import Visualization from './Visualization.js';
import ExoplanetDetails from './ExoplanetDetails.js';
import EducationalContent from './EducationalContent.js';
import Subscription from './Subscription.js';
import Login from './Login.js';
import Register from './Register.js';
import Profile from './Profile.js';

class Interface extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      loggedIn: false,
      user: null,
      cosmologicalData: [],
      exoplanetData: [],
      habitabilityData: [],
      lifeSignatureData: [],
      statisticalData: [],
    };
  }

  handleUserLogin = (user) => {
    this.setState({ loggedIn: true, user: user });
  }

  handleUserLogout = () => {
    this.setState({ loggedIn: false, user: null });
  }

  render() {
    return (
      <div>
        <Header loggedIn={this.state.loggedIn} handleLogout={this.handleUserLogout} />
        {this.state.loggedIn ? (
          <div>
            <Profile user={this.state.user} />
            <CustomQueries user={this.state.user} />
            <Visualization data={this.state.cosmologicalData} />
            <ExoplanetDetails data={this.state.exoplanetData} />
            <EducationalContent />
            <Subscription user={this.state.user} />
          </div>
        ) : (
          <div>
            <Login handleLogin={this.handleUserLogin} />
            <Register handleLogin={this.handleUserLogin} />
          </div>
        )}
        <Footer />
      </div>
    );
  }
}

export default Interface;
```