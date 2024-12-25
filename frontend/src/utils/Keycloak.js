import Keycloak from 'keycloak-js';

// Keycloak configuration options

const keycloak = new Keycloak({
  url: 'http://localhost:8080/', // URL to your Keycloak server
  realm: 'HEXVAULT', // Name of your Keycloak realm
  clientId: 'Client', // Your client ID in Keycloak
});


export default keycloak;
