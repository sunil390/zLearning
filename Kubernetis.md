# AWX intsall in MiniKube

## 19th Nov - AWX ReInstall

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

## 18th Nov

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
6. cd /usr/local/bin 
8. sudo nano kubectl
```bash
#!/bin/bash
args="$@"
minikube kubectl -- $args 
```
9. sudo chmod 755 kubectl
10. cd ~/awx-operator
11. make deploy
11. kubectl get pods -n $NAMESPACE
12. kubectl config set-context --current --namespace=$NAMESPACE
13. kubectl apply -f awx-demo.yml
14. kubectl logs -f deployments/awx-operator-controller-manager -c awx-manager (no outputs seen)
15. kubectl get pods -l "app.kubernetes.io/managed-by=awx-operator"
16. sudo apt-get install ubuntu-desktop
17. sudo apt install xrdp
18. minikube service awx-demo-service --url -n $NAMESPACE ( copy url and access the page from ubuntu desktop firefox)
19. kubectl get secret awx-demo-admin-password -o jsonpath="{.data.password}" | base64 --decode (this is the password for admin)
20. login with admin


## 17th Nov 

minikube kubectl -- apply -f https://raw.githubusercontent.com/ansible/awx-operator/0.13.0/deploy/awx-operator.yaml

---
apiVersion: awx.ansible.com/v1beta1
kind: AWX
metadata:
  name: awx-znitro
spec:
  service_type: nodeport
  ingress_type: none
  hostname: awx-znitro.com

notepad awx-znitro.yml

minikube kubectl -- apply -f awx-znitro.yml

minikube kubectl -- get pods -l "app.kubernetes.io/managed-by=awx-operator"

minikube kubectl -- get svc -l "app.kubernetes.io/managed-by=awx-operator"

---
apiVersion: awx.ansible.com/v1beta1
kind: AWX
metadata:
  name: awx-nginx
spec:
  service_type: clusterip
  ingress_type: ingress
  hostname: my-awx.znitro.com

notepad awx-nginx-ingress.yml

minikube kubectl -- apply -f awx-nginx-ingress.yml

minikube kubectl -- get awx

minikube kubectl -- get pods -l "app.kubernetes.io/managed-by=awx-operator"

minikube kubectl -- get svc -l "app.kubernetes.io/managed-by=awx-operator"

minikube service list

minikube service awx-znitro-service --url

minikube delete

minikube start --addons=ingress --cpus=3 --cni=flannel --install-addons=true --kubernetes-version=stable --memory=5g --vm-driver=hyperv


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
7.   

## 5th November 2021 Microk8s

1. Installed ubuntu 20.04.3 , select microk8s , default network options (NAT)
2. Reboot ubutu after changing network option to bridge
3. Join the group  https://microk8s.io/docs
```bash
microk8s status --wait-ready
microk8s enable dashboard dns registry istio
microk8s kubectl get all --all-namespaces

sudo usermod -a -G microk8s $USER
sudo chown -f -R $USER ~/.kube
echo - $USER

nano ~/.bash_aliases - add below line 
alias kubectl='microk8s kubectl'

kubectl get nodes

microk8s stop
microk8s start
``` 
4. sudo microk8s dashboard-proxy
5. https://192.168.2.96:10443 <-- This is the Ubuntu ip

