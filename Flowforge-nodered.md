# FlowForge 


## FlowForge Setup

1. cd ~
2. curl -sL https://deb.nodesource.com/setup_16.x | sudo bash -
3. sudo apt -y install nodejs
4. sudo mkdir /opt/flowforge
5. sudo chown $USER /opt/flowforge
6. wget https://github.com/flowforge/installer/releases/download/v0.5.0/flowforge-installer-0.5.0.zip
7. unzip flowforge-installer-x.y.z.zip
8. cp -R flowforge-installer-x.y.z/* /opt/flowforge
9. cd /opt/flowforge
10. ./install.sh
11. Add Stack
12. Add template 

## NodeRed - Install NodeRed First

1. bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
