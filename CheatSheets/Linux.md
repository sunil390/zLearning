# Linux Snippets

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
