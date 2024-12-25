import Landingpage from './pages/Landingpage';
import EncryptDecrypt from './pages/EncryptDecrypt';
import Passwordtesting from './pages/Passwordtesting';
import Timeprediction from './pages/Timeprediction';
import Attacks from './pages/Attacks';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import keycloak from './utils/Keycloak';
import { ReactKeycloakProvider } from '@react-keycloak/web';

const keycloakInitOptions = {
  onLoad: 'login-required', // Options: 'login-required' or 'check-sso'
};
//add keycloak provider wraper around the app

function App() {
  return (
    <ReactKeycloakProvider authClient={keycloak} >
    <BrowserRouter>
    <Routes>
      <Route exact path="/" element={<Landingpage />} />
      <Route path="/EncryptDecrypt" element={<EncryptDecrypt />} />
      <Route path="/Attacks" element={<Attacks />} />
      <Route path="/Timeprediction" element={<Timeprediction />} />
      <Route path="/Passwordtesting" element={<Passwordtesting />} />
    </Routes>
  </BrowserRouter>
  </ReactKeycloakProvider>
    
  );
}

export default App;