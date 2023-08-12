# Linux Snippets

## Repo removal in Ubuntu

1. sudo add-apt-repository --remove https://ppa.launchpadcontent.net/vantuz/cool-retro-term/ubuntu
2. sudo apt update

## Static IP Linux
1. nano /etc/sysconfig/network-scripts/ifcfg-ens160
```
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=dhcp
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
NAME=ens160
IPADDR=192.168.2.87
NETMASK=255.255.255.0
UUID=7427c9f0-f98b-4fbd-b52e-321501c61af7
DEVICE=ens160
ONBOOT=yes
```

## [blk_update_request I/O Error dev fd0 sector 0 ](https://askubuntu.com/questions/719058/blk-update-request-i-o-error-dev-fd0-sector-0)

1. sudo rmmod floppy
2. echo "blacklist floppy" | sudo tee /etc/modprobe.d/blacklist-floppy.conf
3. sudo dpkg-reconfigure initramfs-tools

## Linux on Z

1. CentOS Stream9 https://www.centos.org/centos-stream/
2. SNA https://www.sinenomine.net/index.php/offerings/linux/ClefOS
3. SUSE https://www.suse.com/download/sles/
4. RHEL Trial https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux/ibm-z-linux-one/try-it
5. Ubuntu http://old-releases.ubuntu.com/releases/20.04.3/


## apt update issue
```
E: Release file for http://us.archive.ubuntu.com/ubuntu/dists/focal-updates/InRelease is not valid yet (invalid for another 36min 11s). Updates for this repository will not be applied.
E: Release file for http://us.archive.ubuntu.com/ubuntu/dists/focal-backports/InRelease is not valid yet (invalid for another 37min 5s). Updates for this repository will not be applied.
E: Release file for http://us.archive.ubuntu.com/ubuntu/dists/focal-security/InRelease is not valid yet (invalid for another 35min 33s). Updates for this repository will not be applied.
```


1. sudo apt-get -o Acquire::Check-Valid-Until=false -o Acquire::Check-Date=false update
2. sudo date --set "20 FEB 2022 3:00 AM"




## Shell Screen Recording <https://asciinema.org/docs/usage>

1. sudo apt-get install asciinema
2. asciinema rec  (control+c to stop recording and save locally)
3. asciinema play 

## passwordless ssh from powershell.

```bash
ssh-keygen
type $env:USERPROFILE\.ssh\id_rsa.pub | ssh sunil390@192.168.2.195 "cat >> .ssh/authorized_keys"
```

## To check if the ports are free on a Unix host, run:

$ netstat -an | egrep '4440|4443'

If the ports are in use on the server, you will see output similar to below:

tcp46      0      0  *.4440                 *.*                    LISTEN

## Resizing Ubuntu filesystem

<https://www.techrepublic.com/blog/smb-technologist/extending-partitions-on-linux-vmware-virtual-machines/>

1. Shutdown the VM
2. Edit Settings
3. Select the hard disk you would like to extend On the right side, make the provisioned size as large as you need it
4. Power on the VM, Connect to the command line of the Linux VM.
5. sudo fdisk -l
6. sudo fdisk /dev/sda 
7. Type p to print the partition table and press Enter
8. Type n to add a new partition
9. Type p again to make it a primary partition (This was missed)
10. from /dev/sda list pick last cylider+1 as the first cylinder Now you'll be prompted to pick the first cylinder.
11. If you want it to take up the rest of the space available (as allocated in step 4), just choose the default value for the last cylinder.
12. Type w to save these changes and Restart the VM and login.
13. fdisk -l. sda4 is now present.
14. sudo vgdisplay
15. sudo vgextend ubuntu-vg /dev/sda4)
16. sudo vgdisplay ubuntu-vg | grep "Free"
17. sudo lvextend  -L+2.99G /dev/ubuntu-vg/ubuntu-lv
18. sudo resize2fs /dev/ubuntu-vg/ubuntu-lv
19. sudo df -h
