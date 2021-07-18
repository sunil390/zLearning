
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

5. Upon commit, pipeline starts, clones the repo to gitlab-runner@zgitlab:~/builds/pfz1t9M5/0/sunil390/zansible 

6. the ansible-playbook command is executed from the repo home location.

`````