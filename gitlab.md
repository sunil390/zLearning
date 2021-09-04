`````
1. The gitlab project zgitlab was created

2. added these folders to run the host_setup.yaml playbook

filter_plugins
host_vars
tasks
templates
```

3. ansible.cfg, host_setup.yaml and inventory.yml files were added.

4. added .gitlab-ci.yml 

````yaml
before_script:
  - echo "Before script section"
  - echo "For example you might run an update here or install a build dependency"
  - echo "Or perhaps you might print out some debugging details"

after_script:
  - echo "After script section"
  - echo "For example you might do some cleanup here"

build1:
  stage: build
  script:
    - echo "Do your build here"

test1:
  stage: test
  script:
    - echo "Do a test here"
    - ansible-playbook -i inventory.yml console_command.yaml

test2:
  stage: test
  script:
    - echo "Do another parallel test here"
    - echo "For example run a lint test"

deploy1:
  stage: deploy
  script:
    - echo "Do your deploy here"

5. Upon commit, pipeline starts, clones the repo to gitlab-runner@zgitlab:~/builds/pfz1t9M5/0/sunil390/zansible , 
      - pfz1t9M5 is the Name of the Runner.
      - sunil390 is the Gitlab User
      - zansible is the project name
      - builds is the default folder in gitlab-runner home folder.
      - 0 ? 

6. the ansible-playbook command is executed from the repo home location. This is awesome! no cloning or cd required...

If you already has a repository and just changed the way you do authentication to MFA, u can change your remote origin HTTP URI to use your new api token as follows:

git remote set-url origin http://oauth2:iGNMAymWeNqhztnqbLeT@gitlab.acer.com/sunil390/zansible.git

Ansible git clone
https://opensource.com/article/19/11/how-host-github-gitlab-ansible

Pushing Existing repo

cd C:\Users\zsuni\GitLab\zansible>
git remote rename origin old-origin
git remote add origin http://gitlab.znitro.com/mainframe/zansible.git
git push -u origin --all
git push -u origin --tags


`````
for https setup  https://docs.bitnami.com/bch/apps/gitlab/administration/create-ssl-certificate-nginx/

sudo mkdir /etc/gitlab/ssl/
sudo openssl genrsa -out /etc/gitlab/ssl/server.key 2048
sudo openssl req -new -key /etc/gitlab/ssl/server.key -out  /etc/gitlab/ssl/cert.csr
sudo openssl x509 -in  /etc/gitlab/ssl/cert.csr -out  /etc/gitlab/ssl/server.crt -req -signkey  /etc/gitlab/ssl/server.key  
sudo openssl rsa -des3 -in  /etc/gitlab/ssl/server.key -out privkey.pem

sudo openssl rsa -in privkey.pem -out  /etc/gitlab/ssl/server.key


update /etc/gitlab/gitlab.rb

# note the 'https' below
external_url "https://gitlab.example.com"

letsencrypt['enable'] = false

nginx['redirect_http_to_https'] = true
# For GitLab
nginx['ssl_certificate'] = "/etc/gitlab/ssl/server.crt"
nginx['ssl_certificate_key'] = "/etc/gitlab/ssl/server.key"

sudo cp /home/sathya/gitlab.rb /etc/gitlab/



sudo gitlab-ctl reconfigure

`````
