# AWX install in Kubernetes

## Microk8s on rhel 8.6

[AWX on CentOS/RHEL](https://computingforgeeks.com/install-and-configure-ansible-awx-on-centos/)

1. sudo dnf -y update
2. sudo systemctl disable firewalld --now
3. sudo reboot
4. sudo setenforce 0
5. sudo sed -i 's/^SELINUX=.*/SELINUX=permissive/g' /etc/selinux/config
6. cat /etc/selinux/config | grep SELINUX=

### firewall rhel

1. sudo firewall-cmd --list-services
2. sudo firewall-cmd --permanent --add-port 30080/tcp
3. nmap localhost
4. sudo firewall-cmd --list-all
5. sudo systemctl disable firewalld --now


### Nfs Setup 

1. sudo systemctl start nfs-server
2. sudo systemctl status nfs-server


### MicroK8s on rhel8.6
1. Download and install rhel 8.6 from Redhat developer
2. sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
3. sudo dnf upgrade
4. sudo subscription-manager repos --enable "rhel-*-optional-rpms" --enable "rhel-*-extras-rpms"
5. sudo yum update
6. sudo yum install snapd
7. sudo systemctl enable --now snapd.socket
8. sudo ln -s /var/lib/snapd/snap /snap
9. sudo snap install microk8s --classic
10. sudo usermod -a -G microk8s sunil390 && sudo chown -f -R sunil390 ~/.kube
11. echo "alias kubectl='microk8s kubectl'" >> ~/.bashrc && source ~/.bashrc
12. microk8s enable dns:192.168.2.1
13. microk8s enable storage
14. microk8s enable ingress
15. microk8s enable metallb:192.168.2.200-192.168.2.210
16. microk8s enable dashboard
17. microk8s enable registry


### Monitoring Cockpit
1. sudo yum install cockpit
2. sudo systemctl enable --now cockpit.socket
3. http://192.168.2.87:9090

### [Certificate Setup](https://www.baeldung.com/openssl-self-signed-cert)

1. Root CA: openssl req -x509 -nodes -sha256 -days 3650 -newkey rsa:4096 -keyout rootCA.key -out rootCA.crt
```
Country Name (2 letter code) [XX]:IN
State or Province Name (full name) []:KA
Locality Name (eg, city) [Default City]:Bengaluru
Organization Name (eg, company) [Default Company Ltd]:sunil390
Organizational Unit Name (eg, section) []:rnd
Common Name (eg, your name or your server's hostname) []:rootCA
Email Address []:sunil390@gmail.com
```
2. Cert Request: Cert Req: openssl req -newkey rsa:4096 -nodes -keyout awx.key -out awx.csr
```
Country Name (2 letter code) [XX]:IN
State or Province Name (full name) []:KA
Locality Name (eg, city) [Default City]:Bengaluru
Organization Name (eg, company) [Default Company Ltd]:sunil390
Organizational Unit Name (eg, section) []:rnd
Common Name (eg, your name or your server's hostname) []:awx.com
Email Address []:sunil390@gmail.com
Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
```
3. Configuration Text : awx.ext
```
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
subjectAltName = @alt_names
[alt_names]
DNS.1 = awx.sunil390.com
```
4. openssl x509 -req -CA rootCA.crt -CAkey rootCA.key -in awx.csr -out awx.crt -days 3650 -CAcreateserial -extfile awx.ext
```
Signature ok
subject=C = IN, ST = KA, L = Bengaluru, O = sunil390, OU = rnd, CN = awx.com, emailAddress = sunil390@gmail.com
Getting CA Private Key
```
5. base64 encoding: cat awx.crt|base64 -w0 
6. openssl x509 -text -noout -in awx.crt
  1. .crt is X.509 certificate that's ASCII PEM-encoded
```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            72:d5:8d:e8:fc:0a:fe:07:23:3d:eb:2a:0d:68:32:18:bd:54:12:19
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = IN, ST = KA, L = Bengaluru, O = sunil390, OU = rnd, CN = rootCA, emailAddress = sunil390@gmail.com
        Validity
            Not Before: May 22 12:31:55 2022 GMT
            Not After : May 19 12:31:55 2032 GMT
        Subject: C = IN, ST = KA, L = Bengaluru, O = sunil390, OU = rnd, CN = awx.com, emailAddress = sunil390@gmail.com
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (4096 bit)
                Modulus:
                    00:c2:0d:02:bf:65:da:d0:70:72:30:8e:92:c2:7d:
                    e5:a3:8c:ad:f4:48:e2:a5:a0:e5:77:6c:c8:1e:00:
                    39:12:9e:c0:3c:c1:c1:97:42:f8:fa:85:9e:ee:0b:
                    5c:73:82:28:e0:1f:90:e8:b5:96:74:79:0e:97:f6:
                    e8:67:99:d4:a5:24:0f:e3:03:52:2a:35:2e:d1:4f:
                    a6:9d:cb:10:cc:08:6e:09:e1:b6:82:3b:2c:61:e0:
                    d1:33:1c:5e:24:c3:39:30:7d:0a:05:cb:ab:66:b6:
                    de:a1:80:85:f8:2a:89:42:cc:c3:66:3e:a1:96:98:
                    92:80:8f:2d:9f:ab:80:dd:08:9f:f0:ea:2c:aa:05:
                    55:a8:4b:3d:86:57:2e:e4:04:5d:2c:6f:cc:a1:53:
                    a4:70:d3:fc:df:2b:69:c3:80:2f:86:94:e1:bd:4c:
                    dc:87:bf:1a:5c:d4:ed:e1:10:48:09:40:a1:82:23:
                    fb:c8:6d:7f:bb:7c:88:50:3d:b3:26:23:40:30:5d:
                    b5:9d:41:61:d9:45:43:df:07:40:d4:56:f1:5c:cc:
                    8b:85:39:c7:7e:55:d9:0c:fd:41:18:d7:4b:33:bf:
                    97:2e:92:a3:28:ee:a7:c0:86:f4:56:ff:ca:57:5a:
                    db:06:a9:5e:9c:45:9a:55:24:32:03:8d:66:a4:46:
                    4a:c1:db:c8:09:1f:6f:67:08:d4:58:10:d5:8f:d1:
                    01:aa:18:12:16:b3:8e:7f:80:5c:80:d0:7f:29:aa:
                    d3:bd:21:f1:0c:ad:76:32:81:95:7d:f0:05:e2:c2:
                    ff:68:96:78:85:34:38:2a:72:1d:fb:d4:c0:b6:57:
                    28:6e:a7:03:47:51:fe:e9:30:cd:bf:f8:cf:9f:49:
                    eb:31:d5:6e:84:da:f1:4b:77:12:68:4c:48:4e:c6:
                    e7:d1:e5:8b:2e:02:54:47:f2:57:2b:1a:ab:d0:7a:
                    4d:f9:68:ac:d5:40:c1:10:93:0b:42:ea:ae:44:5e:
                    d1:a2:4c:af:00:1d:ea:3b:7b:f2:fb:40:81:3a:71:
                    08:89:8a:01:44:6f:35:cb:5b:11:dc:d4:e2:37:60:
                    5c:5a:91:d4:6f:76:21:73:e4:26:aa:9a:5e:e2:e9:
                    1a:b2:9c:63:70:2d:99:2d:94:97:de:f2:e0:bf:a3:
                    d4:3e:63:e9:d1:1f:5e:1e:89:d5:2d:53:37:96:15:
                    c2:76:f1:46:bc:aa:1b:87:e3:82:4d:c9:25:6a:8a:
                    f4:50:4c:c9:57:e9:ab:b7:0d:b6:d8:6c:fb:0f:53:
                    62:ef:ea:e4:95:e9:ae:d4:58:35:97:8c:8e:c1:21:
                    06:f6:7a:7a:c8:16:0d:43:c0:e2:0e:ee:51:6b:c5:
                    5f:58:11
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Authority Key Identifier:
                keyid:C2:8B:6B:65:15:B2:25:4A:BD:8C:4F:C7:8E:03:E2:58:2C:A2:07:3E

            X509v3 Basic Constraints:
                CA:FALSE
            X509v3 Subject Alternative Name:
                DNS:awx.sunil390.com1~
    Signature Algorithm: sha256WithRSAEncryption
         21:b2:6a:cd:42:2b:61:78:bb:fb:c5:b7:7f:23:1a:6a:ec:8f:
         6e:b0:30:fd:71:f2:00:84:ce:7e:07:3f:d8:c3:ab:a9:ec:e7:
         82:84:db:64:7d:9c:7b:30:ab:80:95:b6:f4:0c:8f:c9:62:6c:
         e0:59:00:96:24:91:5f:7b:df:0c:a3:20:7f:9b:e3:13:3e:3d:
         66:15:f9:d4:57:b2:92:ad:f4:bb:be:3b:8e:00:0b:4b:6e:0f:
         6a:92:e9:2a:e2:79:62:4b:d1:03:31:db:e8:52:34:e5:e7:20:
         d2:5c:e5:6b:2e:ba:15:65:2e:5f:9e:56:2a:c3:1d:54:46:1b:
         06:b2:00:3b:bd:10:5d:47:90:91:bf:48:c8:a8:ed:4c:02:62:
         8f:08:16:d5:a2:9b:67:d2:13:ca:70:c8:22:38:fa:d1:c7:d4:
         73:93:2f:af:f7:cf:6c:e2:14:2e:37:21:00:fc:7f:ac:5c:2d:
         30:31:3b:f5:b9:3a:0b:40:6c:31:82:37:1d:3d:46:55:e1:45:
         63:2c:78:33:0a:09:85:da:ac:77:c0:c8:13:76:c0:ac:2d:9e:
         eb:68:63:a3:9d:cc:a2:71:6e:1b:e9:6b:51:ac:b4:9d:3f:7d:
         d3:32:2e:a6:e6:d5:c7:be:f0:ed:22:0d:7c:55:4b:ce:4e:45:
         56:79:08:4c:46:9d:78:c1:42:7f:8b:23:84:86:aa:57:fa:19:
         b3:40:9f:dd:5b:d0:ed:00:78:f0:6f:19:6a:7d:b0:70:7c:1f:
         9d:a7:b3:1e:75:9a:30:16:6a:67:6a:6a:b2:74:e9:25:ac:68:
         f4:03:28:41:fb:d9:de:76:13:a1:17:88:68:c6:58:ae:80:58:
         cf:81:16:d6:f8:9a:e6:b6:75:49:e8:12:75:61:3f:77:66:ed:
         42:0c:c6:99:ac:5a:8e:8e:3e:a1:d1:e5:7a:68:d2:b0:a6:18:
         02:be:44:05:e9:c2:12:b3:70:88:14:48:b5:5f:bb:7c:71:ce:
         47:05:10:e3:dd:68:8c:e6:d0:42:c8:88:26:9e:f1:6f:ca:90:
         fd:57:ca:3e:dc:b4:52:ec:24:9d:14:5e:06:08:00:89:59:6e:
         f3:26:ee:bd:2b:9d:75:07:19:3f:21:e7:ec:90:07:1a:e1:b9:
         7a:06:a8:9a:e5:1b:ea:69:2b:48:0e:d3:3a:d5:44:2c:fe:70:
         5d:0b:86:ca:4c:8e:cb:2e:cf:7e:2a:4f:dd:24:82:ea:0b:b7:
         a4:be:49:da:15:4e:46:37:d6:05:6f:59:da:aa:b9:28:49:74:
         31:88:7d:4b:8d:f6:78:83:7c:4b:85:bc:28:a2:dd:cc:4a:43:
         e6:40:63:b0:dc:c0:68:2d
```
6.  PEM-encoded certificate to a DER-encoded certificate
openssl x509 -in awx.crt -outform der -out awx.der

7. Combine private key and certificate into a PKCS12 file ( pfx used for importing and exporting certificate chains in Microsoft IIS)
openssl pkcs12 -inkey awx.key -in awx.crt -export -out awx.pfx

## Helm Install.

1. sudo snap install helm --classic
2. microk8s enable helm3
3. microk8s enable storage dns ingress portainer 
4. helm3 repo add awx-operator https://ansible.github.io/awx-operator/
5. helm3 repo update
6. helm3 search repo awx-operator
7.  

## Installation using Kustomize

1. curl -s "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh"  | bash
2. nano kustomization.yaml
```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  # Find the latest tag here: https://github.com/ansible/awx-operator/releases
  - github.com/ansible/awx-operator/config/default?ref=0.20.0

# Set the image tags to match the git version from above
images:
  - name: quay.io/ansible/awx-operator
    newTag: 0.20.0

# Specify a custom namespace in which to install AWX
namespace: awx
```
3. ./kustomize build . | kubectl apply -f -
4. kubectl config set-context --current --namespace=awx
5. k get pods
```
sunil390@dashb:~$ k get pods
NAME                                               READY   STATUS    RESTARTS   AGE
awx-operator-controller-manager-5d9949568d-62dkc   1/2     Running   0          3m55s
```
6. nano awx-zdino.yaml
```
---
apiVersion: awx.ansible.com/v1beta1
kind: AWX
metadata:
  name: awx-zdino
spec:
  service_type: nodeport
```
7. add awx-zdino to kustomiztion.yaml
```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  # Find the latest tag here: https://github.com/ansible/awx-operator/releases
  - github.com/ansible/awx-operator/config/default?ref=0.20.0
  - awx-zdino.yaml
# Set the image tags to match the git version from above
images:
  - name: quay.io/ansible/awx-operator
    newTag: 0.20.0

# Specify a custom namespace in which to install AWX
namespace: awx
```
8. kustomize build . | kubectl apply -f -
9. kubectl logs -f deployments/awx-operator-controller-manager -c awx-manager
10. $ kubectl get secret awx-demo-admin-password -o jsonpath="{.data.password}" | base64 --decode
yDL2Cx5Za94g9MvBP6B73nzVLlmfgPjR


## [AWX Cluster Sample](https://githubhot.com/repo/ansible/awx-operator/issues/260?page=1)

## 16th Jan 2022 Portainer

1. microk8s enable portainer
2. https://192.168.2.96:30779
3. admin / localpw


## 16th Jan HAProxy
[HAproxy](https://linuxhint.com/how-to-install-and-configure-haproxy-load-balancer-in-linux/)
[K8s MetalLB traefik](https://tansanrao.com/home-lab-infrastructure/)
1. /etc/hosts
```sh
192.168.2.5 HAproxy
192.168.2.96 awxserver1
```
2. sudo sudo apt install haproxy
3. k get svc
```
sunil390@mk8s:~$ k get svc
NAME                                              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
awx-operator-controller-manager-metrics-service   ClusterIP   10.152.183.230   <none>        8443/TCP       55d
awx-znitro-postgres                               ClusterIP   None             <none>        5432/TCP       55d
awx-znitro-service                                NodePort    10.152.183.81    <none>        80:31324/TCP   55d
gpu-operator-node-feature-discovery               ClusterIP   10.152.183.215   <none>        8080/TCP       43d
```
4. sudo nano /etc/haproxy/haproxy.cfg
```sh
frontend web-frontend
  bind 192.168.2.5:80
  mode http
  default_backend web-backend

backend web-backend
  balance roundrobin
  server awxserver1 192.168.2.96:31324 check

listen stats
  bind 192.168.2.5:8080
  mode http
  option forwardfor
  option httpclose
  stats enable
  stats show-legends
  stats refresh 5s
  stats uri /stats
  stats realm Haproxy\ Statistics
  stats auth admin:admin@9            #Login User and Password for the monitoring
  stats admin if TRUE
  default_backend web-backend
```
5. haproxy -c -f /etc/haproxy/haproxy.cfg
6. sudo systemctl restart haproxy.service
7. sudo systemctl status haproxy.service


## Upgrade to 1.23

```sh
sudo snap refresh microk8s --channel=1.23/stable
microk8s (1.23/stable) v1.23.0 from Canonical✓ refreshed
```

## 22nd Nov Galaxy collection install and end to end Playbook testing

1. <https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#install-multiple-collections-with-a-requirements-file>
2. In Git Repo create collections folder and add requirements.yml file
```yml
---
collections:
  - name: ibm.ibm_zos_core
    version: "1.4.0-beta.1"
    source: "https://galaxy.ansible.com"
```
3. ssh-keygen in ubuntu and copy privatekey from .ssh/id_rsa 
4. Add inventory and under hosts enter these rows against zos1
```yml
---
ansible_host: 192.168.2.44
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
5. In awx credentials add zos1 as machine and enter id password of sysprg1 and paste the above private key.
6. In Templates against Cancel_User select inventory and zos1 credentials
7. Launch the Template

## 20th Nov Microk8s GoldDisc and AWX Install 

### Gold Disc Creation

1. setp VM with bridged network, 5 GB memory and 25 GB disk 3 cpus
2. Install ubuntu 20.04.3 select microk8s 
3. sudo apt update
4. sudo apt upgrade
5. sudo usermod -a -G microk8s $USER && sudo chown -f -R $USER ~/.kube
6. echo "alias kubectl='microk8s kubectl'" >> ~/.bash_aliases && source ~/.bash_aliases
7. sudo nano /usr/local/bin/kubectl 
```bash
#!/bin/bash
args="$@"
microk8s kubectl $args 
```
8. sudo chmod 755 /usr/local/bin/kubectl
9. sudo apt install net-tools
10. sudo ufw allow in on cni0 && sudo ufw allow out on cni0
11. sudo ufw default allow routed

### Microk8s Customization

1. microk8s start
2. microk8s status --wait-ready
3. kubectl get nodes
4. microk8s enable dns storage ingress dashboard
5. kubectl get --all-namespaces pods
```bash
NAMESPACE     NAME                                       READY   STATUS    RESTARTS        AGE
kube-system   calico-node-zg4b7                          1/1     Running   1 (5m54s ago)   46m
kube-system   calico-kube-controllers-6bcdd9597d-kjqfj   1/1     Running   1 (5m54s ago)   46m
kube-system   coredns-7f9c69c78c-k4bd6                   1/1     Running   0               100s
traefik       traefik-ingress-controller-gktgh           1/1     Running   0               27s
kube-system   hostpath-provisioner-5c65fbdb4f-nqq28      1/1     Running   0               26s
```
6. kubectl get storageclass
```bash
NAME                          PROVISIONER            RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
microk8s-hostpath (default)   microk8s.io/hostpath   Delete          Immediate           false                  2m58s
```
### AWX Install

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
```bash
NAME                                              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
awx-operator-controller-manager-metrics-service   ClusterIP   10.152.183.230   <none>        8443/TCP       14m
awx-znitro-postgres                               ClusterIP   None             <none>        5432/TCP       9m46s
awx-znitro-service                                NodePort    10.152.183.81    <none>        80:31324/TCP   9m41s
```
14. On Windows Powershell ->  ssh -L 31324:localhost:31324 sunil390@192.168.2.96
15. kubectl get secret awx-znitro-admin-password -o jsonpath="{.data.password}" | base64 --decode

### Trouble Shooting
1. sudo apt-get install ubuntu-desktop
2. sudo apt install xrdp
3. sudo vgdisplay ubuntu-vg | grep "Free"
4. sudo lvextend  -L+3.9G /dev/ubuntu-vg/ubuntu-lv
5. sudo resize2fs /dev/ubuntu-vg/ubuntu-lv
6. df -h
7. microk8s enable dashboard
8. token=$(microk8s kubectl -n kube-system get secret | grep default-token | cut -d " " -f1) microk8s kubectl -n kube-system describe secret $token
9. kubectl port-forward -n kube-system service/kubernetes-dashboard 10443:443
10. microk8s enable metallb:192.168.2.97-192.168.2.99
11. curl 192.168.2.97 -I
12. ssh tunnelling <https://superuser.com/questions/253843/how-to-create-a-ssh-tunnel-chain-in-one-command>
```bash
echo "Host *" >> ~/.ssh/config
echo "ServerAliveInterval 60" >> ~/.ssh/config

JumpServer tunneling 
ssh -L 1115:127.0.0.1:1115 username@jumpserver1 -tt ssh -L 1115:target_db_server:1433  username@jumpserver2
```

```yml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: foo
  namespace: awx-namespace

spec:
  rules:
    - host: awx.znitro.com
      http:
        paths:
          - path: /
            pathType: Exact
            backend:
              service:
                name:  awx-znitro
                port:
                  number: 80
```

### Microk8s Reinstall

1. microk8s disable dashboard dns storage ingress
2. sudo snap remove microk8s
3. sudo snap install microk8s --classic
4. microk8s enable dns dashboard storage ingress

## 19th Nov - AWX ReInstall in Minikube

1. minikube start --cpus=3 --memory=4.5g --addons=ingress
2. cd awx-operator
3. export NAMESPACE=awx-namespace
4. make deploy
5. kubectl get pods -n $NAMESPACE
6. kubectl config set-context --current --namespace=$NAMESPACE
7. cp awx-demo.yml awx-znitro.yml (Changed demo to znitro)
```bash
---
apiVersion: awx.ansible.com/v1beta1
kind: AWX
metadata:
  name: awx-znitro
spec:
  service_type: nodeport
```
8. kubectl apply -f awx-znitro.yml
9. kubectl logs -f deployments/awx-operator-controller-manager -c awx-manager (no outputs seen error: container awx-manager is not valid for pod awx-operator-controller-manager-68d787cfbd-p4tll )
9. kubectl get pods -l "app.kubernetes.io/managed-by=awx-operator"
```bash
NAME                    READY   STATUS    RESTARTS   AGE
awx-znitro-d46576-b6qsc   4/4     Running   0          2m9s
awx-znitro-postgres-0     1/1     Running   0          2m14s
```
10. minikube service awx-znitro-service --url -n $NAMESPACE ( copy url and access the page from ubuntu desktop firefox  http://192.168.49.2:30737 )
11. kubectl get secret awx-znitro-admin-password -o jsonpath="{.data.password}" | base64 --decode (this is the password for admin )
12. login with admin and password as above.

## 18th Nov MINIKUBE

### Install Docker on Ubuntu 20.04.3

1. https://docs.docker.com/engine/install/ubuntu/
2. sudo apt-get update
3. sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
4. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
5. echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
6. sudo apt-get update
7. sudo apt-get install docker-ce docker-ce-cli containerd.io
8. sudo docker run hello-world

```
sudo vgdisplay ubuntu-vg | grep "Free"
sudo lvextend  -L+xxG /dev/ubuntu-vg/ubuntu-lv
sudo resize2fs /dev/ubuntu-vg/ubuntu-lv
sudo df -h
```

### Install Minikube 

1. https://minikube.sigs.k8s.io/docs/start/
2. curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
3. sudo install minikube-linux-amd64 /usr/local/bin/minikube
4. sudo usermod -aG docker $USER && newgrp docker
5. minikube start --cpus=3 --memory=4.5g --addons=ingress
6. alias kubectl="minikube kubectl --"

### AWX

1. git clone https://github.com/ansible/awx-operator.git --branch 0.14.0
2. cd awx-operator
3. git checkout
4. export NAMESPACE=my-namespace
5. sudo apt install make
6. sudo nano /usr/local/bin/kubectl
```bash
#!/bin/bash
args="$@"
minikube kubectl -- $args 
```
7. sudo chmod 755 kubectl
8. cd ~/awx-operator
9. make deploy
10. kubectl get pods -n $NAMESPACE
11. kubectl config set-context --current --namespace=$NAMESPACE
12. kubectl apply -f awx-demo.yml
13. kubectl logs -f deployments/awx-operator-controller-manager -c awx-manager (no outputs seen)
14. kubectl get pods -l "app.kubernetes.io/managed-by=awx-operator"
15. sudo apt-get install ubuntu-desktop
16. sudo apt install xrdp
17. minikube service awx-demo-service --url -n $NAMESPACE ( copy url and access the page from ubuntu desktop firefox)
18. kubectl get secret awx-demo-admin-password -o jsonpath="{.data.password}" | base64 --decode (this is the password for admin)
19. login with admin

## 5th November MiniKube

1. Enable HyperV https://www.xda-developers.com/how-to-install-hyper-v-windows-11-home/
copy this content to hv.bat and execute from Administrator shell 
```bash
pushd "%~dp0"
dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum >hv.txt
for /f %%i in ('findstr /i . hv.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i"
del hv.txt
Dism /online /enable-feature /featurename:Microsoft-Hyper-V -All /LimitAccess /ALL
pause
```
2. Reboot Windows11
3. Configure Minikube https://minikube.sigs.k8s.io/docs/start/
4. minikube start
5. minikube dashboard

## zowe container

1. From dashboard click cluster and click on + sight on right top corner.
2. Upload common/zowe-ns.yaml
3. Upload common/zowe-sa.yaml
4. edit samples/workspace-pvc replace hostpath with standard ( minikube kubectl get sc will list the current storage class name)
5. minikube kubectl -- apply -f samples/workspace-pvc.yaml
6. updated config-cm.yaml and certificates-secret.yaml per https://docs.zowe.org/stable/user-guide/k8s-config
