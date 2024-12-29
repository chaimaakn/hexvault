import React, { useState } from 'react';
import Navbar2 from '../components/Navbar/Navbar2';
import '../styles/Services.css';

function Passwordtesting() {
  const [showPopup, setShowPopup] = useState(false);

  // Function to handle showing the popup
  const handleTestPassword = () => {
    setShowPopup(true); // Show the popup when button is clicked
  };

  // Function to close the popup
  const handleClosePopup = () => {
    setShowPopup(false); // Close the popup
  };

  return (
    <div id="passwordtesting">
      {/* Apply the blur class to the content when the popup is shown */}
      <div className={`main-content ${showPopup ? 'blur' : ''}`}>
        <div className="navbar-container">
          <Navbar2 />
        </div>
        <div className="container-2">
          <div className="container-3">
            <h1>Password Testing</h1>
            <p>
              To test the strength of your password, enter your password in the
              input field below and click the "Test Password" button.
            </p>
            <input type="text" placeholder="Enter your password..." />
            <button onClick={handleTestPassword}>Test password</button>
          </div>
        </div>
      </div>

      {/* Popup Window */}
      {showPopup && (
        <>
          <div className="overlay"></div>
          <div className="popup">
            <div className="popup-content">
              <h2>Result!</h2>
              <p>password is weak</p>
              <button onClick={handleClosePopup}>Close</button>
            </div>
          </div>
        </>
      )}
    </div>
  );
}

export default Passwordtesting;
