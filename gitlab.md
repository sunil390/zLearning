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

`````
