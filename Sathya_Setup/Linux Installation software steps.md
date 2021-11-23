# Devops
## Install linux on VM
1. Download ubuntu-20.04.3-live-server-amd64 from Ubuntu Site
2. Download and Install Vmware vsphere Workstation player latest version from Vmware Site
3. Open Vmware Vsphere Workstation player and new image and select location of downloaded ubuntu-20.04.3-live-server-amd64.iso image
4. give linux name as gitlab and given user name sathya and pwd gitlab
5. create a new directory on windows as VM and give that path for linux vm installation C:\VM
6. Give Max disk size is 30gb as single disk and give RAM as 5GB which is 5144MB and processor as 3.
7. Select network select bridged and select only lan ethernet network option.
8. Select option defaults and install Ubuntu linux on vm
9. mirror address as remove prefix in on the showed web url
10. Install openssh server option to install it.
11. once linux installed and rebooted.
12. open windows terminal and use ssh connection for your newly installed linux sathya@192.168.1.24
13. issue sudo apt update followed by sudo apt upgrade
## Install Node-Red setup
https://nodered.org/docs/getting-started/windows
1. pre-req is node.js https://nodejs.org/en/ install on window node-v16.13.0-x64
2. open cmd prompt and issue npm install -g --unsafe-perm node-red to install node-red on windows
```cmd 
C:\Users\sathi>npm install -g --unsafe-perm node-red

added 34 packages, removed 33 packages, changed 256 packages, and audited 291 packages in 17s

28 packages are looking for funding
  run `npm fund` for details

3 moderate severity vulnerabilities

To address all issues, run:
  npm audit fix

Run `npm audit` for details.
npm notice
npm notice New patch version of npm available! 8.1.0 -> 8.1.3
npm notice Changelog: https://github.com/npm/cli/releases/tag/v8.1.3
npm notice Run npm install -g npm@8.1.3 to update!
npm notice

C:\Users\sathi>

closed and opened again cmd
C:\Users\sathi>npm install -g --unsafe-perm node-red

changed 290 packages, and audited 291 packages in 4s

28 packages are looking for funding
  run `npm fund` for details

3 moderate severity vulnerabilities

To address all issues, run:
  npm audit fix

Run `npm audit` for details.

C:\Users\sathi>npm audit fix

up to date, audited 1 package in 278ms

found 0 vulnerabilities

C:\Users\sathi>

C:\Users\sathi>node-red
16 Nov 18:35:03 - [info]

Welcome to Node-RED
===================

16 Nov 18:35:03 - [info] Node-RED version: v2.1.3
16 Nov 18:35:03 - [info] Node.js  version: v16.13.0
16 Nov 18:35:03 - [info] Windows_NT 10.0.22000 x64 LE
16 Nov 18:35:04 - [info] Loading palette nodes
16 Nov 18:35:04 - [info] Settings file  : C:\Users\sathi\.node-red\settings.js
16 Nov 18:35:04 - [info] Context store  : 'default' [module=memory]
16 Nov 18:35:04 - [info] User directory : \Users\sathi\.node-red
16 Nov 18:35:04 - [warn] Projects disabled : editorTheme.projects.enabled=false
16 Nov 18:35:04 - [info] Flows file     : \Users\sathi\.node-red\flows.json
16 Nov 18:35:04 - [info] Creating new flow file
16 Nov 18:35:04 - [warn]

---------------------------------------------------------------------
Your flow credentials file is encrypted using a system-generated key.

If the system-generated key is lost for any reason, your credentials
file will not be recoverable, you will have to delete it and re-enter
your credentials.

You should set your own key using the 'credentialSecret' option in
your settings file. Node-RED will then re-encrypt your credentials
file using your chosen key the next time you deploy a change.
---------------------------------------------------------------------

16 Nov 18:35:04 - [info] Server now running at http://127.0.0.1:1880/
16 Nov 18:35:04 - [info] Starting flows
16 Nov 18:35:04 - [info] Started flows

```

3. open notepad and update 
C:\Users\sathi\.node-red\settings.js . find project enable false to true.
4. restart node-red using cmd command prompt command is node-red

