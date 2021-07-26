# abc

```jcl
C:\Users\A463336>zowe  profiles create zosmf-profile zNitro --host 192.168.2.44 --port 443 --user sysprg1 --password sysprg1 --reject-unauthorized false
Profile created successfully! Path:
C:\Users\A463336\.zowe\profiles\zosmf\zNitro.yaml

host:               192.168.2.44
port:               443
user:               sysprg1
password:           password
rejectUnauthorized: false

Review the created profile and edit if necessary using the profile update command.

C:\Users\A463336>zowe  zos-jobs list jobs --zosmf-profile znitro
JOB03096 CC 0000    CFZIVP1 OUTPUT
TSU03030 ABEND S222 SYSPRG1 OUTPUT
TSU03029 ABEND S222 SYSPRG1 OUTPUT
TSU03027 ABEND S222 SYSPRG1 OUTPUT
TSU03026 JCL ERROR  SYSPRG1 OUTPUT
TSU03100            SYSPRG1 ACTIVE
TSU03099            SYSPRG1 ACTIVE
TSU03095            SYSPRG1 ACTIVE

```

## zowe setup in Ubuntu 20.04.2

<https://docs.zowe.org/stable/user-guide/cli-installcli/#installing-zowe-cli-from-an-online-registry>

### setup nodejs and npm

```shell
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

sunil390@gitlab:~$ node --version
v14.17.2

sunil390@gitlab:~$ npm --version
6.14.13
```

### zowe install
Secure credential store is pending...
<https://github.com/zowe/zowe-cli-scs-plugin/blob/master/README.md#software-requirements>

```
npm install -g @zowe/cli@zowe-v1-lts

EACCESS Errors

<https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally>

logged on as gitlab-runner

mkdir ~/.npm-global

npm config set prefix '~/.npm-global'

gitlab-runner@gitlab:~$ cat .profile
export PATH=~/.npm-global/bin:$PATH

source ~/.profile

test successful.
gitlab-runner@gitlab:~$ npm install -g jshint
/home/gitlab-runner/.npm-global/bin/jshint -> /home/gitlab-runner/.npm-global/lib/node_modules/jshint/bin/jshint
+ jshint@2.13.0
added 31 packages from 15 contributors in 2.808s

Now under gitlab-runner installed zowe cli

npm install -g @zowe/cli@zowe-v1-lts

zowe plugins install @zowe/secure-credential-store-for-zowe-cli@zowe-v1-lts

zowe plugins install @zowe/cics-for-zowe-cli@zowe-v1-lts @zowe/db2-for-zowe-cli@zowe-v1-lts @zowe/ims-for-zowe-cli@zowe-v1-lts @zowe/mq-for-zowe-cli@zowe-v1-lts @zowe/zos-ftp-for-zowe-cli@zowe-v1-lts

cics-success
db2-error
ims-success
mq-success
ftp-success

zowe --help
```

### Issuing zowe CLI from gitlab-runner ...

https://github.com/zowe/zowe-cli-scs-plugin/blob/master/README.md#software-requirements

zowe config reset CredentialManager to unsecure zowe profiles...

Will do above later...
```shell
zowe  profiles create zosmf-profile zNitro --host 192.168.2.44 --port 443 --user sysprg1 --password sysprg1 --reject-unauthorized false

zowe  zos-jobs list jobs --zosmf-profile znitro

```
