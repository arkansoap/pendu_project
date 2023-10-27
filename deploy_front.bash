echo "********** deploiement pendu backend **********"

# Commande effectiées sur la machine locale 
REPFRONT=$(pwd)

cd $REPFRONT

npm run build 

sudo scp -r  /home/tfuchez/Bureau/projets/pendu_project/frontend_pendu/dist/ 5.182.18.114:/usr/share/nginx/tech.arkansoap.penduflex

# Commande effectiées sur le serveur distant
cat > /etc/nginx/sites-available/tech.arkansoap.penduflex << EOF
server {
    listen      80;
    server_name arkansoap.tech;    
    charset utf-8;
    root    /usr/share/nginx/tech.arkansoap.penduflex/dist;
    index   index.html;
    #Always serve index.html for any request
    location / {

        root /usr/share/nginx/tech.arkansoap.penduflex/dist;
        try_files $uri  /index.html;
    }    
    error_log  /var/log/nginx/vue-app-error.log;
    access_log /var/log/nginx/vue-app-access.log;
}
EOF


sudo ln -s /etc/nginx/sites-available/tech.arkansoap.penduflex.conf /etc/nginx/sites-enabled/