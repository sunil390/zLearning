# Prereqs

```
Runner Install
--------------
curl -LJO "https://gitlab-runner-downloads.s3.amazonaws.com/latest/deb/gitlab-runner_amd64.deb"
sudo dpkg -i gitlab-runner_amd64.deb

sudo passwd gitlab-runner

sudo gitlab-runner register

Ansible User Install
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

From gitlab-runner id
ansible-galaxy collection install ibm.ibm_zos_core

ansible-galaxy collection install ibm.ibm_zosmf

ansible-galaxy collection install ibm.ibm_zos_zosmf


````