## Install Ansible as Global
1. on windows terminal on your installed linux vm, install below things
2. curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3 get-pip.py
sudo python3 -m pip install ansible
```
sathya@gitlab:~$ ansible --version
ansible [core 2.11.6]
  config file = None
  configured module search path = ['/home/sathya/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python3.8/dist-packages/ansible
  ansible collection location = /home/sathya/.ansible/collections:/usr/share/ansible/collections
  executable location = /usr/local/bin/ansible
  python version = 3.8.10 (default, Sep 28 2021, 16:10:42) [GCC 9.3.0]
  jinja version = 2.10.1
  libyaml = True
sathya@gitlab:~$
```

3. from site download ibm_zos_core tar.gz https://galaxy.ansible.com/ibm/ibm_zos_core
 and then transfer to linux vm

4. Created /usr/share/ansible and /usr/share/ansible/collections folders and chmod 755
```
sathya@gitlab:~$ sudo mkdir /usr/share/ansible/collections
sathya@gitlab:~$ sudo chmod 755 /usr/share/ansible/collections
sathya@gitlab:~$ sudo chmod 755 /usr/share/ansible
```

sudo ansible-galaxy collection install ibm-ibm_zos_core-1.4.0-beta.1.tar.gz -p /usr/share/ansible/collections
```
sathya@gitlab:~$ sudo ansible-galaxy collection install ibm-ibm_zos_core-1.4.0-beta.1.tar.gz -p /usr/share/ansible/collections
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Installing 'ibm.ibm_zos_core:1.4.0-beta.1' to '/usr/share/ansible/collections/ansible_collections/ibm/ibm_zos_core'
ibm.ibm_zos_core:1.4.0-beta.1 was installed successfully
sathya@gitlab:~$
```

## Install gitlab
use site https://about.gitlab.com/install/?version=ce#ubuntu

1. sudo apt-get install -y curl openssh-server ca-certificates tzdata perl
2. sudo apt-get install -y postfix
3. change below command as follows before issuing

sudo EXTERNAL_URL="https://gitlab.example.com" apt-get install gitlab-ce

to

sudo EXTERNAL_URL="http://192.168.1.24" apt-get install gitlab-ce

```
sathya@gitlab:~$ sudo EXTERNAL_URL="http://192.168.1.24" apt-get install gitlab-ce
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following NEW packages will be installed:
  gitlab-ce
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 967 MB of archives.
After this operation, 2,660 MB of additional disk space will be used.
Get:1 https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu focal/main amd64 gitlab-ce amd64 14.4.2-ce.0 [967 MB]
Fetched 967 MB in 2min 42s (5,967 kB/s)
Selecting previously unselected package gitlab-ce.
(Reading database ... 71791 files and directories currently installed.)
Preparing to unpack .../gitlab-ce_14.4.2-ce.0_amd64.deb ...
Unpacking gitlab-ce (14.4.2-ce.0) ...
Setting up gitlab-ce (14.4.2-ce.0) ...
```

4. password of root as stored as follow, make a note of it

Notes:
Default admin account has been configured with following details:
Username: root
Password: You didn't opt-in to print initial root password to STDOUT.
Password stored to /etc/gitlab/initial_root_password. This file will be cleaned up in first reconfigure run after 24 hours.
```
sathya@gitlab:~$ sudo cat /etc/gitlab/initial_root_password
# WARNING: This value is valid only in the following conditions
#          1. If provided manually (either via `GITLAB_ROOT_PASSWORD` environment variable or via `gitlab_rails['initial_root_password']` setting in `gitlab.rb`, it was provided before database was seeded for the first time (usually, the first reconfigure run).
#          2. Password hasn't been changed manually, either via UI or via command line.
#
#          If the password shown here doesn't work, you must reset the admin password following https://docs.gitlab.com/ee/security/reset_user_password.html#reset-your-root-password.

Password: GjL1ZBWxPieag36kboUqu+Lo/6sWx82TtSixUneNqbM=

# NOTE: This file will be automatically deleted in the first reconfigure run after 24 hours.
sathya@gitlab:~$
```

5. open web browser type http://192.168.1.24/
  to access gitlab user id root and password of earlier step.

6. using root create new admin id as sathya and pwd gitlab55. 


## Install Gitlab Runner
Install gitlab runner on linux vm image using below steps

1. curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash
2. sudo apt-get install gitlab-runner
```
sathya@gitlab:~$ curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  5945  100  5945    0     0   6627      0 --:--:-- --:--:-- --:--:--  6627
Detected operating system as Ubuntu/focal.
Checking for curl...
Detected curl...
Checking for gpg...
Detected gpg...
Running apt-get update... done.
Installing apt-transport-https... done.
Installing /etc/apt/sources.list.d/runner_gitlab-runner.list...done.
Importing packagecloud gpg key... done.
Running apt-get update... done.

The repository is setup! You can now install packages.
sathya@gitlab:~$ sudo apt-get install gitlab-runner
Reading package lists... Done
Building dependency tree
Reading state information... Done
Suggested packages:
  docker-engine
The following NEW packages will be installed:
  gitlab-runner
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 453 MB of archives.
After this operation, 493 MB of additional disk space will be used.
Get:1 https://packages.gitlab.com/runner/gitlab-runner/ubuntu focal/main amd64 gitlab-runner amd64 14.4.0 [453 MB]
Fetched 453 MB in 1min 20s (5,688 kB/s)
Selecting previously unselected package gitlab-runner.
(Reading database ... 71562 files and directories currently installed.)
Preparing to unpack .../gitlab-runner_14.4.0_amd64.deb ...
Unpacking gitlab-runner (14.4.0) ...
Setting up gitlab-runner (14.4.0) ...
GitLab Runner: creating gitlab-runner...
Home directory skeleton not used
Runtime platform                                    arch=amd64 os=linux pid=18685 revision=4b9e985a version=14.4.0
gitlab-runner: the service is not installed
Runtime platform                                    arch=amd64 os=linux pid=18695 revision=4b9e985a version=14.4.0
gitlab-ci-multi-runner: the service is not installed
Runtime platform                                    arch=amd64 os=linux pid=18725 revision=4b9e985a version=14.4.0
Runtime platform                                    arch=amd64 os=linux pid=18803 revision=4b9e985a version=14.4.0
INFO: Docker installation not found, skipping clear-docker-cache
sathya@gitlab:~$
```
3. sudo passwd gitlab-runner  new password is gitlab
4. sudo gitlab-runner register 
you need gitlab details give ip address of gitlab and registration token from site admin area and then click runners on right side you will see token details.

```
sathya@gitlab:~$ sudo gitlab-runner register
Runtime platform                                    arch=amd64 os=linux pid=34170 revision=4b9e985a version=14.4.0
Running in system-mode.

Enter the GitLab instance URL (for example, https://gitlab.com/):
http://192.168.1.24
Enter the registration token:
Pu6yxqznk2shsu97uz55
Enter a description for the runner:
[gitlab]:
Enter tags for the runner (comma-separated):

Registering runner... succeeded                     runner=Pu6yxqzn
Enter an executor: docker, shell, virtualbox, custom, docker-ssh, parallels, ssh, docker+machine, docker-ssh+machine, kubernetes:
shell
Runner registered successfully. Feel free to start it, but if it's running already the config should be automatically reloaded!
sathya@gitlab:~$
```
## Install Postgresql
1. sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
2. wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
3. sudo apt-get update
4. sudo apt-get -y install postgresql
5. edit /etc/postgresql/14/main/postgresql.conf and change
sudo nano /etc/postgresql/14/main/postgresql.conf

change port 5432 to 5433  ( Since 5432 is used by gitlab postgresql)

Save CTRL+X and then Y and then enter

6. sudo nano /etc/postgresql/14/main/pg_hba.conf
host    all all 0.0.0.0/0   md5  

```
# "local" is for Unix domain socket connections only
local   all             all                                     peer
host    all             all             0.0.0.0/0               md5
```
Save CTRL+X and then Y and then enter
7. sudo systemctl stop postgresql
8. sudo systemctl start postgresql
9. sudo passwd postgres ( Change password - This is to access psql prompt to define rundeck database)
```
sathya@gitlab:~$ sudo passwd postgres
New password: gitlab
Retype new password:
passwd: password updated successfully
sathya@gitlab:~$
```
10. su postgres
11. psql
```
sathya@gitlab:~$ su postgres
Password:
postgres@gitlab:/home/sathya$ psql
psql (14.1 (Ubuntu 14.1-1.pgdg20.04+1))
Type "help" for help.

postgres=# \password
Enter new password: gitlab
Enter it again:
postgres=#
```
12. \password (Change database admin user postgres password here for administration using pgadmin GUI)
13. to come out use \q and enter
## Install Rundeck
1. sudo apt-get install openjdk-11-jre-headless
2. curl https://raw.githubusercontent.com/rundeck/packaging/main/scripts/deb-setup.sh 2> /dev/null | sudo bash -s rundeck
3. sudo apt-get update
4. sudo apt-get install rundeck
5. edit below files
sudo nano /etc/rundeck/rundeck-config.properties
 
