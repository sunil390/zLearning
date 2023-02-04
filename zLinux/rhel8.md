# RHEL on x86

## [Extending LVM](https://kb.vmware.com/s/article/1006371)

1. VMWare Workstation -> Extend Disk
2. Power On VM
3. Identify the device name, which is by default /dev/sda, and confirm the new size by running the command: # fdisk -l
4. Create a new primary partition: Run the command: # fdisk /dev/sda (depending the results of the step 4)
5. Press p to print the partition table to identify the number of partitions. By default, there are 2: sda1 and sda2.
6. Press n to create a new primary partition.
7. Press p for primary.
8. Press 3 for the partition number, depending on the output of the partition table print.
9. Press Enter two times.
10. Press t to change the system's partition ID.
11. Press 3 to select the newly creation partition.
12. Type 8e to change the Hex Code of the partition for Linux LVM.
13. Press w to write the changes to the partition table.
14. Restart the virtual machine.
15. Run this command to verify that the changes were saved to the partition table and that the new partition has an 8e type: # fdisk -l
16. Run this command to convert the new partition to a physical volume: # pvcreate /dev/sda3
17. Run this command to extend the physical volume: Note: To determine which volume group to extend, use the command vgdisplay. Note: Additionally, for the remainder of the commands, VolGroup00 will be unique to each Guest and should be adjusted to reflect your specific VM.  # vgextend VolGroup00 /dev/sda3
18. Run this command to verify how many physical extents are available to the Volume Group: # vgdisplay VolGroup00 | grep "Free"
19. Run the following command to extend the Logical Volume: Note: To determine which logical volume to extend, use the command lvdisplay. # lvextend -L+#G /dev/VolGroup00/LogVol00  Where # is the number of Free space in GB available as per the previous command. Use the full number output from Step 10 including any decimals.
20. Run the following command to expand the ext3 filesystem online, inside of the Logical Volume: Note: Use resize2fs instead of ext2online for non-Red Hat virtual machines. Use xfs_growfs for Red Hat, CentOS 7 and other VM Guest OS types that use the XFS file system. # ext2online /dev/VolGroup00/LogVol00
21. Run the following command to verify that the / filesystem has the new space available: # df -h /


## Upgrade to AWX Operator 1.1.4 31st Jan 2023

1. cd ~
2. sudo rm -rf awx-operator 
3. git clone https://github.com/ansible/awx-operator.git
4. cd awx-operator
5. git checkout 1.1.4  
6. export NAMESPACE=awx 
7. make deploy
8. kubectl -n awx logs -f deployments/awx-operator-controller-manager -c awx-manager


## External [MariaDB](https://www.atlantic.net/dedicated-server-hosting/how-to-install-gitea-code-hosting-service-on-rockylinux-8/) for Gitea.

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
7. git.al8.com
8. Database Type : MySQL
9. Host : 192.168.2.4:3306
10. Username : gitea
11. Password : .....
12. Databasename : gitea
13. Sever Domain : git.al8.com
14. Gitea Base URL : https://git.al8.com
15. go to zansible folder 
16. git remote remove origin (Only if Origin Exists)
17. git remote add origin https://git.al8.com/sunil390/zAnsible.git
18. git config --global http.sslVerify false
19. git push -u origin main

## Almalinux 8.7

1. download almalinux http://repo.extreme-ix.org/alma/8.7/isos/x86_64/
2. configure a new VM.
3. Custom Networking vmnet1 was used with LAN.
4. Rest of the procedures are ditto similar to the rhel 8.7 steps listed below.

## Upgrade to AWX Operator 1.1.3

1. cd ~
2. git clone https://github.com/ansible/awx-operator.git
3. cd awx-operator
4. git checkout 1.1.3  
5. export NAMESPACE=awx 
6. make deploy
7. kubectl -n awx logs -f deployments/awx-operator-controller-manager -c awx-manager

