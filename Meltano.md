***Local installation***

If you're running Linux or macOS and have Python 3.6, 3.7 or 3.8 installed, we recommend installing Meltano into a dedicated Python virtual environment inside the directory that will hold your Meltano projects.

Create and navigate to a directory to hold your Meltano projects:
```
mkdir meltano-projects
cd meltano-projects
```
Create and activate a virtual environment for Meltano inside the .venv directory:
```
python3 -m venv .venv
source .venv/bin/activate
```
Install the meltano package from PyPI:
```
pip3 install meltano
```
Optionally, verify that the meltano CLI is now available by viewing the version:
```
meltano --version
```

***Custom Project***
```
(.venv) sunil@Dell:~/meltano-projects$ meltano --version
meltano, version 1.77.0
(.venv) sunil@Dell:~/meltano-projects$ meltano init zdataops

(.venv) sunil@Dell:~/meltano-projects$ cd zdataops/
(.venv) sunil@Dell:~/meltano-projects/zdataops$ git init
Initialized empty Git repository in /home/sunil/meltano-projects/zdataops/.git/
(.venv) sunil@Dell:~/meltano-projects/zdataops$ git add --all
(.venv) sunil@Dell:~/meltano-projects/zdataops$ git commit -m 'Initial Meltano project'
[master (root-commit) 279f4f5] Initial Meltano project
 11 files changed, 6 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 analyze/.gitkeep
 create mode 100644 extract/.gitkeep
 create mode 100644 load/.gitkeep
 create mode 100644 meltano.yml
 create mode 100644 model/.gitkeep
 create mode 100644 notebook/.gitkeep
 create mode 100644 orchestrate/.gitkeep
 create mode 100644 requirements.txt
 create mode 100644 transform/.gitkeep
(.venv) sunil@Dell:~/meltano-projects/zdataops$
```

