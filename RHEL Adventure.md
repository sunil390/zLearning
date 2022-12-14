# RHEL installed from dveloper.redhat.com 

## epel repo enablement

1. sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
2. sudo yum install -y tigervnc-server xrdp
3. sudo systemctl start xrdp
4. sudo systemctl enable xrdp
5. sudo netstat -antup | grep xrdp ( Ubuntu sudo adduser xrdp ssl-cert)
6. sudo firewall-cmd --permanent --add-port=3389/tcp ( Ubuntu sudo ufw allow 3389)
7. sudo firewall-cmd --reload
8. sudo nano /etc/xrdp/startwm.sh and add startxfce4 for RHEL
```sh
# for Ubuntu
 if test -r /etc/profile; then
        . /etc/profile
 fi

unset DBUS_SESSION_BUS_ADDRESS
unset XDG_RUNTIME_DIR

 test -x /etc/X11/Xsession && exec /etc/X11/Xsession
 exec /bin/sh /etc/X11/Xsession
```
9. sudo bash -c 'echo "exec gnome-session" >> /etc/xrdp/xrdp.ini'
10. reboot

## Ansible Setup

1. sudo yum update
2. login as root and issue usermod -aG wheel <username>
3. curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
4. sudo python3 get-pip.py
5. sudo python3 -m pip install ansible
6. sudo mkdir /usr/share/ansible and sudo mkdir /usr/share/ansible/collections folders and chmod 755
7. wget https://galaxy.ansible.com/download/ibm-ibm_zos_core-1.4.0-beta.1.tar.gz
8. sudo ansible-galaxy collection install ibm-ibm_zos_core-1.4.0-beta.1.tar.gz -p /usr/share/ansible/collections
9. ansible-galaxy collection list
10. systemctl enable --now cockpit.socket
11. https://192.168.2.211:9090 to access cockpit..
