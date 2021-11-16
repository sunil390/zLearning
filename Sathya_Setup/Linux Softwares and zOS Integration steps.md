# Linux Softwares and zOS Integration steps
## Verification
1. Make sure below softwares are running on Linux
a. gitlab
b. gitlab-runner
c. rundeck
d. psql
e. ansible
f. your zOS lpar is up and avilable
2. on zOS make sure SSH and CSF are running
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
