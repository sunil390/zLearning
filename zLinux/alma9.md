# Almalinux9 on x86

## 1 - alma linux 9.4 - fresh sequence.

1. deselect sidechannel mitigation from advance options in vm player workstation 17.6.1
2. in display settings delected accelerate 3D graphics - else desktop was not responding
3. increase disk to 60 gb
4. select network - bridge and custom vmten0
5. add superuser
6. change timezone to local timezone
7. complete install and reboot.
8. sudo dnf install epel-release -y
9. sudo dnf install xrdp -y
10. sudo systemctl enable xrdp --now
11. sudo systemctl status xrdp
12. sudo firewall-cmd --new-zone=xrdp --permanent
13. sudo firewall-cmd --zone=xrdp --add-port=3389/tcp --permanent
14. sudo firewall-cmd --zone=xrdp --add-source=192.168.1.0/24 --permanent  or sudo firewall-cmd --add-port=3389/tcp --permanent
15. sudo firewall-cmd --reload
16. sudo reboot now
17. sudo dnf upgrade
18. sudo dnf install snapd
19. sudo systemctl enable --now snapd.socket
20. sudo ln -s /var/lib/snapd/snap /snap
21. sudo snap install btop

## postgres15 26th May 2024
1. sudo mkdir -p /data/postgres-15
2. sudo chmod 755 /data/postgres-15
3. cd ..
2. kubectl apply -k base
2. kubectl -n awx logs -f deployments/awx-operator-controller-manager




## K3S Upgrade  25th May 2024
1. curl -sfL https://get.k3s.io | sh -s - --write-kubeconfig-mode 644
2. sudo nano /etc/rancher/k3s/resolv.conf nameserver 192.168.2.85
3. sudo nano /etc/systemd/system/k3s.service

```
ExecStart=/usr/local/bin/k3s \
    server \
        '--write-kubeconfig-mode' \
        '644' \
        '--resolv-conf' \
        '/etc/rancher/k3s/resolv.conf' \ 
``` 
4. sudo service k3s stop  
5. Restart Linux.


## awx Upgrade 25th May 2024.
1. cd ~
2. sudo rm -rf awx-operator
3. git clone https://github.com/ansible/awx-operator.git
4. cd awx-operator
5. git checkout 2.17.0
6. export NAMESPACE=awx
7. make deploy
8. kubectl -n awx logs -f deployments/awx-operator-controller-manager -c awx-manager


## External [MariaDB](https://www.atlantic.net/dedicated-server-hosting/how-to-install-gitea-code-hosting-service-on-rockylinux-8/) for Gitea. - Pending

1. sudo dnf install git unzip gnupg2 nano wget -y
2. sudo dnf install mariadb-server -y
3. systemctl start mariadb
4. systemctl enable mariadb
5. sudo mysql
6. CREATE DATABASE gitea CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci';
7. GRANT ALL ON gitea.* TO 'gitea'@'%.%.%.%' IDENTIFIED BY 'gitea1911';
8. FLUSH PRIVILEGES;
9. EXIT;
10. sudo nano /etc/my.cnf.d/mariadb-server.cnf
```
...
bind-address=0.0.0.0
...
innodb_file_format = Barracuda
innodb_large_prefix = 1
innodb_default_row_format = dynamic
```
11. systemctl restart mariadb

### Gitea Config.
1. cd ~/awx-on-k3s
2. kubectl delete -k git
3. cd /data/git
4. sudo rm -rf git gitea ssh 
5. cd ~/awx-on-k3s
6. kubectl apply -k git
7. git.al9.com
8. Database Type : MySQL
9. Host : 192.168.2.85:3306
10. Username : gitea
11. Password : .....
12. Databasename : gitea
13. Sever Domain : git.al9.com
14. Gitea Base URL : https://git.al9.com
15. go to zansible folder 
16. git remote remove origin (Only if Origin Exists)
17. git remote add origin https://git.al9.com/sunil390/zAnsible.git
18. git config --global http.sslVerify false
19. git push -u origin main