grails.serverURL=http://localhost:4440
to grails.serverURL=http://192.168.1.24:4440

added new line dataSource.dirverClassName = org.postgresql.Driver

dataSource.dbCreate = none
to 
dataSource.dbCreate = update
 
dataSource.url = jdbc:h2:file:/var/lib/rundeck/data/rundeckdb;DB_CLOSE_ON_EXIT=FALSE
to 
dataSource.url = jdbc:postgresql://127.0.0.1:5433/rundeck 

added below lines
dataSource.username = rundeckuser
dataSource.password = rundeckpassword

```
# change hostname here
grails.serverURL=http://192.168.1.24:4440
dataSource.driverClassName = org.postgresql.Driver
dataSource.dbCreate = update
#dataSource.url = jdbc:h2:file:/var/lib/rundeck/data/rundeckdb;DB_CLOSE_ON_EXIT=FALSE
dataSource.url = jdbc:postgresql://127.0.0.1:5433/rundeck
dataSource.username = rundeckuser
dataSource.password = rundeckpassword
grails.plugin.databasemigration.updateOnStart=true
```

5. Edit file  /etc/rundeck/framework.properties
sudo nano /etc/rundeck/framework.properties
change all localhost to ip address

framework.server.name = localhost
framework.server.hostname = localhost
framework.server.port = 4440
framework.server.url = http://localhost:4440
```
# ----------------------------------------------------------------
# Rundeck server connection information
# ----------------------------------------------------------------

framework.server.name = 192.168.1.24
framework.server.hostname = 192.168.1.24
framework.server.port = 4440
framework.server.url = http://192.168.1.24:4440
```

6. create postgres database and userid and grant access
su postgres
password gitlab
psql
create database rundeck;
create user rundeckuser with password 'rundeckpassword';
grant ALL privileges on database rundeck to rundeckuser;

```
sathya@gitlab:~$ su postgres
Password:
postgres@gitlab:/home/sathya$ psql
psql (14.1 (Ubuntu 14.1-1.pgdg20.04+1))
Type "help" for help.

postgres=# create database rundeck;
CREATE DATABASE
postgres=# create user rundeckuser with password 'rundeckpassword';
CREATE ROLE
postgres=# grant ALL privileges on database rundeck to rundeckuser;
GRANT
postgres=# \q
postgres@gitlab:/home/sathya$

```

7. sudo service rundeckd start
8. sudo tail -f /var/log/rundeck/service.log
some abend, so perform restart of linux and then verify

```
[2021-11-16T14:38:04,775] INFO  rundeckapp.BootStrap - workflowConfigFix973: No fix was needed. Storing fix application state.
[2021-11-16T14:38:04,991] INFO  rundeckapp.BootStrap - Rundeck startup finished in 704ms
[2021-11-16T14:38:05,121] INFO  rundeckapp.Application - Started Application in 37.151 seconds (JVM running for 38.779)
Grails application running at http://localhost:4440 in environment: production
```
9. open web browse http://192.168.1.24:4440/user/login
use id admin pwd admin


## Microk8s GoldDisc and AWX Install
---
## Gold Disc Creation

1. setp VM with bridged network, 5 GB memory and 25 GB disk 3 cpus
2. Install ubuntu 20.04.3 select microk8s while installing linux on vm
3. sudo apt update
4. sudo apt upgrade
5. Reboot
6. sudo usermod -a -G microk8s $USER && sudo chown -f -R $USER ~/.kube
7. echo "alias kubectl='microk8s kubectl'" >> ~/.bash_aliases && source ~/.bash_aliases
8. sudo nano /usr/local/bin/kubectl
```
#!/bin/bash
args="$@"
microk8s kubectl $args 
```
9. sudo chmod 755 /usr/local/bin/kubectl
10. sudo apt install net-tools
11. sudo ufw allow in on cni0 && sudo ufw allow out on cni0
12. sudo ufw default allow routed

 
## Microk8s Customization
---
1. microk8s start
2. microk8s status --wait-ready
```
sathya@mk8s:~$ \microk8s status --wait-ready
microk8s is running
high-availability: no
  datastore master nodes: 127.0.0.1:19001
  datastore standby nodes: none
```
3. kubectl get nodes
```
sathya@mk8s:~$ kubectl get nodes
NAME   STATUS   ROLES    AGE   VERSION
mk8s   Ready    <none>   17h   v1.22.3-3+9ec7c40ec93c73
```

