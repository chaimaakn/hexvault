import Landingpage from './pages/Landingpage';
import Page from './pages/Page1';
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
          <Route path="/page1" element={<Page />} />
        </Routes>
      </BrowserRouter>
    </ReactKeycloakProvider>

  );
}

export default App;