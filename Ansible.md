# Prereqs

```
Runner Install
--------------
curl -LJO "https://gitlab-runner-downloads.s3.amazonaws.com/latest/deb/gitlab-runner_amd64.deb"
sudo dpkg -i gitlab-runner_amd64.deb

sudo passwd gitlab-runner

sudo gitlab-runner register


Ansible User Install ( Currently Ansible 2.9.6 installed through "sudo apt install ansible" alone is working )
--------------------
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py --user
python -m pip install --user ansible

sudo apt install python3-pip
pip install ansible

Ansible Global Install from sunil390
------------------------------------
sudo python3 get-pip.py
sudo python3 -m pip install ansible

Further testing required to see why ansible installed using pip is not working ...
----------------------------------------------------

After installing ansible 2.9.6 From gitlab-runner id install the IBM Collections.
ansible-galaxy collection install ibm.ibm_zos_core

ansible-galaxy collection install ibm.ibm_zosmf

ansible-galaxy collection install ibm.ibm_zos_zosmf

Created  api token 'PCrB672urixrzwXJy62c' in zgitlab 
jJrK13zf_RMwBGTRKqPk - gitlab 

gitlab-runner@zgitlab:~$ git clone http://oauth2:jJrK13zf_RMwBGTRKqPk@gitlab.znitro.com/mainframe/zansible.git


ssh issue
 PERMIT BPX.POE CLASS(FACILITY) ID(IBMUSER) ACCESS(UPDATE)   
 SETROPTS RACLIST(FACILITY) REFRESH                          

1. Generate the Key

gitlab-runner@zgitlab:~$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/gitlab-runner/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/gitlab-runner/.ssh/id_rsa
Your public key has been saved in /home/gitlab-runner/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:QLd4Q3d8XHbLNGhpFpzNtNmQMW0KCIfgjOuYPTMVcRg gitlab-runner@zgitlab
The key's randomart image is:
+---[RSA 3072]----+
|      E+=ooooo%O+|
|     =.*.+..oO**X|
|    . * +   +o B.|
|     . + .    .  |
|    . . S        |
|   = .           |
|  o *            |
|     +           |
|                 |
+----[SHA256]-----+

2. Copy the Key to z/OS

gitlab-runner@zgitlab:~$ ssh-copy-id sysprg1@znitro.hercules.com
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/gitlab-runner/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
sysprg1@znitro.hercules.com's password:
mkdir: FSUM6404 directory ".ssh": EDC5141I Read-only file system.

Changed Root to R/W from R/O

gitlab-runner@zgitlab:~$ ssh-copy-id sysprg1@znitro.hercules.com
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/gitlab-runner/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
sysprg1@znitro.hercules.com's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'sysprg1@znitro.hercules.com'"
and check to make sure that only the key(s) you wanted were added.

3. Run the Playbook.

/home/gitlab-runner/zansible> ansible-playbook -i "znitro.hercules.com," host_setup.yaml -u sysprg1 -vvv
/home/gitlab-runner/zansible> ansible-playbook -i inventory.yml console_command.yaml





````