4. microk8s enable dns storage ingress dashboard
5. kubectl get --all-namespaces pods
```
sathya@mk8s:~$ kubectl get --all-namespaces pods
NAMESPACE       NAME                                               READY   STATUS    RESTARTS      AGE
kube-system     dashboard-metrics-scraper-58d4977855-5xg9h         1/1     Running   1 (76m ago)   17h
kube-system     coredns-7f9c69c78c-lflfm                           1/1     Running   1 (76m ago)   17h
awx-namespace   awx-znitro-postgres-0                              1/1     Running   1 (76m ago)   17h
kube-system     hostpath-provisioner-5c65fbdb4f-xtc9r              1/1     Running   1 (76m ago)   17h
kube-system     kubernetes-dashboard-59699458b-86dds               1/1     Running   1 (76m ago)   17h
awx-namespace   awx-znitro-6ddf4956fd-8bnjl                        4/4     Running   4 (76m ago)   17h
kube-system     calico-kube-controllers-6dfdf55d48-gcc8w           1/1     Running   2 (76m ago)   17h
kube-system     calico-node-hk72c                                  1/1     Running   2 (76m ago)   17h
awx-namespace   awx-operator-controller-manager-647f4c5c7d-7cj6l   2/2     Running   2 (76m ago)   17h
ingress         nginx-ingress-microk8s-controller-wsjcv            1/1     Running   1 (76m ago)   17h
kube-system     metrics-server-85df567dd8-vmb27                    1/1     Running   1 (76m ago)   17h
sathya@mk8s:~$
```
6. kubectl get storageclass
```
sathya@mk8s:~$ kubectl get storageclass
NAME                          PROVISIONER            RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
microk8s-hostpath (default)   microk8s.io/hostpath   Delete          Immediate           false                  17h
sathya@mk8s:~$
```

## AWX Install
---
1. sudo apt install make
2. git clone https://github.com/ansible/awx-operator.git --branch 0.15.0
3. cd awx-operator
4. git checkout
5. export NAMESPACE=awx-namespace
6. make deploy
7. kubectl get pods -n $NAMESPACE
8. kubectl config set-context --current --namespace=$NAMESPACE
9. nano awx-demo.yml (Changed demo to znitro)
10. kubectl apply -f awx-demo.yml
11. kubectl logs -f deployments/awx-operator-controller-manager -c awx-manager
12. kubectl get pods -l "app.kubernetes.io/managed-by=awx-operator"
13. kubectl get svc
```
sathya@mk8s:~$ kubectl get svc
NAME                                              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
awx-operator-controller-manager-metrics-service   ClusterIP   10.152.183.253   <none>        8443/TCP       17h
awx-znitro-postgres                               ClusterIP   None             <none>        5432/TCP       17h
awx-znitro-service                                NodePort    10.152.183.52    <none>        80:30551/TCP   17h
sathya@mk8s:~$
```
14. On Windows Powershell ->  ssh -L 30551:localhost:30551 sathya@192.168.1.25
15. kubectl get secret awx-znitro-admin-password -o jsonpath="{.data.password}" | base64 --decode
16. open browser
http://localhost:30551/#/login
use admin and password from 15th step


