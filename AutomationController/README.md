# Ansible-Navigator and Builder on RHEL 8.6

https://infohub.delltechnologies.com/l/dell-powermax-ansible-modules-best-practices-1/creating-ansible-execution-environments-using-ansible-builder

1. python3 -m pip install ansible-navigator --user
2. echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.profile
3. source ~/.profile
4. python3 -m pip install ansible-builder
5. execution-environment.yml, requirements.yml and requirements.txt

execution-environment.yml
```
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
``` 
requirements.txt
```
---
jmespath>=1.0.1
```
requirements.yml
```
---
collections:
 - name: community.general
 - name: ansible.utils
 - name: awx.awx
 - name: ibm.ibm_zos_core
```
 6. ansible-builder build  <<< will take some time to build.
 ```
 [sunil390@sunil390 playbooks]$ ansible-builder build
Running command:
  podman build -f context/Containerfile -t ansible-execution-env:latest context
Complete! The build context can be found at: /home/sunil390/playbooks/context
 ```
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

## RHEL 8.6 Preparation.

1. sudo dnf update
2. sudo yum install python39
3. sudo python3.9 -m pip install --upgrade pip
4. sudo python3.9 -m pip install ansible
5. sudo pip3.9 install jmespath
6. Update .bashrc
```
nano .bashrc
alias python3='python3.9'
```

## Jinja2 Templates 

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