## Private Registry - Work in Progress - Open Issues - Pending
1. cd awx-on-k3s
2. REGISTRY_HOST="registry.al9.com"
3. openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -out ./registry/tls.crt -keyout ./registry/tls.key -subj "/CN=${REGISTRY_HOST}/O=${REGISTRY_HOST}" -addext "subjectAltName = DNS:${REGISTRY_HOST}"
4. cd registry
5. nano ingress.yaml
```
...
    - hosts:
        - registry.al9.com     👈👈👈
      secretName: registry-secret-tls
  rules:
    - host: registry.al9.com     👈👈👈
...
```
6. kubectl run htpasswd -it --restart=Never --image httpd:2.4 --rm -- htpasswd -nbB reguser --password--
7. Replace htpasswd in registry/configmap.yaml with your own htpasswd string that generated above
8. sudo mkdir -p /data/registry
9. kubectl apply -k registry
10. kubectl -n registry get all,ingress
11. sudo dnf install podman-docker
12. sudo nano /etc/containers/registries.conf.d/myregistry.conf
```
[[registry]]
location = "registry.al9.com"
insecure = true
```
13. docker login registry.al9.com
14. testdrive registry
```
# Pull from docker.io
podman pull quay.io/smile/redis

# Tag as your own image on your private container registry
podman tag quay.io/smile/redis registry.al9.com/reguser/redis

# Push your own image to your private container registry
podman push registry.al9.com/reguser/redis

Push Error >>>>

kubectl logs registry-69df8f9f57-dntdj -c registry -n registry | less

docker run -it --rm registry.al9.com/reguser/whalesay:latest cowsay hoge

```
## K3S Upgrade  12 Mar 2024
1. curl -sfL https://get.k3s.io | sh -s - --write-kubeconfig-mode 644
2. sudo nano /etc/rancher/k3s/resolv.conf nameserver 192.168.2.85
3. sudo nano /etc/systemd/system/k3s.service

```
ExecStart=/usr/local/bin/k3s \
    server \
        '--write-kubeconfig-mode' \
        '644' \
        '--resolv-conf' \
        '/etc/rancher/k3s/resolv.conf' \ 
``` 
4. sudo service k3s stop  
5. Restart Linux.


## awx Upgrade 9th March 2024.
1. cd ~
2. sudo rm -rf awx-operator
3. git clone https://github.com/ansible/awx-operator.git
4. cd awx-operator
5. git checkout 2.12.2
6. export NAMESPACE=awx
7. make deploy
8. kubectl -n awx logs -f deployments/awx-operator-controller-manager -c awx-manager

## http to https redirect 19th Feb 2024
#### AWX
1. cd awx-on-k3s/base 
2. nano middleware.yaml
```
apiVersion: traefik.io/v1alpha1
kind: Middleware
metadata:
  namespace: kube-system
  name: hsts
spec:
  headers:
    sslRedirect: true
    forceSTSHeader: true
    stsSeconds: 63072000
    stsIncludeSubdomains: true
    stsPreload: true
```
3. kubectl -n kube-system apply -f middleware.yaml
4. kubectl -n kube-system get middleware.traefik.io
5. nano awx.yaml 
```
spec:
  ...
  ingress_annotations: |     👈👈👈
    traefik.ingress.kubernetes.io/router.middlewares: kube-system-hsts@kubernetescrd     👈👈👈
```
6. cd ..
7. kubectl apply -k base
8. kubectl -n awx logs -f deployments/awx-operator-controller-manager --tail=100
9. kubectl -n awx get ingress awx-ingress -o=jsonpath='{.metadata.annotations}' | jq

### gitea 19th Feb 2024
1. cd git
2. nano ingress.yaml 
```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: git-ingress
  annotations:     👈👈👈
    traefik.ingress.kubernetes.io/router.middlewares: kube-system-hsts@kubernetescrd     👈👈👈
```
3. cd ..
4. kubectl apply -k git

