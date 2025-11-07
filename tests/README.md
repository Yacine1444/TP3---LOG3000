# Module de tests – Calculatrice Web (LOG3000)

Ce répertoire contient l’ensemble des tests du projet :  
- **backend** (fonctions Python et logique Flask)  
- **frontend** (structure HTML de la page `index.html`)

---

## Contenu
- `test_calculator.py` : fichier contenant tous les tests unitaires et d’intégration.

---

## Types de tests

| Catégorie | Description |
|------------|-------------|
| **Unitaires (backend)** | Vérifient le comportement des fonctions `add`, `subtract`, `multiply`, `divide` et `calculate()` |
| **Intégration (Flask)** | Vérifient que la route `'/'` fonctionne en GET et POST |
| **Frontend (HTML)** | Vérifient la présence des boutons, du champ d’affichage et du titre dans `index.html` |

---

## Exécution des tests

1. **Installer les dépendances (si ce n'est pas déjà fait) :**
   ```bash
   pip install -r requirements.txt
2. **Aller dans le répertoire racine du projet (si ce n’est pas déjà le cas) :**
    ```bash
    cd <chemin-vers-le-projet>/TP3---LOG3000
3. **Lancer tous les tests :**
    ```bash
    python -m pytest -v
4. **Filtrer un test spécifique :**
    ```bash
    python -m pytest -k <nom_du_test>