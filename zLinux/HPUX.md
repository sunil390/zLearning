# HPUX

## Ready to load 10.2 system https://archive.org/details/hpux_20200510
```
Network is configured as follows:
ethernet    10.0.2.12
netmask    255.255.255.0
gateway    10.0.2.2
DNS          8.8.8.8

So make sure you are setting up 10.0.2.2 your bridge br0 device on your Linux machine for the network to be operational !

Credentials:
root:p4ssw0rd
user:p4ssw0rd
```
1.  wget https://archive.org/details/hpux_20200510/hpux.img
2.  cd hpux/qemu/build
3.  
```
./qemu-system-hppa \
-m 1024 \
-boot menu=on \
-drive if=scsi,bus=0,index=6,file=../../hpux.img,format=raw \
-net nic,model=tulip \
-net tap,script=no,ifname=tap0 \
-boot c \
-serial telnet::4441,server \
-nographic
```
### root password reset.
1. added -boot menu=on 
2. BO ISL
3. Interact with ISL -> Y
4. hpux -is
5. passwd root
### Disable mail daemon
1. vi /etc/rc.config.d/mailservs
2. set the line "export SENDMAIL_SERVER=1" to be "export SENDMAIL_SERVER=0"

### Network Issues.  [Multiple ip's](https://support.hpe.com/hpesc/public/docDisplay?docId=emr_na-c02949912)

1. lanscan
2. ifconfig lan0 192.168.2.200 netmask 255.255.255.0 up
3. ifconfig lan0
4. route add default 192.168.2.1

### HP-UX Cheat Sheet 

http://www.unixmantra.com/2013/04/hp-ux-cheat-sheet.html

## Prep for cool term

1. Install Ubuntu 22.04.1 Server
2. sudo apt install slim
3. sudo apt install ubuntu-desktop
4. sudo reboot
5. sudo apt-get install build-essential
6. sudo apt install -y qtcreator qtbase5-dev qt5-qmake cmake qtdeclarative5-dev
7. sudo dnf install qt5-qtbase qt5-qtbase-devel
8. git clone https://github.com/Swordfish90/qmltermwidget.git
9. cd qmltermwidget
10. export PATH=$PATH:/usr/lib/qt5/bin 
11. sudo add-apt-repository ppa:vantuz/cool-retro-term
12. sudo apt update
13. sudo apt install cool-retro-term
14. sudo apt install build-essential qmlscene qml-module-qtquick-controls2 qml-module-qtgraphicaleffects qml-module-qtquick-dialogs \
    qml-module-qtquick-localstorage qml-module-qtquick-window2 qml-module-qt-labs-settings qml-module-qt-labs-folderlistmodel qtquickcontrols2-5-dev
14. qmake && make
15. qmlscene -I . test-app/test-app.qml
16. git clone --recursive https://github.com/Swordfish90/cool-retro-term.git
17. cd cool-retro-term
18. qmake && make
19. ./cool-retro-term

## HP-UX

1. https://archive.org/download/hpux-11i-v3
2. sudo apt install ninja-build gcc libglib2.0-dev libpixman-1-dev zlib1g zlib1g-dev cmake flex bison pkg-config -y
3. mkdir hpux && cd hpux && git clone git clone https://github.com/qemu/qemu.git
4. cd qemu && ./configure --target-list=hppa-softmmu
5. cd build && cp qemu-system-hppa ../../qemu-system-hppa
6. cd .. && ./qemu-system-hppa --version
7. sudo apt install uml-utilities net-tools bridge-utils
8. sudo passwd root (change password of root)
9. su -
```
ip tuntap add tap0 mode tap
ip link set tap0 up
echo 1 > /proc/sys/net/ipv4/conf/tap0/proxy_arp
ip route add 192.168.2.200 dev tap0
arp -Ds 192.168.2.200 ens33 pub
```
9. dd if=/dev/zero of=hpux.img bs=1024 count=8M
10.  ./qemu-system-hppa -boot d \
           -serial telnet::4441,server 
           -drive if=scsi,bus=0,index=6,file=../../hpux.img,format=raw 
           -serial mon:stdio 
           -D /tmp/foo 
           -nographic 
           -m 512 
           -d nochain 
           -cdrom ../../HPUX11iv3_Disc1.iso 
           -D /tmp/foo 
           -net nic,model=tulip  
           -net tap,script=no,ifname=tap0


11. telnet 192.168.2.36 4441
12. Redy to use 10.2 https://archive.org/details/hpux_20200510
13. https://supratim-sanyal.blogspot.com/2019/11/hpux-11i-v1-hpux-1111-pa-risc-guest.html
14. https://astr0baby.wordpress.com/2019/04/28/running-hp-ux-11-11-on-qemu-system-hppa/