## Expose /etc/hosts to Pods on K3s 19th Feb 2024
1. sudo nano /etc/hosts
```
192.168.2.85 awx.al9.com
192.168.2.85 git.al9.com
192.168.2.85 registry.al9.com
```
2. sudo dnf install dnsmasq
3. sudo systemctl enable dnsmasq --now
4. sudo nano /etc/rancher/k3s/resolv.conf
nameserver 192.168.2.85
5. sudo nano /etc/systemd/system/k3s.service
``` 
ExecStart=/usr/local/bin/k3s \
    server \
        '--write-kubeconfig-mode' \
        '644' \
        '--resolv-conf' \
        '/etc/rancher/k3s/resolv.conf' \ 
```
6. sudo systemctl daemon-reload
7. sudo systemctl restart k3s
8. kubectl -n kube-system delete pod -l k8s-app=kube-dns
9. sudo systemctl restart dnsmasq
10. kubectl run -it --rm --restart=Never busybox --image=busybox:1.28 -- nslookup git.al9.com
11. almalinux 9.3 dnsmasq issue
```
[sunil390@alma9 ~]$ kubectl run -it --rm --restart=Never busybox --image=busybox:1.28 -- nslookup git.al9.com
If you don't see a command prompt, try pressing enter.
nslookup: can't resolve 'git.al9.com'
pod "busybox" deleted
pod default/busybox terminated (Error)

/etc/dnsmasq.conf - comment out below two parameters
# interface=lo
# bind-interfaces

sudo pkill -9 -f dnsmasq
sudo service dnsmasq restart
systemctl status dnsmasq

[sunil390@alma9 ~]$ kubectl run -it --rm --restart=Never busybox --image=busybox:1.28 -- nslookup git.al9.com
Server:    10.43.0.10
Address 1: 10.43.0.10 kube-dns.kube-system.svc.cluster.local
Name:      git.al9.com
Address 1: 192.168.2.85 alma9
pod "busybox" deleted

```

## Gitea for AWX 19th Feb 2024
1. cd awx-on-k3s
2. GIT_HOST="git.al9.com"
3. openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -out ./git/tls.crt -keyout ./git/tls.key -subj "/CN=${GIT_HOST}/O=${GIT_HOST}" -addext "subjectAltName = DNS:${GIT_HOST}"
4. nano git/ingress.yaml  -> update hostname
5. sudo mkdir -p /data/git
6. kubectl apply -k git
7. kubectl -n git get all,ingress
8. access https://git.al9.com , In the first config scree update Git Base url as https://git.al9.com
9. First logged in user will be the Administrator of Gitea
10. go to zansible folder git remote add origin https://git.al9.com/Sunil390/zAnsible.git
11. git config --global http.sslVerify false
12. git push -u origin main

## [K3S on alma9](https://github.com/kurokobo/awx-on-k3s) 18th Feb 2024
1. sudo systemctl disable firewalld --now
2. sudo systemctl disable nm-cloud-setup.service nm-cloud-setup.timer
3. sudo reboot
4. sudo dnf install -y git curl
5. curl -sfL https://get.k3s.io | INSTALL_K3S_VERSION=v1.28.6+k3s2 sh -s - --write-kubeconfig-mode 644
6. cd ~
7. git clone https://github.com/kurokobo/awx-on-k3s.git
8. cd awx-on-k3s
9. git checkout 2.12.1
10. kubectl apply -k operator
11. AWX_HOST="awx.al9.com"
12. openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -out ./base/tls.crt -keyout ./base/tls.key -subj "/CN=${AWX_HOST}/O=${AWX_HOST}" -addext "subjectAltName = DNS:${AWX_HOST}"
13. cd base
14. sudo nano awx.yaml -> change host to awx.al9.com
15. sudo nano kustomization.yaml -> change both the passwords
16. sudo mkdir -p /data/postgres-13
17. sudo mkdir -p /data/projects
18. sudo chmod 755 /data/postgres-13
19. sudo chown 1000:0 /data/projects
20. cd ..
21. kubectl apply -k base
22. kubectl -n awx logs -f deployments/awx-operator-controller-manager
23. kubectl -n awx get awx,all,ingress,secrets
24. C:\Windows\System32\Drivers\etc\hosts   -> 192.168.2.85 awx.al9.com

## tools 17th Feb 2024
1. sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
2. sudo dnf upgrade
3. sudo dnf install snapd
4. sudo systemctl enable --now snapd.socket
5. sudo ln -s /var/lib/snapd/snap /snap
6. sudo snap install btop
