import Landingpage from './pages/Landingpage';
import EncryptDecrypt from './pages/EncryptDecrypt';
import Passwordtesting from './pages/Passwordtesting';
import Timeprediction from './pages/Timeprediction';
import Attacks from './pages/Attacks';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { keycloak, initKeycloak } from './utils/Keycloak';
import { ReactKeycloakProvider } from '@react-keycloak/web';

//add keycloak provider wraper around the app

function App() {
  const handleOnEvent = (event, error) => {
    console.log('onKeycloakEvent', event, error);
  };

  return (
    <ReactKeycloakProvider
      authClient={keycloak}
      onEvent={handleOnEvent}
      initOptions={{
        onLoad: 'check-sso',
        silentCheckSsoRedirectUri: window.location.origin + '/silent-check-sso.html',
        pkceMethod: 'S256',
        checkLoginIframe: false
      }}>
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