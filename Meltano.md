*** Local installation ***

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
