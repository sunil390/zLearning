# Linux Softwares and zOS Integration steps
## Verification
1. Make sure below softwares are running on Linux
a. gitlab
b. gitlab-runner
c. rundeck
d. psql
e. ansible
f. your zOS lpar is up and avilable
2. on zOS make sure SSH and CSF are running and ZOAU and Python are installed.
3. open your gitlab webbrowser
create new group called Mainframe under that create new project called zansible (blank project)
4. Click add ssh key
5. on windows command prompt issue ssh-keygen.
```
C:\Users\sathi\Gitlab>ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (C:\Users\sathi/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in C:\Users\sathi/.ssh/id_rsa.
Your public key has been saved in C:\Users\sathi/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:r8rK0xmVdSNxMSFCtlM5YJQdihwkvd2XmCuee2qk1KQ sathi@LAPTOP-6RNUON34
The key's randomart image is:
+---[RSA 3072]----+
|    .oooB+=+=o   |
|     o.=.=*oo.   |
|      oo++ * o   |
|      . =.+ o    |
|       =S  o     |
|      E +..      |
|     o * o.      |
|   ...+ +..      |
|    oooo++       |
+----[SHA256]-----+
```

6. open .ssh/id_rsa.pub on notepad, copy the full content and put it on gitlab web browser ssh key section and add i.
7. do git clone

```
C:\Users\sathi\Gitlab>git clone git@192.168.1.24:mainframe/zansible.git
Cloning into 'zansible'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

C:\Users\sathi\Gitlab>dir
 Volume in drive C is OS
 Volume Serial Number is 7C46-8E7B

 Directory of C:\Users\sathi\Gitlab

16-11-2021  20:37    <DIR>          .
16-11-2021  18:32    <DIR>          ..
10-09-2021  14:39    <DIR>          imsansible
16-11-2021  20:37    <DIR>          zansible
04-09-2021  15:28    <DIR>          zansible.old
04-09-2021  18:45    <DIR>          zansible.old1
04-09-2021  11:07           188,438 zansible.zip
               1 File(s)        188,438 bytes
               6 Dir(s)  764,654,637,056 bytes free

C:\Users\sathi\Gitlab>
```
8. copied our old zansible files from old directory to newly created zansible
9. cd into zansible directory  and then type
a. git add .
b. git commit -m "intial commit"
c. git push
d. refresh and verify on your gitlab zansible project all the fixes are available.

```

C:\Users\sathi\Gitlab\zansible>git commit -m "initial commit"
[main 7f9f1c1] initial commit
 29 files changed, 1705 insertions(+), 1 deletion(-)


C:\Users\sathi\Gitlab\zansible>git push
Enumerating objects: 39, done.
Counting objects: 100% (39/39), done.
Delta compression using up to 16 threads
Compressing objects: 100% (33/33), done.
Writing objects: 100% (37/37), 21.77 KiB | 2.72 MiB/s, done.
Total 37 (delta 6), reused 0 (delta 0), pack-reused 0
To 192.168.1.24:mainframe/zansible.git
   5938b37..7f9f1c1  main -> main
```
## Rundeck Ansible Integration

1. from sathya logon : sudo chsh -s /bin/bash rundeck
2. change password of rundeck
3. exit and  Login as rundeck pwd as gitlab
4. ssh-keygen
rundeck@gitlab:~$ ssh-keygen


5. ssh-copy-id sysprg1@192.168.1.44

```
rundeck@gitlab:~$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/var/lib/rundeck/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /var/lib/rundeck/.ssh/id_rsa
Your public key has been saved in /var/lib/rundeck/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:TemVbLvGFlN22uNoJkci15ZxJ5dniLMCqYjaxZvYa34 rundeck@gitlab
The key's randomart image is:
+---[RSA 3072]----+
|                 |
|         . o o ..|
|        o o B.=o*|
|   o . . = o.*+Bo|
|  . + . S.+o==...|
| o + o    oo++o .|
|. o +      .== . |
|    ..E    o=    |
|   oo.           |
+----[SHA256]-----+
rundeck@gitlab:~$ ssh-copy-id sysprg1@192.168.1.44
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/var/lib/rundeck/.ssh/id_rsa.pub"
The authenticity of host '192.168.1.44 (192.168.1.44)' can't be established.
ECDSA key fingerprint is SHA256:/hRt6nIQt3uibLOhjtxVfKANn8W5AG/SPJ5q79mi9MA.
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys

**********************************************************
ALERT! ALERT! ALERT! ALERT! ALERT! ALERT! ALERT! ALERT!
**********************************************************
You are entering into a ATOS Secured Area!
Your IP, Login Time,  Username has been noted and
as been sent to the server administrator!
This service is restricted to authorized users only.
All activities on this system are logged.
**********************************************************
sysprg1@192.168.1.44's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'sysprg1@192.168.1.44'"
and check to make sure that only the key(s) you wanted were added.

rundeck@gitlab:~$

```
for sysprg1 ssh didn' work, since some other configuration was done. create new userid sathya

