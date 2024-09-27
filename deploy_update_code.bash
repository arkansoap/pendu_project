#### locally ####
cd /home/pendu_project/frontend_pendu
npm run build
sudo scp -r  /home/tfuchez/Bureau/projets/pendu_project/frontend_pendu/dist/ 5.182.18.114:/usr/share/nginx/tech.arkansoap.penduflex

#### on the server ####
ssh root@5.182.18.114
cd /home/pendu_project
git switch main
git pull
mv .env.prod .env

sudo systemctl reload nginx
