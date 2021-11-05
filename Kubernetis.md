# Kubernetis

## 5th November 2021

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