```
rundeck@gitlab:~$ ssh-copy-id sathya@192.168.1.44
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/var/lib/rundeck/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
**********************************************************
ALERT! ALERT! ALERT! ALERT! ALERT! ALERT! ALERT! ALERT!
**********************************************************
You are entering into a ATOS Secured Area!
Your IP, Login Time,  Username has been noted and
as been sent to the server administrator!
This service is restricted to authorized users only.
All activities on this system are logged.
**********************************************************
sathya@192.168.1.44's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'sathya@192.168.1.44'"
and check to make sure that only the key(s) you wanted were added.

rundeck@gitlab:~$ ssh sathya@192.168.1.44
**********************************************************
ALERT! ALERT! ALERT! ALERT! ALERT! ALERT! ALERT! ALERT!
**********************************************************
You are entering into a ATOS Secured Area!
Your IP, Login Time,  Username has been noted and
as been sent to the server administrator!
This service is restricted to authorized users only.
All activities on this system are logged.
**********************************************************
$ ls -la
total 50
drwxr-xr-x   3 SATHYA   1           8192 Nov 16 16:35 .
drwxr-xr-x   5 0        1           8192 Nov 16 16:29 ..
-rw-------   1 SATHYA   1              9 Nov 16 16:35 .sh_history
drwx------   2 SATHYA   1           8192 Nov 16 16:34 .ssh
$

```

update zos userid .profile with below details.

export PYTHON_HOME=/usr/lpp/IBM/cyp/v3r8/pyz                                
export PATH=$PATH:$PYTHON_HOME/bin                                          
export LIBPATH=$LIBPATH:$PYTHON_HOME/lib                                    
# ZOAU REQUIREMENTS                                                         
export _BPXK_AUTOCVT=ON                                                     
export ZOAU_HOME=/usr/lpp/IBM/zoautil                                       
export PATH=${ZOAU_HOME}/bin:$PATH                                          
# ZOAU MAN PAGE REQS (OPTIONAL)                                             
export MANPATH=${ZOAU_HOME}/docs/%L:$MANPATH                                
# ZOAU JAVA REQS (OPTIONAL)                                                 
export JAVA_HOME=/usr/lpp/java/J8.0_64 # Root directory for Java 64-bit     
export CLASSPATH=${ZOAU_HOME}/lib:${CLASSPATH}                              
# ZOAU PYTHON REQS (OPTIONAL)                                               
export ZOAU_HOME=/usr/lpp/IBM/zoautil                                       
export PATH=${ZOAU_HOME}/bin:$PATH                                          
export LIBPATH=${ZOAU_HOME}/lib:${LIBPATH}                                  


issue pcon -r to verify



rundeck@gitlab:~$ cat /var/lib/rundeck/.ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDCJ2Vr9dmwML0EjF9Kc6d2kYyzLlgK1uWsaxJTXuDTNnKhBVempC8VduUIQaCoycVOzD6BHljMWwyhSwGAwKnzokVRJTPaFMl45HrLkG1zBVyuL+TWHUnSUyMpPcFGT+zicHXWTHoH5Kr6CTfi2UsTEJFlv5B97SxRwoYCDctVI0m0vdaK9w/oDYI+Zk790JUDL3O7lIYehSV2O6RaebC76sTg7aPHSrBjJSNWpVpfnr3NthnpWQ3CEiV0o4BoQQeWtLMe9nrEvONJkzQgNWcoP2IoePUQ8wD3WyOQFuopmNbkOcuny3lvJJUtEBdWW4085P0zTggWrcW9msjzUxl3eAaCHU335fn7qxmhgam3i90YAXHd9WVk+wcF/MclI+iBUsWkqX0BvEcwRI99vQi58ZgrHRuZZmvd/uE1ai5aeqm/WiXCpCOZaCrSkF8N749lckmHa3Qa+zxtM86+F9IXX2GdUFZywJMm1pBC+ruaFm6FmWWIzKpt4h3d3fyLmNU= rundeck@gitlab
rundeck@gitlab:~$