## Private Registry - Work in Progress - Open Issues
1. cd awx-on-k3s
2. REGISTRY_HOST="registry.znext.com"
3. openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -out ./registry/tls.crt -keyout ./registry/tls.key -subj "/CN=${REGISTRY_HOST}/O=${REGISTRY_HOST}" -addext "subjectAltName = DNS:${REGISTRY_HOST}"
4. cd registry
5. nano ingress.yaml
```
...
    - hosts:
        - registry.znext.com     👈👈👈
      secretName: registry-secret-tls
  rules:
    - host: registry.znext.com     👈👈👈
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
location = "registry.znext.com"
insecure = true
```
13. docker login registry.znext.com
14. testdrive registry
```
# Pull from docker.io
podman pull quay.io/smile/redis

# Tag as your own image on your private container registry
podman tag quay.io/smile/redis registry.znext.com/reguser/redis

# Push your own image to your private container registry
podman push registry.znext.com/reguser/redis

Push Error >>>>

kubectl logs registry-69df8f9f57-dntdj -c registry -n registry | less

docker run -it --rm registry.znext.com/reguser/whalesay:latest cowsay hoge

```

## http to https redirect
#### AWX
1. cd awx-on-k3s/base 
2. nano middleware.yaml
```
apiVersion: traefik.containo.us/v1alpha1
kind: Middleware
metadata:
  name: redirect
spec:
  redirectScheme:
    scheme: https
    permanent: true
```
3. kubectl -n default apply -f middleware.yaml
4. kubectl -n default get middleware
5. nano awx.yaml 
```
spec:
  ...
  ingress_annotations: |      👈👈👈
    traefik.ingress.kubernetes.io/router.middlewares: default-redirect@kubernetescrd      👈👈👈
```
6. cd ..
7. kubectl apply -k base
8. kubectl -n awx logs -f deployments/awx-operator-controller-manager --tail=100
9. kubectl -n awx get ingress awx-ingress -o=jsonpath='{.metadata.annotations}' | jq
### gitea
1. cd git
2. nano ingress.yaml 
```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: <resource name>
  annotations:     👈👈👈
    traefik.ingress.kubernetes.io/router.middlewares: default-redirect@kubernetescrd     👈👈👈
...
```
3. cd ..
4. kubectl apply -k git

## Expose /etc/hosts to Pods on K3s
1. sudo nano /etc/hosts
```
192.168.2.87 awx.znext.com
192.168.2.87 git.znext.com
```
2. sudo dnf install dnsmasq
3. sudo systemctl enable dnsmasq --now
4. sudo nano /etc/rancher/k3s/resolv.conf
nameserver 192.168.2.87
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
10. kubectl run -it --rm --restart=Never busybox --image=busybox:1.28 -- nslookup git.znext.com
11. dnsmasq issue
```
systemctl status dnsmasq output shows as failed.
Dec 18 04:58:54 rhel8 dnsmasq[119706]: failed to create listening socket for port 53: Address already in use

ps ax | grep dnsmasq
   2082 ?        S      0:00 /usr/sbin/dnsmasq --conf-file=/var/lib/libvirt/dnsmasq/default.conf --leasefile-ro --dhcp-script=/usr/libexec/libvirt_leaseshelper
   2084 ?        S      0:00 /usr/sbin/dnsmasq --conf-file=/var/lib/libvirt/dnsmasq/default.conf --leasefile-ro --dhcp-script=/usr/libexec/libvirt_leaseshelper
 124778 pts/0    S+     0:00 grep --color=auto dnsmasq

netstat -anp | egrep "list|53"
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
tcp        0      0 192.168.122.1:53        0.0.0.0:*               LISTEN      -
tcp        0      0 10.42.0.1:37530         10.42.0.16:8181         TIME_WAIT   -
tcp        0      0 10.42.0.1:37538         10.42.0.16:8181         TIME_WAIT   -
tcp6       0      0 192.168.2.87:10250      10.42.0.3:53904         ESTABLISHED -
udp        0      0 192.168.122.1:53        0.0.0.0:*                           -

sudo pkill -9 -f dnsmasq
sudo service dnsmasq restart
systemctl status dnsmasq

kubectl run -it --rm --restart=Never busybox --image=busybox:1.28 -- nslookup git.znext.com
Server:    10.43.0.10
Address 1: 10.43.0.10 kube-dns.kube-system.svc.cluster.local
Name:      git.znext.com
Address 1: 192.168.2.87 rhel8
pod "busybox" deleted
```

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
18. sudo nano awx.yaml -> change host to awx.znext.com
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
