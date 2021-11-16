# VM Linux Install setup step 1
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
1. 




