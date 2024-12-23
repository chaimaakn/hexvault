import Keycloak from 'keycloak-js';

// Keycloak configuration options

const keycloak = new Keycloak({
  url: 'http://localhost:8080/auth', // URL to your Keycloak server
  realm: 'hexvault', // Name of your Keycloak realm
  clientId: 'react', // Your client ID in Keycloak
});


export default keycloak;
