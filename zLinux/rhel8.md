# RHEL on x86

## Expose /etc/hosts to Pods on K3s
1. sudo nano /etc/hosts
```
192.168.2.87 awx.znext.com
192.168.2.87 git.znext.com
```
2. sudo dnf install dnsmasq
3. sudo systemctl enable dnsmasq --now
4. sudo tee /etc/rancher/k3s/resolv.conf <<EOF
nameserver 192.168.2.87
EOF
5. Resolver config.  
``` 
ExecStart=/usr/local/bin/k3s \
    server \
        '--write-kubeconfig-mode' \
        '644' \
        '--resolv-conf' \     👈👈👈
        '/etc/rancher/k3s/resolv.conf' \ 👈👈👈 
```
6. sudo systemctl daemon-reload
7. sudo systemctl restart k3s
8. kubectl -n kube-system delete pod -l k8s-app=kube-dns
9. sudo systemctl restart dnsmasq
10. kubectl run -it --rm --restart=Never busybox --image=busybox:1.28 -- nslookup git.znext.com
11. dnsmasq issue

                                               
## Gitea for AWX
1. cd awx-on-k3s
2. GIT_HOST="git.znext.com"
3. openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -out ./git/tls.crt -keyout ./git/tls.key -subj "/CN=${GIT_HOST}/O=${GIT_HOST}" -addext "subjectAltName = DNS:${GIT_HOST}"
4. nano git/ingress.yaml  -> update hostname
5. sudo mkdir -p /data/git
6. kubectl apply -k git
7. kubectl -n git get all,ingress
8. access https://git.znext.com , In the first config scree update Git Base url as https://git.znext.com
9. First logged in user will be the Administrator of Gitea
10. go to zansible folder git remote add origin https://git.znext.com/Sunil390/zAnsible.git
11. git config --global http.sslVerify false
12. git push -u origin main

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
28. C:\Windows\System32\Drivers\etc\hosts   -> 192.168.2.87 awx.znext.com

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
