import Landingpage from './pages/Landingpage';
import Page from './pages/Page1';
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
      <Route path="/page1" element={<Page />} />
      <Route path="/attacks" element={<Attacks />} />
    </Routes>
  </BrowserRouter>
  </ReactKeycloakProvider>
    
  );
}

export default App;