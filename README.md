# Projet Web - La création d'un site web

## Introduction
Le hachage des mots de passe est une technique utilisée pour sécuriser les mots de passe en les transformant en une chaîne de caractères unique et fixe à l'aide d'algorithmes comme SHA-256 ou bcrypt. Contrairement au chiffrement, le hachage est unidirectionnel : une fois un mot de passe haché, il ne peut pas être facilement converti en texte clair. Cependant, des attaques comme le brute force, où des combinaisons sont testées jusqu'à trouver une correspondance, ou les rainbow tables, qui exploitent des bases de données de hachages pré-calculés, menacent cette sécurité. Les bonnes pratiques, comme l'utilisation de salage (salt), rendent ces attaques plus difficiles.

Pour le projet du module web, nous avons décidé de donner vie à cette idée en créant une interface interactive et complète. Notre site **HexVault** permet aux utilisateurs d'explorer et de comprendre ces différentes attaques de manière intuitive, tout en offrant une expérience utilisateur fluide et moderne.

## Fonctionnalités
- Simulations d'attaques (force brute, dictionnaire, dictionnaire amélioré, hybrid).
- Tester votre mot de passe.
- Prédiction de temps pour casser un mot de passe.
- Fonctions de cryptage et décryptage (AES,DES,3DES,CHACHA20,RC4).
- Compte utilisateur et historique.
## Présentation Générale


HexVault est une plateforme web innovante dédiée à la sécurité des mots de passe. Elle combine des technologies de pointe avec des outils conviviaux pour aider les particuliers et les organisations à se protéger efficacement contre les menaces cybernétiques.

## Mission

Notre mission est de sensibiliser à l'importance de choisir des mots de passe sécurisés tout en offrant aux utilisateurs les outils nécessaires pour tester, renforcer et protéger leurs identifiants de manière efficace.

## Nos Objectifs
-**Promouvoir les Bonnes Pratiques** : Encourager les utilisateurs à adopter des mots de passe forts et uniques pour leurs comptes.

-**Proposer des Simulations Réalistes** : Aider les utilisateurs à comprendre les risques associés aux mots de passe faibles grâce à des scénarios d'attaques réalistes.

-**Permettre la Protection des Données** : Offrir des outils simples et efficaces pour sécuriser les informations sensibles.

## Technologies Utilisées
**Frontend** : HTML, CSS, JavaScript, React.js, Three.js (pour les objets 3D).  
**Backend** : FastAPI.  
**Base de données** : MongoDB, PostgreSQL.  
**Authentification** : Keycloak.
## Lien design
https://www.figma.com/design/8jlyWezwaFMTgBZFvRHpU1/web-project?node-id=0-1&t=7XTX6i36BTDGupdW-1
## Lien Vidéo
https://drive.google.com/file/d/1zzMctOWtO_2xrssLDkVrYG7Hj0LLzEW3/view?usp=drive_link

## Répartition de notre code  
**/Fronted**:ce Dossier contient le frontend de notre site web

**/fastAPI/featuresservices**:ce Dossier contient le backend de notre site web



## Comment Notre Code Marche
Nous utilisons un concept de multiservices pour optimiser les performances et la gestion des opérations coûteuses, comme les attaques. Pour cela, nous avons attribué une base de données spécialisée pour ces tâches, utilisant MongoDB pour stocker les dictionnaires, car elle est rapide et bien adaptée à ces besoins spécifiques.

Notre architecture est divisée en plusieurs services distincts :

**Frontend** : un serveur dédié à l'interface utilisateur.
**Backend** : un serveur gérant la logique métier et les interactions avec les bases de données.
Bases de données :
**MongoDB** est utilisé pour les attaques et l’historique, en raison de sa rapidité et de sa capacité à gérer efficacement des données non relationnelles.
**PostgreSQL** est utilisé pour les utilisateurs et leurs informations personnelles, grâce à sa robustesse et à son support des relations complexes.
 
## Comment Démarrer Nos Serveurs
Pour démarrer les serveurs, suivez ces étapes :

1-Installer les bibliothèques nécessaires :

Les fichiers requirements pour le backend et le frontend contiennent les dépendances nécessaires. Installez-les en suivant les instructions fournies.

2-Démarrer les serveurs :

**Backend** : Exécutez la commande suivante :
```bash
uvicorn main:app --reload --port=8001
```
**Frontend** : Lancez le serveur avec :
```bash
npm start
```
3-Configurer Keycloak :

Exécutez Keycloak via Docker Compose pour cela il fauderait ce déplacer vers le dossier Frontend et démarrez les composants nécessaires dans Docker.
```bash
docker-compose up -d
```

4-Créer les utilisateurs et les clients :

Configurez les utilisateurs et clients nécessaires à votre application dans Keycloak.

5-Tester le site :

Une fois tout en place, testez votre site et ses fonctionnalités pour vous assurer que tout fonctionne correctement.

## Comment utiliser les attaques
**Étape 1 :** Récupérer le hash du mot de passe
Identifiez la source du hash (base de données, fichier, etc.).

**Étape 2 :** Identifier et séparer les composants
Si le hash utilise un salt , isolez-le.
```bash
$1$GhE59K.G$Ue3N0/dj.Sdutcb5E1vcN1
```
Exemple de format :
```bash
salt:GhE59K.G
hash:Ue3N0/dj.Sdutcb5E1vcN1
```
Placez le hash et le salt dans les champs appropriés du programme .

**Étape 3 :** Remplir le champs de la méthode du hash (md5/sha256/sha2 elle indique dans le hach)

**Étape 4 :** Lancer l'attaque .

## Pourquoi crypter les mots de passe stockés localement ?

Beaucoup de personnes conservent leurs mots de passe dans des fichiers locaux sur leur ordinateur pour ne pas les oublier. Cependant, ces fichiers peuvent être accessibles en cas de piratage, de vol de l’appareil ou d’accès non autorisé. Crypter ces mots de passe permet de les protéger en les rendant illisibles sans la clé de déchiffrement. Cela ajoute une couche de sécurité essentielle, réduisant les risques que des informations sensibles tombent entre de mauvaises mains, même si le fichier est compromis.

## Le principe du chiffrement symétrique :

Le chiffrement symétrique utilise une seule clé pour à la fois chiffrer et déchiffrer les données. Lors du chiffrement, l'algorithme prend le texte en clair et la clé, puis transforme le texte en une version illisible, appelée texte chiffré. Ce texte chiffré ne peut être retrouvé sous sa forme originale qu'en utilisant la même clé pour le décryptage. Le chiffrement avec une clé unique est rapide, mais nécessite de protéger cette clé pour garantir la sécurité des données.



