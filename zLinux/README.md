#zLinux

## Offline Repo

1. Download dvd image from https://access.redhat.com/downloads/content/69/ver=/rhel---7/7.9/x86_64/product-software to JumpServer
2. sudo mkdir -p  /mnt/disc
3. sudo mount -o loop rhel-server-7.9-x86_64-dvd.iso /mnt/disc
4. sudo cp /mnt/disc/media.repo /etc/yum.repos.d/rhel7dvd.repo
5. sudo chmod 644 /etc/yum.repos.d/rhel7dvd.repo
6. sudo nano /etc/yum.repos.d/rhel7dvd.repo
```
enabled=1
baseurl=file:///mnt/disc/
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
```
```
Cleanup epel repo
$ cd /etc/yum.repos.d
$ sudo rm epel-testing.repo
$ sudo rm epel.repo
```
7. sudo yum clean all
8. sudo yum repolist enabled
10. sudo yum update

## Network Connection

1. nmcli d
2. Manual nameserver override
3. sudo nano /etc/NetworkManager/conf.d/90-dns-none.conf
```
[main]
dns=none
```
4. systemctl reload NetworkManager
5. sudo nano /etc/resolv.conf
```
nameserver 8.8.8.8
```
6. systemctl reload NetworkManager
7. cat /etc/resolv.conf


[RHEL v7 to v8 in place Upgrade](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/pdf/upgrading_from_rhel_7_to_rhel_8/red_hat_enterprise_linux-8-upgrading_from_rhel_7_to_rhel_8-en-us.pdf)

[Ubuntu on Z](http://www.fargos.net/packages/README_UbuntuOnHercules.html)
