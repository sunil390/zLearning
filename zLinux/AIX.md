# AIX Fun

## Prerqs almalinux 8.7 [qemu 7.2](https://kwakousys.wordpress.com/2020/09/06/run-aix-7-2-on-x86-with-qemu/)


1. sudo dnf remove python3 ( python 3.6 was being called by default.
2. python3 --version
3. wget https://archive.org/download/aix_7200-04-02-2027_072020/aix_7200-04-02-2027_1of2_072020.iso
4. sudo dnf --enablerepo=powertools install ninja-build
5. sudo dnf install gcc glib2-devel pixman-devel cmake zlib-devel flex bison 
6. git clone https://gitlab.com/qemu-project/qemu.git
7. cd qemu  
8. mkdir build 
9. cd build
10. ../configure –target-list=ppc64-softmmu
11. make
12. ./qemu-img create -f qcow2 hdisk0.qcow2 20G
13. Install
```
./qemu-system-ppc64 \
  -cpu POWER9 \
  -machine pseries,ic-mode=xics \
  -m 8192 \
  -smp 2 \
  -serial stdio \
  -device virtio-scsi,id=scsi0 \
  -drive file=./hdisk0.qcow2,if=none,id=drive-scsi0-0-0-0,format=qcow2,cache=none \
  -device scsi-hd,bus=scsi0.0,channel=0,scsi-id=0,lun=0,drive=drive-scsi0-0-0-0,id=scsi0-0-0-0,bootindex=1 \
  -cdrom ../../AIX72.iso \
  -prom-env "boot-command=boot cdrom:" \
  -prom-env "input-device=/vdevice/vty@71000000" \
  -prom-env "output-device=/vdevice/vty@71000000"

```
14. Boot from Disk
```
./qemu-system-ppc64 \
  -cpu POWER9 \
  -machine pseries,ic-mode=xics \
  -m 8192 \
  -smp 2 \
  -serial stdio \
  -device virtio-scsi,id=scsi0 \
  -drive file=./hdisk0.qcow2,if=none,id=drive-scsi0-0-0-0,format=qcow2,cache=none \
  -device scsi-hd,bus=scsi0.0,channel=0,scsi-id=0,lun=0,drive=drive-scsi0-0-0-0,id=scsi0-0-0-0,bootindex=1 \
  -cdrom ../../AIX72.iso \
  -prom-env "boot-command=boot disk:" \
  -prom-env "input-device=/vdevice/vty@71000000" \
  -prom-env "output-device=/vdevice/vty@71000000"
```
15.  rmitab cron
16.  rmitab clcomd
17.  rmitab naudio2
18.  rmitab pfcdaemon
19.  stopsrc -s clcomd
20.  stopsrc -s pfcdaemon
21.  mount  -v  cdrfs  -o  ro  /dev/cd0  /mnt
22.  mkdir   /tmp/ssh_install
23.  cd  /mnt/installp/ppc
24.  cp  openssh*  /tmp/ssh_install
25.  cd  /tmp/ssh_install
26.  installp -acgXYd . openssh.base openssh.license openssh.man.en_US openssh.msg.en_US
27.  lssrc  -s  sshd
28.  ip tuntap add dev tap0 mode tap
29.  echo 1 > /proc/sys/net/ipv4/conf/tap0/proxy_arp
30.  echo 1 > /proc/sys/net/ipv4/conf/wlp0s20f3/proxy_arp
31.  ip addr add 192.168.2.4 dev tap0
32.  ip link set up tap0
33.  ip link set up dev tap0 promisc on
34.  ip route add 192.168.2.100 dev tap0
35.  arp -Ds 192.168.100.100 wlp0s20f3 pub
35. Boot with NIC

```
./qemu-system-ppc64 \
  -cpu POWER9 \
  -machine pseries,ic-mode=xics \
  -m 8192 \
  -smp 2 \
  -serial stdio \
  -drive file=./hdisk0.qcow2,if=none,id=drive-virtio-disk0 \
  -device virtio-scsi-pci,id=scsi \
  -device scsi-hd,drive=drive-virtio-disk0 \
  -cdrom ../../AIX72.iso \
  -net nic -net tap,script=no,ifname=tap0
  -prom-env "boot-command=boot disk:" \
  -prom-env "input-device=/vdevice/vty@71000000" \
  -prom-env "output-device=/vdevice/vty@71000000"

```
[ref](https://aix4admins.blogspot.com/2020/04/qemu-aix-on-x86-qemu-quick-emulator-is.html)
[Power9 Parms](https://gitlab.com/qemu-project/qemu/-/issues/269)
```
./qemu-system-ppc64 \
  -name "IBM AIX - IBM POWER9" \
  -M pseries,ic-mode=xics \
  -cpu POWER9 \
  -smp 2 \
  -m 8192 \
  -device spapr-vlan,netdev=net0,mac=52:54:00:49:53:14 \
  -netdev tap,id=net0,helper=/usr/libexec/qemu-bridge-helper,br=virbr0 \
  -cdrom ../../AIX72.iso \
  -device virtio-scsi,id=scsi0 \
  -drive file=./hdisk0.qcow2,if=none,id=drive-scsi0-0-0-0,format=qcow2,cache=none \
  -device scsi-hd,bus=scsi0.0,channel=0,scsi-id=0,lun=0,drive=drive-scsi0-0-0-0,id=scsi0-0-0-0,bootindex=1

```
