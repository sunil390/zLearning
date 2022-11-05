## 5th November Ansible-Navigator and builder # rhel 8.6

https://infohub.delltechnologies.com/l/dell-powermax-ansible-modules-best-practices-1/creating-ansible-execution-environments-using-ansible-builder

```
nano .bashrc
alias python3='python3.9'
```
1. python3 -m pip install ansible-navigator --user
2. echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.profile
3. source ~/.profile
4. python3 -m pip install ansible-builder
5. execution environment and requirements.txt
```
execution-environment
---
version: 1

# build_arg_defaults:
#  EE_BASE_IMAGE: 'quay.io/ansible/ansible-runner:stable-2.10-devel'

#ansible_config: 'ansible.cfg'

dependencies:
  galaxy: requirements.yml
  python: requirements.txt
#  system: bindep.txt

additional_build_steps:
  prepend: |
    RUN whoami
    RUN cat /etc/os-release
  append:
    - RUN echo This is a post-install command!
    - RUN ls -la /etc
 
 requirements.txt
 jmespath>=1.0.1

 requirements.yml
 collections:
 - name: community.general

```
 6. ansible-builder build  <<< will take an hour to build.
 7. podman images
 ```
 [sunil390@sunil390 context]$ podman images
REPOSITORY                                 TAG         IMAGE ID      CREATED         SIZE
localhost/ansible-execution-env            latest      b51d4637a6ca  19 minutes ago  1.04 GB
<none>                                     <none>      e126e4efd608  31 minutes ago  1.02 GB
<none>                                     <none>      8db440aa8822  43 minutes ago  816 MB
quay.io/ansible/ansible-runner             latest      bec0dc171168  6 months ago    816 MB
quay.io/ansible/ansible-builder            latest      b0348faa7f41  8 months ago    779 MB
quay.io/ansible/ansible-navigator-demo-ee  0.6.0       e65e4777caa3  15 months ago   1.35 GB
 ```

## 31st Oct ansible install on rhel 8.6

1. sudo dnf update
2. sudo yum install python39
3. sudo python3.9 -m pip install --upgrade pip
4. sudo python3.9 -m pip install ansible
5. sudo pip3.9 install jmespath

## 30th Oct 2022 

### Jinja2
1. Variable {{ variable_name  }}
```
    - name: template task
      template:
        src: index.html.j2
        dest: /var/www/html/index.html
        mode: u=rw,g=r,o=r
```
2. Controlling flow : condition checking with % .... %


```
  server_name _;

        {% if status_url is defined -%}
        location /{{ status_url }} {
            stub_status on;
        }
        {%- endif %}
```
3. Loops:  
```
{% for ip in ansible_all_ipv4_addresses %}
    {{ ip }}<br />
{% endfor %}
```
4. Whitespace control: Do not indent jinja statements
```
<div>
{% if say_hello %}
    Hello, world
{% endif %}
</div>
```
5. filters: filters only apply to that instance of the variable.
5.1 Jija trim filter will remove the \n from the "from_yaml" filter.
5.2 to_json(indent=8) will make the output file readable.



## 26th Oct
json_query
pip install jmespath

## 21st Oct 2022 Installing latest Ansible https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

A. User Install.

1. python3 -m pip install --user ansible
2. update path
```
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:/home/pi/.local/bin:$PATH"
```
B. Global Install
```
sudo python3 -m pip install ansible
```
1. ansible-galaxy collection install ansible.utils
2. ansible-galaxy collection install community.general 

## 4th Oct 2021

Storage Activities 
<https://github.com/billpereira/zos-iaac-demo>


## 3rd Oct 2021

Installed 1.4.0 beta1 tarball after downloading from <https://galaxy.ansible.com/ibm/ibm_zos_core>

```bash
from gitlab-runner login 
ansible-galaxy collection install ibm-ibm_zos_core-1.4.0-beta.1.tar.gz
```
Commented "#  connection: ibm.ibm_zos_core.zos_ssh" from the playbooks as it was causing "the connection plugin 'ibm.ibm_zos_core.zos_ssh' was not found" error as described in <https://github.com/ansible-collections/ibm_zos_core/releases>


## 18th Sept 2021

1. Removed ansible 2.9.6
```bash
sudo apt-get remove ansible
```
2. Install PIP
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
3. Installed Ansible Globally
```bash
$ sudo python3 get-pip.py
$ sudo python3 -m pip install ansible
```
4. removed galaxy from gitlab-runner 
```bash
rm -r .ansible

ansible-galaxy collection install ibm.ibm_zos_core
ansible-galaxy collection install ibm.ibm_zosmf
```


## August 2021

```bash
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


```

