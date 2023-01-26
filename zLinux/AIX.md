# AIX Fun

## Updates...
1. smitty comms and apps -> TCP/IP -> further config -> change hostname - pbaby
2. uname -S pbaby

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
11. make  ( This will take 1 hour to complete)
12. ./qemu-img create -f qcow2 hdisk0.qcow2 20G
13. Install , This will take around 2 Hours to complete.
```
./qemu-system-ppc64 \
  -cpu POWER9 \
  -machine pseries,ic-mode=xics \
  -m 8192 \
  -smp 4 \
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
  -accel tcg \
  -machine pseries,ic-mode=xics \
  -m 8192 \
  -smp 4 \
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
28.  On  Alma Linux ( 28 to 34 After every reboot)
29.  su -
30.  ip tuntap add tap0 mode tap
31.  ip link set tap0 up 
32.  echo 1 > /proc/sys/net/ipv4/conf/tap0/proxy_arp
33.  ip route add 192.168.2.100 dev tap0 
34.  arp -Ds 192.168.2.100 ens160 pub     
35.  Another Terminal $cd aix/qemu/build 
36.  Boot with NIC from 

```
./qemu-system-ppc64 \
  -cpu POWER9 \
  -machine pseries,ic-mode=xics \
  -m 8192 \
  -smp 4 \
  -serial stdio \
  -device virtio-scsi,id=scsi0 \
  -drive file=./hdisk0.qcow2,if=none,id=drive-scsi0-0-0-0,format=qcow2,cache=none \
  -device scsi-hd,bus=scsi0.0,channel=0,scsi-id=0,lun=0,drive=drive-scsi0-0-0-0,id=scsi0-0-0-0,bootindex=1 \
  -cdrom ../../AIX72.iso \
  -net nic,macaddr=56:44:45:30:31:32 \
  -net tap,script=no,ifname=tap0 \
  -prom-env "boot-command=boot disk:" \
  -prom-env "input-device=/vdevice/vty@71000000" \
  -prom-env "output-device=/vdevice/vty@71000000"

 This did not work...
  -device spapr-vlan,netdev=n0,mac=52:54:00:12:00:02 \
  -netdev tap,ifname=tap0,script=no,downscript=no,id=n0 \

```
37. chdev -l en0 -a netaddr=192.168.2.100 -a netmask=255.255.255.0 -a state=up
38. chdev -l inet0 -a route=0,192.168.2.1
39. Go to you Putty preferences and alter your “Terminal – Keyboard” settings for the “function keys and keypad” to “Xterm R6”
40. Connect Using Putty 192.168.2.100

### [AIX QuickSheets](http://www.tablespace.net/quicksheet/aix-quicksheet.pdf)
nmon
oslevel -s
lsconf
lparstat -i
uptime
smtctl


### [AIX Install Reference](https://aix4admins.blogspot.com/2020/04/qemu-aix-on-x86-qemu-quick-emulator-is.html)
### [Power9 spapr Discussion](https://gitlab.com/qemu-project/qemu/-/issues/269)
### [AIX /Linux Networking](https://www.jazakallah.info/post/how-to-setup-network-for-ibm-aix-vm-access-in-qemu)
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
