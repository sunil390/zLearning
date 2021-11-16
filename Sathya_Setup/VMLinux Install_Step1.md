# VM Linux Install setup
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
## Install Install Node-Red setup
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
3. sudo passwd gitlab-runner  new passwor is gitlab
4. sudo gitlab-runner register -- which we will do later

## install gitlab
use site https://about.gitlab.com/install/?version=ce#ubuntu

sudo apt-get install -y curl openssh-server ca-certificates tzdata perl
sudo apt-get install -y postfix
change below command as follows before issuing

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





