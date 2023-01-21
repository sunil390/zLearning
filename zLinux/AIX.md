# AIX Fun

## Prerqs

1. wget https://archive.org/download/aix_7200-04-02-2027_072020/aix_7200-04-02-2027_1of2_072020.iso
2. sudo dnf --enablerepo=powertools install ninja-build
3. sudo dnf install gcc glib2-devel
4. git clone https://gitlab.com/qemu-project/qemu.git
5. cd qemu  
6. mkdir build 
7. cd build
8. ../configure –target-list=ppc64-softmmu



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

qemu-system-ppc64 \
  -name "IBM AIX - IBM POWER9" \
  -M pseries,ic-mode=xics \
  -cpu POWER9 \
  -smp 2 \
  -m 8192 \
  -device spapr-vlan,netdev=net0,mac=52:54:00:49:53:14 \
  -netdev tap,id=net0,helper=/usr/libexec/qemu-bridge-helper,br=virbr0 \
  -device virtio-scsi,id=scsi0 \
  -drive file=./disk.qcow2,if=none,id=drive-scsi0-0-0-0,format=qcow2,cache=none \
  -device scsi-hd,bus=scsi0.0,channel=0,scsi-id=0,lun=0,drive=drive-scsi0-0-0-0,id=scsi0-0-0-0,bootindex=1
```
