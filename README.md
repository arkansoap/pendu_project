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

- sudo -u postgres psql
- CREATE DATABASE pendu;
- \l pour vérifier que la base a bien été créée

- installer postgresql
- créer une base de données avec le nom "pendu" avec l'utilisateur postgres
- créer les tables avec le script dans le répertoire backend_pendu.meta.py
- utiliser le script params_difficulty pour initialiser les paramètres de difficulté ou les updater

## Déploiement inital

- python (+ module requis), uvicorn, gunicorn et postgresql installés
- back et front sont 2 app distinctes
- sudo systemctl start nginx
- sudo systemctl enable nginx

0. Maj du code pr le back

- On créée un repo git /home/pendu_project qu'on link avec le remote (on devrait importer seulement le back mais confusion lors de la création du proket en local)

1. Backend (voir fichier deploy_back.bash):

- Dans backend pendu on écrit le fichier de conf gunicorn_conf.py
- Créer et editer le fichier pour le service
- Start & enable the service:

  - $ sudo systemctl start pendu
  - $ sudo systemctl enable pendu
  - $ sudo systemctl status pendu

- Fichier conf Nginx
- link site enable

2. BDD
   -Comme ci dessus mais sur le serveur de prod au lieu de le faire sur sa machine locale

   - maj les 2 fichiers de conf pour postgre

3. Frontend

- on se place en local ds le repo frontend.
- On se place ds le repo frontend-pendu et build le projet avec la commande 'npm run build' (qui crée le repo dist)
  - penser à changer l adresse back sur le quel il pointe (adresse du back de prod au lieu de localhost)
- Dans /usr/share/nginx/ on copie le repos dist précédemment créé
- Dans /etc/nginx/sites-available/ on écrit le fochier de conf
- link site-enable

## Deploiement suite maj du cod

- Maj du code back
  cd /home/pendu_project
  git switch main
  git pull

- maj du code front
  npm run build -> en local
  scp dist repor sur le serveur

- Restart nginx
  sudo systemctl restart nginx

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