add above key on gitlab ssh addkeys.

rundeck@gitlab:~$ git clone git@192.168.1.24:mainframe/zansible.git
Cloning into 'zansible'...
remote: Enumerating objects: 40, done.
remote: Counting objects: 100% (40/40), done.
remote: Compressing objects: 100% (34/34), done.
remote: Total 40 (delta 6), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (40/40), 21.96 KiB | 21.96 MiB/s, done.
Resolving deltas: 100% (6/6), done.
rundeck@gitlab:~$

```
rundeck@gitlab:~/zansible$ git pull
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 285 bytes | 285.00 KiB/s, done.
From 192.168.1.24:mainframe/zansible
   3e63610..fc3fe57  main       -> origin/main
Updating 3e63610..fc3fe57
Fast-forward
 inventory.yml | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
rundeck@gitlab:~/zansible$ ansible-playbook -i inventory.yml console_command.yaml

PLAY [zos_host] **********************************************************************************************************************

TASK [Execute an operator command to show active jobs] *******************************************************************************
changed: [zos_host]

TASK [Response for Console Command] **************************************************************************************************
ok: [zos_host] => {
    "msg": {
        "changed": true,
        "content": [
            "DCUF      2021320  16:32:21.81             ISF031I CONSOLE SATHYA ACTIVATED",
            "DCUF      2021320  16:32:21.81            -D IPLINFO",
            "DCUF      2021320  16:32:21.84             IEE254I  16.32.21 IPLINFO DISPLAY 026",
            "                                            SYSTEM IPLED AT 14.14.17 ON 11/16/2021",
            "                                            RELEASE z/OS 02.04.00    LICENSE = z/OS",
            "                                            USED LOAD25 IN SYS1.IPLPARM ON 02027",
            "                                            ARCHLVL = 2   MTLSHARE = N",
            "                                            IEASYM LIST = (99,L)",
            "                                            IEASYS LIST = (DF) (OP)",
            "                                            IODF DEVICE: ORIGINAL(02027) CURRENT(02027)",
            "                                            IPL DEVICE: ORIGINAL(02011) CURRENT(02011) VOLUME(X24RA1)",
            "",
            "",
            "Ran 5 \"D IPLINFO\" QUIET NOWAIT"
        ],
        "failed": false,
        "rc": 0
    }
}

PLAY RECAP ***************************************************************************************************************************
zos_host                   : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

rundeck@gitlab:~/zansible$
```

## rundeck webpage customization
1. open project settings
then select everything on User Interface
then from default node executor drop down change ssh to ansible adhoc node executor and executable as /bin/bash

2. click on Jobs and create a job
click workflow and scrip inline executor and add the copied
```
cd /var/lib/rundeck/zansible

if /usr/bin/git pull git@192.168.2.195:mainframe/zansible.git; then
    echo "Git Pull Successful"
else
    echo "Git Pull Failed"
    exit 1
fi

ansible-playbook -i inventory.yml Cancel_User.yaml -e "arg1=$1 arg2=$2"
```
Arugments as 
```
${option.System} ${option.User}
```

3. click on webhook
give name canceluserhook
and give user as administrator
then click no Handler configuration
Select the job as canceluser

options -System ${data.System}  -User ${data.User}


4. go to node-red  
http://127.0.0.1:1880/#flow/b0b9109d78837be3

drag and put inject , http request and debug node on single line

on inject/timestap, edit and name as serivce now and msg.payload as JSON and paste below 
{
    "System": "zos1",
    "User": "IBMUSER"
}

on the http-request icon edit method as POST and paste the http put rundeck webhook postURL and return Parsed JSON objects

5. on gitlab inventory changed zos_hosts to zos1
and created zos1.yml on host__vars directory on gitlab








