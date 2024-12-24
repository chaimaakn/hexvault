import Keycloak from 'keycloak-js';

// Keycloak configuration options

const keycloak = new Keycloak({
  url: 'http://localhost:8080', // URL to your Keycloak server
  realm: 'myRealm', // Name of your Keycloak realm
  clientId: 'Client1', // Your client ID in Keycloak
});


export default keycloak;
