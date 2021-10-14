## Ansible Integration

1. Login with RunDeck id

```bash
sudo passwd rundeck

This account is currently not available.
/usr/sbin/nologin

sunil390@gitlab:~$ sudo su -l rundeck -s /bin/bash
[sudo] password for sunil390:
rundeck@gitlab:~$

rundeck@gitlab:~$ ansible --version
ansible [core 2.11.5]
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/var/lib/rundeck/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python3.8/dist-packages/ansible
  ansible collection location = /var/lib/rundeck/.ansible/collections:/usr/share/ansible/collections
  executable location = /usr/local/bin/ansible
  python version = 3.8.10 (default, Sep 28 2021, 16:10:42) [GCC 9.3.0]
  jinja version = 2.10.1
  libyaml = True

2. Clone repo and Install Ansible Collections.

rundeck@gitlab:~$ git clone http://gitlab.znitro.com/mainframe/zansible.git
Cloning into 'zansible'...
Username for 'http://gitlab.znitro.com': sunil390
Password for 'http://sunil390@gitlab.znitro.com':
remote: Enumerating objects: 254, done.
remote: Counting objects: 100% (78/78), done.
remote: Compressing objects: 100% (49/49), done.
remote: Total 254 (delta 40), reused 55 (delta 27), pack-reused 176
Receiving objects: 100% (254/254), 42.61 KiB | 14.20 MiB/s, done.
Resolving deltas: 100% (133/133), done.
rundeck@gitlab:~$



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

