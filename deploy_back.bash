echo "********** deploiement pendu backend **********"

# Toutes ces commandes sont executées sur le serveur de production.
# sudo ssh 5.182.18.114

# Maj du code
cd /home/pendu_project
git switch main 
git pull 

# Deploy FastAPI using Gunicorn

## Fichier de conf pour gunicorn
cat > /home/pendu_project/backend_pendu/gunicorn_conf.py << EOF
from multiprocessing import cpu_count

# Socket Path

bind = 'unix:/home/pendu_project/backend_pendu/gunicorn.sock'

# Worker Options

workers = cpu_count() + 1

worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options

loglevel = 'debug'

accesslog = '/home/pendu_project/backend_pendu/access_log'

errorlog =  '/home/pendu_project/backend_pendu/error_log'
EOF

## Fichier du service gunicorn
cat > /etc/systemd/system/pendu.service <<EOF
[Unit]

Description=Gunicorn Daemon for FastAPI Demo Application

After=network.target

[Service]

User=root

Group=root

WorkingDirectory=/home/pendu_project/backend_pendu

ExecStart=/home/pendu_project/venv/bin/gunicorn -c gunicorn_conf.py router.main:app

[Install]

WantedBy=multi-user.target
EOF

## start and enable service
sudo systemctl start pendu
sudo systemctl enable pendu

# Setup Nginx as Reverse Proxy

## Fichier de conf pour backend de Nginx
cat > /etc/nginx/sites-available/tech.arkansoap.pendu.conf << EOF
server {
    listen 80;
    listen [::]:80;

    server_name arkansoap.tech;

    root /usr/share/nginx/tech.arkansoap/html;

    index index.php index.html index.htm index.nginx-debian.html;

    access_log  /var/log/nginx/www_access.log;
    error_log   /var/log/nginx/www_error.log;

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php8.1-fpm.sock;
    }

    location ~ /\.ht {
        deny all;
    }
}
EOF

## Add a soft link of the vhost file in the sites-enabled directory.
sudo ln -s /etc/nginx/sites-available/tech.arkansoap.pendu /etc/nginx/sites-enabled/

sudo systemctl reload nginx



