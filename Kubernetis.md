# AWX install in Kubernetes

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
