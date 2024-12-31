import React, { useState } from 'react';
import Navbar2 from '../components/Navbar/Navbar2';
import '../styles/Services.css';

function Timeprediction() {
  const [password, setPassword] = useState(""); // Pour stocker le mot de passe saisi
  const [timeEstimation, setTimeEstimation] = useState(null); // Pour stocker la réponse du backend
  const [error, setError] = useState(null); // Pour gérer les erreurs
  
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
        setError(null); // Effacer les erreurs précédentes
      } else {
        setError('Mot de passe non valide');
      }
    } catch (err) {
      setError(err.message);
      setTimeEstimation(null);
    }
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

          {timeEstimation && (
            <div className="time-display">
              <h2>Time Estimation:</h2>
              <Chronometer timeString={timeEstimation} />
            </div>
          )}

          {error && <p className="error-message">{error}</p>}
        </div>
      </div>
    </div>
  );
}

// Composant pour afficher le chronomètre
const Chronometer = ({ timeString }) => {
  // Le temps est envoyé sous forme de texte, par exemple : "2 jours, 5 heures, 30 minutes, 15 secondes"
  return (
    <div className="chronometer">
      <p>{timeString}</p>
    </div>
  );
};

export default Timeprediction;
