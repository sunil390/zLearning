# RHEL on x86

## [K3S on rhel](https://github.com/kurokobo/awx-on-k3s)
1. sudo systemctl disable firewalld --now
2. sudo reboot
3. sudo dnf install -y git make
4. curl -sfL https://get.k3s.io | sh -s - --write-kubeconfig-mode 644
5. cd ~
6. git clone https://github.com/ansible/awx-operator.git
7. cd awx-operator
8. git checkout 1.1.2
9. export NAMESPACE=awx
10. make deploy
11. kubectl -n awx get all
12. git clone https://github.com/kurokobo/awx-on-k3s.git
13. cd awx-on-k3s
14. git checkout 1.1.2
15. AWX_HOST="awx.znext.com"
16. openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -out ./base/tls.crt -keyout ./base/tls.key -subj "/CN=${AWX_HOST}/O=${AWX_HOST}" -addext "subjectAltName = DNS:${AWX_HOST}"
17. cd base
18. sudo nano zwx.yaml -> change host to awx.znext.com
19. sudo nano kustomization.yaml -> change both the passwords
20. sudo mkdir -p /data/postgres-13
21. sudo mkdir -p /data/projects
22. sudo chmod 755 /data/postgres-13
23. sudo chown 1000:0 /data/projects
24. cd ..
25. kubectl apply -k base
26. kubectl -n awx logs -f deployments/awx-operator-controller-manager
27. kubectl -n awx get awx,all,ingress,secrets

## tools
1. sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
2. sudo dnf upgrade
3. sudo dnf install snapd
4. sudo systemctl enable --now snapd.socket
5. sudo ln -s /var/lib/snapd/snap /snap
6. sudo snap install btop

## Gold copy
1. Install via dvd iso
2. use custom and vmnet1
3. root and admin password
4. change sunil390 to Administrator
5. register with subscription manager
```
sudo subscription-manager register
Registering to: subscription.rhsm.redhat.com:443/subscription
Username: sunil390
Password: 
The system has been registered with ID: ccba1542-4c06-43f2-aecb-25394a6b51b6
The registered system name is: rhel8
```
6. about -> Subscribe -> Enable
7. sudo dnf upgrade
