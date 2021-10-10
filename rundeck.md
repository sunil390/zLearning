
## RunDeck Community Edition

<https://docs.rundeck.com/docs/administration/install/linux-deb.html#installing-rundeck>

```bash
sudo apt-get install openjdk-11-jre-headless

dpkg --list | grep -i rundeck

sudo dpkg -i rundeck_3.4.4.20210920-1_all.deb

sudo service rundeckd start
sudo service rundeckd stop

tail -f /var/log/rundeck/service.log

Change localhost to server ip address in these 2 files

sunil390@gitlab:/etc/rundeck$ nano rundeck-config.properties
sunil390@gitlab:/etc/rundeck$ nano framework.properties

```

