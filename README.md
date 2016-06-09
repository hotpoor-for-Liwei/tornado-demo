# Install Ubuntu
Ubuntu Server 14.04 LTS
user: ubuntu
password: xxx

# server step 1
sudo apt-get update
sudo apt-get upgrade

# server step 2
sudo apt-get install nginx mysql-server python-pip supervisor

## install newst nginx stable version:
download nginx signing: http://nginx.org/keys/nginx_signing.key
sudo vi /etc/apt/source.list
append two lines:
deb http://nginx.org/packages/ubuntu/ trusty nginx
deb-src http://nginx.org/packages/ubuntu/ trusty nginx
sudo apt-get update
sudo apt-get install nginx

# server step 3
sudo apt-get install libmysqld-dev python-dev zlib1g-dev 
sudo pip install mysql-python certifi

# server step 4
sudo mkdir /var/www
sudo chown -R ubuntu:ubuntu /var/www

# local step 1
git clone https://github.com/xzm920/tornado-demo.git

# local step 2
rsync -avz tornado-demo ubuntu@example.com:/var/www

# run nginx and tornado by user www-data

# create log directory
sudo mkdir /var/log/nginx/tornado-demo
sudo chown -R www-data:www-data /var/log/nginx/tornado-demo

# server step 5
configure nginx
/etc/nginx/nginx.conf
/etc/nginx/conf.d/tornado-demo.conf
restart nginx

# server step 6
configure supervisor
/etc/supervisor/conf.d/tornado-demo.conf
restart supervisor
sudo /etc/init.d/supervisor restart
sudo supervisorctl
start app
exit

C
C
C
C



