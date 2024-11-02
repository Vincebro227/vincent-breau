import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import './App.css';
import Thoughts from './Thoughts';

const App: React.FC = () => {
  return (
    <Router basename='/vincent-breau/'>
      <div>
        <nav className="navbar">
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/thoughts">Thoughts</Link></li>
            <li><Link to="/experience">Experience</Link></li>
            <li><Link to="/travel">Travel</Link></li>
          </ul>
        </nav>
        <div className="text-container">
          <Routes>
            <Route path="/" element={
              <div className="typewriter">
                <h4>Vincent Breau, 2003-09-07, Los Angeles, CA</h4>
                <p>Hello :)</p>
                <p>My name is <strong>Vincent Breau</strong>, and I am a <strong>Computer Science student</strong> at <strong>McGill</strong> University.</p>
                <p>This website will act as a multipurpose repository. You can read some parts of my stream of consciousness in the <strong>Thoughts</strong> section.
                You can also learn more about my experiences ... </p>
              </div>
            } />
            <Route path="/thoughts" element={<Thoughts />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default App;