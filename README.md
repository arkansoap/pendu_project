# pendu_projet

> A pendu with flexs implementation with vue.js

## Lancer en local

activer l'environnement virtuel à partir de la racine du projet:

```bash
source venv/bin/activate
```

### Backend avec uvicorn

Se placer ds le répertoire backend_pendu et lancer la commande ci dessous:

```bash
uvicorn router.main:app
```

### Frontend avec npm

se placer ds le répertoire frontend_pendu et lancer la commande ci dessous:

```bash
npm run dev
```

### BDD

- installer postgresql
- créer une base de données avec le nom "pendu" avec l'utilisateur postgres
- créer les tables avec le script sql dans le répertoire backend_pendu.meta.py

## Déploiement

/etc/nginx/sites-available/
/usr/share/nginx/

A Remplir ...

## TODO

- regle et fonctionnement ds l onglet rules
- rajouter "new game" qd partie finie
- rajout des images pr nb d'essais
- poop up indiquant que nv param de difficuté pris en compte pour la provhaine game + score enregistré
- pas possible d'enregistrer plusieurs fois le score (une seule ligne identique dans table high score)
- new game qd click sur onglet game (du haut) / ou simplement revenir à l'écran tel qu'il était
- revoir calcul du score
- partie contacts -> mettre les liens (se faire un fb, twitter "pro")
- score:
  - paramètre réglable plus finement (choix de toutes les variables - tentatives, ...)
  - rajout temps (chrono) ds calcul du score
  - choix caratctères: avec ou sans accent, avec ou sans tiret, ....
  - tester syst de score, faire script qui test plein de combi et voir si les resultats ont du sens
