# ZOWE Enablement

## ZOWE Convenience Install

1. ZFS Setup

```jcl
//$01CZFS  JOB 0,REGION=0M,CLASS=A,MSGCLASS=A,NOTIFY=&SYSUID       
//CREATE   EXEC PGM=IDCAMS                                         
//SYSPRINT DD SYSOUT=*                                             
//SYSIN    DD *                                                    
  DEFINE CLUSTER ( -                                               
         NAME(ZWE100.ZOWE.V1240.INSTALL.ZFS) -                     
         TRK(28725 30) -                                           
         LINEAR -                                                  
         SHAREOPTIONS(3) -                                         
         )                                                         
//*                                                                
//         SET ZFSDSN='ZWE100.ZOWE.V1240.INSTALL.ZFS'              
//FORMAT   EXEC PGM=IOEAGFMT,COND=(0,LT),                          
//            PARM='-aggregate &ZFSDSN -compat'                    
//SYSPRINT DD SYSOUT=*                                             
//*                                                                
//MOUNT    EXEC PGM=IKJEFT01,COND=(0,LT)                           
//SYSEXEC  DD DISP=SHR,DSN=SYS1.SBPXEXEC                           
//SYSTSPRT DD SYSOUT=*                                             
//SYSTSIN  DD *                                     
  PROFILE MSGID WTPMSG                              
  oshell umask 0022; +                              
    mkdir -p /var/zowe                              
  MOUNT +                                           
    FILESYSTEM('ZWE100.ZOWE.V1240.INSTALL.ZFS') +   
    MOUNTPOINT('/var/zowe') +                       
    MODE(RDWR) TYPE(ZFS) PARM('AGGRGROW')           
//* 
```
2. Unpax
```jcl
//$02UNPAX JOB 0,REGION=0M,CLASS=A,MSGCLASS=A,NOTIFY=&SYSUID 
//UNPAX    EXEC PGM=IKJEFT01                                 
//SYSEXEC  DD DISP=SHR,DSN=SYS1.SBPXEXEC                     
//SYSTSPRT DD SYSOUT=*                                       
//SYSTSIN  DD *                                              
  PROFILE MSGID WTPMSG                                       
  oshell cd /var/zowe; +                                     
    pax -ppx -rf zowe-1.24.0.pax                             
/*
```
3. Runtime 
```jcl
//$03RUNTM JOB 0,REGION=0M,CLASS=A,MSGCLASS=A,NOTIFY=&SYSUID         
//RUNTIME  EXEC PGM=IKJEFT01                                         
//SYSEXEC  DD DISP=SHR,DSN=SYS1.SBPXEXEC                             
//SYSTSPRT DD SYSOUT=*                                               
//SYSTSIN  DD *                                                      
  PROFILE MSGID WTPMSG                                               
  oshell export +                                                    
   NODE_HOME=/usr/lpp/IBM/cnj/v12r0/IBM/node-v12.16.1-os390-s390x; + 
   cd /var/zowe/zowe-1.24.0/install; +                               
   ./zowe-install.sh -i /var/zowe/runtime -h ZWE100.V1240 -l +       
    /var/zowe/logs                                                   
//*
```
4. Certificates
```jcl
//$04CERTF JOB 0,REGION=64M,CLASS=A,MSGCLASS=A,NOTIFY=&SYSUID 
//RUNTIME  EXEC PGM=IKJEFT01,REGION=0M,COND=(0,LT)            
//SYSEXEC  DD DISP=SHR,DSN=SYS1.SBPXEXEC                      
//SYSTSPRT DD SYSOUT=*                                        
//SYSTSIN  DD *                                               
  PROFILE MSGID WTPMSG                                        
  oshell export ZOWE_ZOSMF_PORT=10443; +                      
   cd /var/zowe/runtime/bin; +                                
   ./zowe-setup-certificates.sh -p +                          
    /var/zowe/runtime/bin/zowe-setup-certificates.env         
//*   
```
5. Instance
```jcl
//$05INSTN JOB 0,REGION=64M,CLASS=A,MSGCLASS=A,NOTIFY=&SYSUID        
//RUNTIME  EXEC PGM=IKJEFT01,REGION=0M,COND=(0,LT)                   
//SYSEXEC  DD DISP=SHR,DSN=SYS1.SBPXEXEC                             
//SYSTSPRT DD SYSOUT=*                                               
//SYSTSIN  DD *                                                      
  PROFILE MSGID WTPMSG                                               
  oshell export +                                                    
   NODE_HOME=/usr/lpp/IBM/cnj/v12r0/IBM/node-v12.16.1-os390-s390x; + 
   export ZOWE_ZOSMF_PORT=10443; +                                   
   cd /var/zowe/runtime/bin; +                                       
   ./zowe-configure-instance.sh -c /apps/zowe/v1240                  
//*  
```

## zOSMF Certificates

