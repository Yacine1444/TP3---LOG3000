# Calculatrice Web – LOG3000  

## Numéro d’équipe  
22  

## Description du but  
Il s’agit d’une calculatrice développée avec Flask (Python). Elle permet d’effectuer les opérations arithmétiques de base (addition, soustraction, multiplication et division) depuis une interface web, faite en HTML et CSS.

## Description de la portée:
- Interface web avec un champ d’affichage et des boutons pour les opérandes et les opérateurs.
- Traite une expression sous la forme d’une chaîne de caractères (opérande–opérateur–opérande).
- Aucune persistance de données et aucun compte utilisateur.
- Projet organisé en modules avec `operators.py` pour la logique des opérations, `app.py` pour le serveur, `templates/` pour le HTML et `static/` pour le CSS.

## Prérequis d’installation
- Un compte GitHub
- Git installé localement 
- Python 
- pip  
 
## Instructions d’installation  
1. **Cloner le dépôt GitHub avec la commande :**  
   ```bash
   git clone https://github.com/<nom-utilisateur>/<nom-du-repo>.git
2. **Se déplacer dans le répertoire du projet :**
   ```bash
   cd <chemin-vers-le-projet>/TP3---LOG3000
3. **Installer les dépendances avec la commande :**
   ```bash
   pip install -r requirements.txt

## Instructions pour utiliser l'application
1. **Lancer le serveur Flask avec la commande :**
   ```bash
   python app.py
2. **Ouvrir un navigateur est accéder au lien suivant:**
   ```bash
   http://localhost:5000
3. **Utiliser l'interface avec les différents boutons:**
- Cliquer sur les chiffres (opérandes) et les opérateurs pour composer votre expression mathématique.

## Test
Il existe des test pour les trois fichiers suivant:
- `operators.py`: Tests unitaires sur la logique des différents opérateurs mathématiques (`+`, `-`, `*`, `/`).
- `app.py`: Tests unitaires pour la fonction calculate et tests d’intégration pour la route `/` (requêtes `GET` et `POST`).
- `index.html`: Tests de **front-end** pour vérifier la présence des différents éléments de l’affichage (boutons, champ, titre, etc.).

## Déroulement pour éxecuter les test:
1. **Aller dans le répertoire racine du projet:**
    ```bash
    cd <chemin-vers-le-projet>/TP3---LOG3000
2. **Lancer tous les tests :**
    ```bash
    python -m pytest -v
3. **(Optionnel): Filtrer un test spécifique :**
    ```bash
    python -m pytest -k <nom_du_test>

## Flux de contribution:
1. Branches:
   - Créer une branche par issue avec la commande:
     ```bash
      git checkout -b fix/<issue-id>-<mot-clé>
   - Faire des commits cours et explicite en commençant par un verbe
2. Pull Request (PR)
   - Ouvrir une pull request en référant l’issue.
   - Relire le code et corriger s’il y a des erreurs.
3. Issues:
   - Créer une issue pour chaque test échoué lors de l’exécution des tests.
   - Assigner une personne responsable à chaque issue.


