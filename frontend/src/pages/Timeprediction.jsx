import React, { useState } from 'react';
import Navbar2 from '../components/Navbar/Navbar2';
import '../styles/Services.css';

function Timeprediction() {
  const [password, setPassword] = useState(""); // Pour stocker le mot de passe saisi
  const [timeEstimation, setTimeEstimation] = useState(null); // Pour stocker la réponse du backend
  const [error, setError] = useState(null); // Pour gérer les erreurs
  const [isPopupOpen, setIsPopupOpen] = useState(false); // Pour gérer l'ouverture du pop-up

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8001/attaque/check-password', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ password }),
      });

      if (!response.ok) {
        throw new Error('Erreur lors de la connexion au serveur');
      }

      const data = await response.json();
      if (data.success) {
        setTimeEstimation(data.timeestimation);
        setError(null);
        setIsPopupOpen(true); // Ouvrir le pop-up
      } else {
        setError('Mot de passe non valide');
      }
    } catch (err) {
      setError(err.message);
      setTimeEstimation(null);
    }
  };

  const handleClosePopup = () => {
    setIsPopupOpen(false); // Fermer le pop-up
  };

  return (
    <div id='timeprediction'>
      <div className="navbar-container">
        <Navbar2 />
      </div>

      <div className="test-container">
        <div className="test-container1">
          <h1>Time Prediction</h1>
          <p>Enter your password and we'll tell you how long it takes for it to be cracked!</p>
          <input
            type="text"
            placeholder="Enter your password..."
            value={password}
            onChange={handlePasswordChange}
          />
          <button onClick={handleSubmit}>Start</button>

          {error && <p className="error-message">{error}</p>}
        </div>
      </div>

      {isPopupOpen && timeEstimation && (
        <Popup timeEstimation={timeEstimation} onClose={handleClosePopup} />
      )}
    </div>
  );
}

// Composant Pop-up
const Popup = ({ timeEstimation, onClose }) => {
  // Séparer les valeurs de jours, heures, minutes et secondes
  const [days, hours, minutes, seconds] = parseTimeEstimation(timeEstimation);

  return (
    <div className="popup2">
      <div className="popup-content2">
        <h2>Time Estimation</h2>
        <div className="chronometer">
          <div className="time-box">
            <h3>{days}</h3>
            <p>Days</p>
          </div>
          <div className="time-box">
            <h3>{hours}</h3>
            <p>Hours</p>
          </div>
          <div className="time-box">
            <h3>{minutes}</h3>
            <p>Minutes</p>
          </div>
          <div className="time-box">
            <h3>{seconds}</h3>
            <p>Seconds</p>
          </div>
        </div>
        <button className="close-button" onClick={onClose}>
          Close
        </button>
      </div>
    </div>
  );
};

// Fonction pour analyser le temps estimé (séparer en jours, heures, minutes et secondes)
const parseTimeEstimation = (timeString) => {
  const timeParts = timeString.match(/\d+/g); // Extraire les chiffres
  const [days, hours, minutes, seconds] = timeParts.map((t) => parseInt(t, 10));
  return [days || 0, hours || 0, minutes || 0, seconds || 0];
};

export default Timeprediction;

