# HPUX

## Prep for cool term

1. Install Ubuntu 22.04.1 Server
2. sudo apt install slim
3. sudo apt install ubuntu-desktop
4. sudo reboot
5. sudo apt-get install build-essential
6 sudo apt install -y qtcreator qtbase5-dev qt5-qmake cmake qtdeclarative5-dev
7. git clone https://github.com/Swordfish90/qmltermwidget.git
8. cd qmltermwidget
9. export PATH=$PATH:/usr/lib/qt5/bin
10. sudo add-apt-repository ppa:vantuz/cool-retro-term
11. sudo apt update
12. sudo apt install cool-retro-term
13. sudo apt install build-essential qmlscene qml-module-qtquick-controls2 qml-module-qtgraphicaleffects qml-module-qtquick-dialogs \
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
arp -Ds 192.168.2.100 ens33 pub
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
12. 
