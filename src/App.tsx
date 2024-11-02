import React from 'react';
import './App.css';

const App: React.FC = () => {
  return (
    <div>
      <nav className="navbar">
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#thoughts">Thoughts</a></li>
            <li><a href="#experience">Experience</a></li>
            <li><a href="#travel">Travel</a></li>
        </ul>
      </nav>
      <div className="text-container">
        <div className="typewriter">
            <h4>Vincent Breau, 2003-09-07, Los Angeles, CA</h4>
            <p>Hello :)</p>
            <p>My name is <strong>Vincent Breau</strong>, and I am a <strong>Computer Science student</strong> at <strong>McGill</strong> University.</p>
            <p>This website will act as a multipurpose repository. You can read some parts of my stream of consciousness in the <strong>Thoughts</strong> section.
            You can also learn more about my experiences ... </p>
        </div>
      </div>
    </div>
  );
};

export default App;