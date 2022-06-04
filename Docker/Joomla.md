# Joomla on Docker

## Steps...

1. sudo apt-get install docker.io -y
2. sudo usermod -aG docker $USER
3. newgrp docker
4. docker network create joomla-network
5. docker pull mysql:5.7
6. docker pull joomla
7. docker volume create mysql-data
8. docker run -d --name joomladb  -v mysql-data:/var/lib/mysql --network joomla-network -e "MYSQL_ROOT_PASSWORD=PWORD" -e MYSQL_USER=joomla -e "MYSQL_PASSWORD=PWORD" -e "MYSQL_DATABASE=joomla" mysql:5.7
9. docker volume create joomla-data
10. docker run -d --name joomla -p 80:80 -v joomla-data:/var/www/html --network joomla-network -e JOOMLA_DB_HOST=joomladb -e JOOMLA_DB_USER=joomla -e JOOMLA_DB_PASSWORD=PWORD joomla
11. host will be joomladb and dbname is joomla
