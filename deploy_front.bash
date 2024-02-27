echo "********** deploiement pendu backend **********"

# Commande effectiées sur la machine locale 
REPFRONT=$(pwd)

cd $REPFRONT

npm run build 

sudo scp -r  /home/tfuchez/Bureau/projets/pendu_project/frontend_pendu/dist/ 5.182.18.114:/usr/share/nginx/tech.arkansoap.penduflex

cat > /etc/nginx/sites-available/tech.arkansoap.penduflex.conf << EOF
server {
    listen 80;
    server_name penduflex.arkansoap.tech;

    location / {
        root /usr/share/nginx/tech.arkansoap.penduflex/dist;
        try_files \$uri \$uri/ /index.html;
    }
}
EOF


sudo ln -s /etc/nginx/sites-available/tech.arkansoap.penduflex.conf /etc/nginx/sites-enabled/