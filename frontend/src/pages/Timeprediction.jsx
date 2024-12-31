import React from 'react'
import Navbar2 from '../components/Navbar/Navbar2';
import '../styles/Services.css';

function Timeprediction() {
  return (
    <div id='timeprediction'>

    <div className="navbar-container">
            <Navbar2 />
        </div>

        <div className="test-container">
          <div className="test-container1">
            <h1>Time Prediction</h1>
            <p>enter your password and we'll tell you how long it takes for it to be cracked!</p>
            <input type="text" placeholder="Enter your password..." />
            <button >Start</button>
          </div>
       
        </div>
       
   
</div>
  )
}

export default Timeprediction