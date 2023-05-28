# OpenSSH

## Reference

1. [quickstart](https://coztoolkit.com/docs/pt-quick-inst/pt-quick-inst-doc.pdf)
2. [ssh key check](https://9to5answer.com/cannot-ssh-into-cisco-switch-invalid-key-length)
3. To disable host key checking at the inventory level, we use the below command.
```
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```
4. Similarly, to disable it at the host level,
```
ansible_ssh_extra_args='-o StrictHostKeyChecking=no'
Inventory/hosts method appears to be more secure but it only works with connection type ssh and not paramiko.
```
5. Also, to do it at the global level, we add the following in /etc/ansible/ansible.cfg.
```
host_key_checking = False
```