## Galaxy collection install and end to end Playbook testing
---
1. https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#install-multiple-collections-with-a-requirements-file
2. In Git Repo create collections folder and add requirements.yml file
```
---
collections:
  - name: ibm.ibm_zos_core
    version: "1.4.0-beta.1"
    source: "https://galaxy.ansible.com"
```
3. on http://localhost:30551/#/login
4. Create new user sathya and provide admin access
5. create new Organization  as ATOS select Excution envirnonment as AWX EE (latest) and Galaxy Credintals as ansible galaxy
6. create new credinatals awx-gitlab select Organization  as ATOS, credintal type Source control , give username and password of gitlab
7. create Inventories Name ZOS1-INV select Organization as ATOS, instance group default
8. create new hosts as zos1, select inventory as ZOS1-INV and enter below lines on variables yaml. 
```
---
ansible_host: 192.168.1.44
ansible_user: sysprg1
ansible_python_interpreter: /usr/lpp/IBM/cyp/v3r8/pyz/bin/python3.8
################################################################################
# Configure dependency installations
################################################################################
PYZ: "/usr/lpp/IBM/cyp/v3r8/pyz"
ZOAU: "/usr/lpp/IBM/zoautil"
################################################################################
# Playbook enviroment variables
################################################################################

environment_vars:
  _BPXK_AUTOCVT: "ON"
  ZOAU_HOME: "{{ ZOAU }}"

  LIBPATH: "{{ ZOAU }}/lib:{{ PYZ }}/lib:/lib:/usr/lib:."
  PATH: "{{ ZOAU }}/bin:{{ PYZ }}/bin:/bin:/usr/sbin:/var/bin"
  _CEE_RUNOPTS: "FILETAG(AUTOCVT,AUTOTAG) POSIX(ON)"
  _TAG_REDIR_ERR: "txt"
  _TAG_REDIR_IN: "txt"
  _TAG_REDIR_OUT: "txt"
  LANG: "C"
```
9. ssh-keygen in ubuntu and copy privatekey from .ssh/id_rsa
10. Add new credentials as zos1 as machine and enter id password of sysprg1 and paste the above private key.
11. In Templates  create Canceluserjob Job Type : RUN , Inventory : ZOS1-INV , Project : awx , execution env: AWX EE (latest)
Playbook : Cancel_User.yaml(this is coming from Gitlab)  , Credentials select zos1 save 
12. on canceluserjoba select survey --> add 2 survey Enter Lpar Name and Enter userid (This will be popup during it runs) and you can control user access for that particular job
12. Launch the canceluserjob and verify the job
13. create new workflow under template canceluserworflow --> Organization :ATOS , Inventory :ZOS1-INV


## Access kubernets browser
1.  kubectl get svc -n kube-system
```
sathya@mk8s:~$ kubectl get svc -n kube-system
NAME                        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                  AGE
kube-dns                    ClusterIP   10.152.183.10    <none>        53/UDP,53/TCP,9153/TCP   17h
metrics-server              ClusterIP   10.152.183.49    <none>        443/TCP                  17h
kubernetes-dashboard        ClusterIP   10.152.183.237   <none>        443/TCP                  17h
dashboard-metrics-scraper   ClusterIP   10.152.183.154   <none>        8000/TCP                 17h
```

2. kubectl port-forward -n kube-system service/kubernetes-dashboard 10443:443 (don't close it)

```
Forwarding from 127.0.0.1:10443 -> 8443
Forwarding from [::1]:10443 -> 8443

Handling connection for 10443
E1123 08:57:41.380602   55731 portforward.go:400] an error occurred forwarding 10443 -> 8443: error forwarding port 8443 to pod eaeaa36d07d4ccf0688a5e9d1a06ccea0cdcc8982dd94b936fd1c22040556616, uid : failed to execute portforward in network namespace "/var/run/netns/cni-921146f1-fff0-8958-2c8e-bf8f51d2e87c": read tcp4 127.0.0.1:38268->127.0.0.1:8443: read: connection reset by peer
Handling connection for 10443
E1123 08:57:42.521997   55731 portforward.go:400] an error occurred forwarding 10443 -> 8443: error forwarding port 8443 to pod eaeaa36d07d4ccf0688a5e9d1a06ccea0cdcc8982dd94b936fd1c22040556616, uid : failed to execute portforward in network namespace "/var/run/netns/cni-921146f1-fff0-8958-2c8e-bf8f51d2e87c": read tcp4 127.0.0.1:38288->127.0.0.1:8443: read: connection reset by peer
Handling connection for 10443
Handling connection for 10443
Handling connection for 10443
```
3. Access web interface ssh -L 10443:localhost:10443 sathya@192.168.1.25
https://localhost:10443/#/login
4. logon using token
5. get token password using 
token=$(microk8s kubectl -n kube-system get secret | grep default-token | cut -d " " -f1) microk8s kubectl -n kube-system describe secret $token
```
sathya@mk8s:~$ token=$(microk8s kubectl -n kube-system get secret | grep default-token | cut -d " " -f1) microk8s kubectl -n kube-system describe secret $token
```







