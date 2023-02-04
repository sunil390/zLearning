# zLinux

## [qemu networking](https://gist.github.com/extremecoders-re/e8fd8a67a515fee0c873dcafc81d811c)



## Qemu 

1. su -
2. ip tuntap add tap0 mode tap
3. ip link set tap0 up
4. echo 1 > /proc/sys/net/ipv4/conf/tap0/proxy_arp
5. ip route add 192.168.2.101 dev tap0
6. arp -Ds 192.168.2.101 ens160 pub
8. sudo dnf install libslirp-devel dhclient
7. git clone https://github.com/qemu/qemu.git
8. cd qemu && ./configure --target-list=s390x-softmmu --enable-slirp && make
9. ./qemu/build/qemu-img create -f qcow2 almalinux.qcow2 20G
10. cd build
```
./qemu-system-s390x -M s390-ccw-virtio \
  -cpu qemu -m 4G -smp 3 \
  -drive file=../../AlmaLinux-9.1-s390x-dvd.iso,media=cdrom,if=none,id=drive-virtio-disk1 \
  -device virtio-scsi -device scsi-cd,drive=drive-virtio-disk1,id=virtio-disk1,bootindex=1 \
  -drive file=../../almalinux.qcow2,if=none,id=drive-virtio-disk0 \
  -device virtio-blk-ccw,drive=drive-virtio-disk0,id=virtio-disk0,bootindex=2,scsi=off \
  -nic user,model=virtio,hostfwd=tcp::2222-:22 \
  -nographic -display none -serial mon:stdio

```

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
