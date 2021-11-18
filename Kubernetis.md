# Kubernetis

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

