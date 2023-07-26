```javascript
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Interface from './components/Interface';
import CustomQueries from './components/CustomQueries';
import EducationalContent from './components/EducationalContent';
import Visualization from './components/Visualization';
import ExoplanetDetails from './components/ExoplanetDetails';
import Subscription from './components/Subscription';
import Login from './components/Login';
import Register from './components/Register';
import Profile from './components/Profile';

function App() {
  return (
    <Router>
      <Header />
      <Switch>
        <Route path="/" exact component={Interface} />
        <Route path="/custom-queries" component={CustomQueries} />
        <Route path="/educational-content" component={EducationalContent} />
        <Route path="/visualization" component={Visualization} />
        <Route path="/exoplanet-details" component={ExoplanetDetails} />
        <Route path="/subscription" component={Subscription} />
        <Route path="/login" component={Login} />
        <Route path="/register" component={Register} />
        <Route path="/profile" component={Profile} />
      </Switch>
      <Footer />
    </Router>
  );
}

export default App;
```