```jcl
//********************************************************************  
//*                                                                  *  
//* This job must be run using a user ID that has the RACF SPECIAL   *  
//* attribute.                                                       *  
//*                                                                  *  
//* This job assumes that the BPX.NEXT.USER profile has been         *  
//* defined in the FACILITY class to enable the use of AUTOUID       *  
//* and AUTOGID.  See the topic "Automatically assigning unique      *  
//* IDs through UNIX services" in z/OS Security Server RACF          *  
//* Security Administrator's Guide for additional information        *  
//* about automatic UID and GID assignment.  If this function has    *  
//* not been enabled, you must assign unique UIDs to the IZUSVR      *  
//* and IZUGUEST user IDs, and unique GIDs to the groups             *  
//* IZUADMIN, IZUSECAD, IZUUSER, and IZUUNGRP.                       *  
//*                                                                  *  
//********************************************************************  
//*                                                                    
//* This step sets up z/OSMF core security settings.                   
//*                                                                    
//STEP1  EXEC PGM=IKJEFT01                                             
//SYSPRINT DD SYSOUT=*                                                 
//SYSTSPRT DD SYSOUT=*                                                 
//SYSTSIN  DD *                                                        
                                                                       
 /* Create the CA certificate for the z/OSMF server                */  
 RACDCERT CERTAUTH GENCERT +                                           
   SUBJECTSDN(CN('z/OSMF CertAuth for Security Domain') +              
   OU('IZUDFLT')) WITHLABEL('zOSMFCA')  +                              
   TRUST NOTAFTER(DATE(2025/05/17))                                    
 RACDCERT ADDRING(IZUKeyring.IZUDFLT) ID(IZUSVR)                       
                                                                       
 /* Create the server certificate for the z/OSMF server            */  
 /* Change HOST NAME in CN field into real local host name         */  
 /* Usually the format of the host name is 'XXXX.XXX.XXX.XXX'      */  
 RACDCERT ID( IZUSVR ) GENCERT SUBJECTSDN(CN('S0W1.EMUFRAMEZOS.COM') + 
   O('IBM') OU('IZUDFLT')) WITHLABEL('DefaultzOSMFCert.IZUDFLT'), +    
   SIGNWITH(CERTAUTH LABEL('zOSMFCA')) NOTAFTER(DATE(2025/05/17))      
 RACDCERT ALTER(LABEL('DefaultzOSMFCert.IZUDFLT')) ID(IZUSVR) TRUST    
 RACDCERT ID( IZUSVR ) CONNECT (LABEL('DefaultzOSMFCert.IZUDFLT') +    
   RING(IZUKeyring.IZUDFLT) DEFAULT)                                   
 RACDCERT ID( IZUSVR ) CONNECT (LABEL('zOSMFCA') +                     
   RING(IZUKeyring.IZUDFLT) CERTAUTH)                                  
                                                                       
 SETROPTS RACLIST(DIGTCERT, DIGTRING) REFRESH                          
/*              
                   
```


## z/OS Tuning

1. Java tuning <https://zeeohhsss.wordpress.com/2020/04/23/turbo-java-in-adcd/>
2. LOAD99 -> IEASYS99
3. Add LFAREA=(1M=(15%,0%),NOPROMPT), in IEASYSDF and IPL.
```bash
IAR040I REAL STORAGE AMOUNTS: 105                                    
  TOTAL AVAILABLE ONLINE: 12G                                        
    LFAREA LIMIT FOR xM, xG, OR xT      : 7782M                      
    LFAREA LIMIT FOR SUM OF 1M= AND 2G= : 6553M                      
    LFAREA LIMIT FOR 2GB PAGES FOR 2G=  : 0 (NOT SUPPORTED)          
IAR048I LFAREA=(1M=(15%,0%),NOPROMPT) WAS PROCESSED WHICH RESULTED IN
1228 1MB PAGES AND 0 2GB PAGES.                                      
```
4. z/OSMF Global configuration Java overrides <https://emuframe.com/index.php/blog>
```jcl
    /global/zosmf/configuration/local_override.cfg                                          
******************************************************* Top of Data ************************
JVM_OPTIONS="-Dcom.ibm.ws.classloading.tcclLockWaitTimeMillis=300000\n-                     
Xshareclasses:cacheDir=/javasc/izusvr1,name=izusvr1cache\n-Xscmx150M\n-Xquickstart\n-Xms256m\n- 
Xmx512m\n-Xlp:objectheap:pagesize=1m,warn,pageable\n-Xlp:codecache:pagesize=1m,pageable"    



```
5. chmod 755 /global/zosmf/configuration/local_override.cfg
6. 

### Java Cacher


## ZOWE CLI

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

zowe  zos-jobs list jobs --zosmf-profile zNitro  (zowe profiles are case sensitive)

```
### Gitlab Ansible

zowe commandline scripts can be directly called from gitlab-ci.yml
