# AIX Fun

## Prerqs almalinux 8.7

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
13. 


https://gitlab.com/qemu-project/qemu/-/issues/269

```
  -nodefaults \
  -nographic \
  -prom-env input-device=/vdevice/vty@71000000 \
  -prom-env output-device=/vdevice/vty@71000000 \
  -serial tcp::9019,server,nowait \
  -monitor tcp::9020,server,nowait \
  -netdev type=user,id=mynet0,hostfwd=tcp:127.0.0.1:9018-10.0.2.18:22 \
  -drive file=images/aix-ppc64.img,format=qcow2,if=none,id=hd,media=disk,cache=unsafe \
  -device virtio-scsi-pci,id=scsi -device scsi-hd,drive=hd \
  -drive file=images/iso/blank-cdrom,format=raw,media=cdrom,cache=unsafe

./qemu-system-ppc64 \
  -name "IBM AIX - IBM POWER9" \
  -M pseries,ic-mode=xics \
  -cpu POWER9 \
  -smp 2 \
  -m 8192 \
  -device spapr-vlan,netdev=net0,mac=52:54:00:49:53:14 \
  -netdev tap,id=net0,helper=/usr/libexec/qemu-bridge-helper,br=virbr0 \
  -device virtio-scsi,id=scsi0 \
  -drive file=./hdisk0.qcow2,if=none,id=drive-scsi0-0-0-0,format=qcow2,cache=none \
  -cdrom ../../AIX72.iso \
  -device scsi-hd,bus=scsi0.0,channel=0,scsi-id=0,lun=0,drive=drive-scsi0-0-0-0,id=scsi0-0-0-0,bootindex=1

./qemu-system-ppc64 -cpu POWER9 \
  -machine pseries,ic-mode=xics -m 4096 -serial stdio \
  -drive file=./hdisk0.qcow2,if=none,id=drive-virtio-disk0 \
  -device virtio-scsi-pci,id=scsi \
  -device scsi-hd,drive=drive-virtio-disk0 \
  -cdrom ../../AIX72.iso \
  -prom-env "boot-command=boot cdrom:" \
  -prom-env "input-device=/vdevice/vty@71000000" \
  -prom-env "output-device=/vdevice/vty@71000000"
```
