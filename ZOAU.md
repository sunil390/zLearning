# September 2021

<https://www.ibm.com/docs/en/zoau/1.2.0?topic=installing-configuring-zoa-utilities#authorized-components>

Unmounted 1.1.3 filesystem and mounted a new filesystem for 1.2

```jcl
//ZOAU12J   JOB REGION=0M,CLASS=S,MSGCLASS=X,               
//            MSGLEVEL=(1,1),NOTIFY=&SYSUID                 
//ALLOCZ   EXEC PGM=IDCAMS                                  
//SYSPRINT DD SYSOUT=*                                      
//SYSIN    DD *                                             
   DEFINE CLUSTER(NAME(SYS1.OMVS.ZOAU12.X24OA1) -             
   LINEAR TRACKS(1600 10) SHAREOPTIONS(3) VOLUMES(X24OA1))  
//RCCHCK   IF ALLOCZ.RC=0 THEN                              
//FORMAT   EXEC PGM=IOEAGFMT,REGION=0M,                     
// PARM=('-aggregate SYS1.OMVS.ZOAU12.X24OA1 -compat')        
//SYSPRINT DD SYSOUT=*                                      
//MOUNT    EXEC PGM=IKJEFT01                                
//SYSTSPRT DD SYSOUT=*                                      
//SYSPRINT DD SYSOUT=*                                      
//SYSTSIN  DD *                                             
  MOUNT FILESYSTEM('SYS1.OMVS.ZOAU12.X24OA1') +               
     TYPE(ZFS) MODE(RDWR) PARM('AGGRGROW') +                
     MOUNTPOINT('/usr/lpp/IBM/zoautil')                     
```
```shell
ftp'ed the pax file to /usr/lpp/IBM/zoautil

from IBMUSER login
#cd /usr/lpp/IBM/zoautil
#pax -p e -rf zoau-1.2.0.pax

from SYSPRG1 login

$ pip3 install /usr/lpp/IBM/zoautil/zoautil_py-1.2.0.tar.gz                                                               
Defaulting to user installation because normal site-packages is not writeable                                             
Processing /usr/lpp/IBM/zoautil/zoautil_py-1.2.0.tar.gz                                                                   
Using legacy 'setup.py install' for zoautil-py, since package 'wheel' is not installed.                                   
Installing collected packages: zoautil-py                                                                                 
  Attempting uninstall: zoautil-py                                                                                        
    Found existing installation: zoautil-py 1.1.0                                                                         
    Uninstalling zoautil-py-1.1.0:                                                                                        
      Successfully uninstalled zoautil-py-1.1.0                                                                           
    Running setup.py install for zoautil-py ... -Ý?25ldone                                                                
-Ý?25hSuccessfully installed zoautil-py-1.2.0                                                                             
-Ý33mWARNING: You are using pip version 21.0.1; however, version 21.2.4 is available.                                     
You should consider upgrading via the '/usr/lpp/IBM/cyp/v3r8/pyz/bin/python3.8 -m pip install --upgrade pip' command.-Ý0m 
$ 

$ /usr/lpp/IBM/cyp/v3r8/pyz/bin/python3.8 -m pip install --upgrade pip                                                              
Defaulting to user installation because normal site-packages is not writeable                                                       
Requirement already satisfied: pip in /usr/lpp/IBM/cyp/v3r8/pyz/lib/python3.8/site-packages (21.0.1)                                
Collecting pip                                                                                                                      
  Downloading pip-21.2.4-py3-none-any.whl (1.6 MB)                                                                                  
-ÝK     |â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--| 1.5 MB 230 kB/s eta 0:00:
-ÝK     |â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--| 1.5 MB 230 kB/s eta 0:00:
-ÝK     |â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--| 1.5 MB 230 kB/s eta 0:00:
-ÝK     |â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--| 1.5 MB 230 kB/s eta 0:00:
-ÝK     |â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--â--| 1.6 MB 230 kB/s          
-Ý?25hInstalling collected packages: pip                                                                                            
-Ý33m  WARNING: The scripts pip, pip3 and pip3.8 are installed in '/home/SYSPRG1/.local/bin' which is not on PATH.                  
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.-Ý0m             
Successfully installed pip-21.2.4                                                                                                   
$                                                                                                                                   
```


# August 2021

```

https://www.ibm.com/docs/en/zoau/1.1.0?topic=installing-configuring-zoa-utilities


ls -E /usr/lpp/IBM/zoautil/bin/mvscmdauth

ZOA Utilities Python APIs

1. Environment variables

export ZOAU_HOME=/usr/lpp/IBM/zoautil
export PATH=${ZOAU_HOME}/bin:$PATH
export LIBPATH=${ZOAU_HOME}/lib:${LIBPATH}

2. Create a virtual environment by using the following command: This did not work! 

python3 -m venv env  --> Worked , Deleted the env folder.
source env/bin/activate  --> Not found ?

3. Set the .profile (Root file system must be in R/W mode else .profile will open in view mode)

    /home/SYSPRG1/.profile                                             
******************************************************* Top of Data ***
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
export CLASSPATH=${ZOAU_HOME}/lib/*:${CLASSPATH}                       
# ZOAU PYTHON REQS (OPTIONAL)                                          
export ZOAU_HOME=/usr/lpp/IBM/zoautil                                  
export PATH=${ZOAU_HOME}/bin:$PATH                                     
export LIBPATH=${ZOAU_HOME}/lib:${LIBPATH}                             

logout and login to set the .profile

SDSF Access.

RDEFINE SDSF *.*     UACC(NONE) OWNER(SYS1)           
PERMIT *.*     CLASS(SDSF) ID(SYSPRG1) ACCESS(READ)   
SETROPTS RACLIST(SDSF) REFRESH                        

ZOAU

pcon -r
opercmd "d a,l"
jls
ddls
pjdd
mls
dls

pip install jmespath


4. from home pip3 install /usr/lpp/IBM/zoautil/zoautil_py-1.1.0.tar.gz

failed for 3 Datasets, Created Aliases.

//IDCAMSJ JOB  CLASS=A,MSGCLASS=A,MSGLEVEL=(1,1), 
//        NOTIFY=&SYSUID                          
//STEP1    EXEC PGM=IDCAMS                        
//SYSPRINT DD SYSOUT=A                            
//SYSIN    DD *                                   
       DEFINE ALIAS                 -             
            (NAME(CEE.SCEEBND2)       -           
            RELATE(SYS1.CEE.SCEEBND2) ) -         
            CATALOG(SYS1.MCATZS24.DISTZOS)   
       DEFINE ALIAS                 -       
            (NAME(CBC.SCCNOBJ)        -     
            RELATE(SYS1.CBC.SCCNOBJ)  ) -   
            CATALOG(SYS1.MCATZS24.DISTZOS) 
       DEFINE ALIAS                 -      
            (NAME(CEE.SCEELIB)        -    
            RELATE(SYS1.CEE.SCEELIB)  ) -  
            CATALOG(SYS1.MCATZS24.DISTZOS)  

/*                                                

$ pip3 install /usr/lpp/IBM/zoautil/zoautil_py-1.1.0.tar.gz                                                          
Defaulting to user installation because normal site-packages is not writeable                                        
Processing /usr/lpp/IBM/zoautil/zoautil_py-1.1.0.tar.gz                                                              
Using legacy 'setup.py install' for zoautil-py, since package 'wheel' is not installed.                              
Installing collected packages: zoautil-py                                                                            
    Running setup.py install for zoautil-py ... -Ý?25ldone                                                           
-Ý?25hSuccessfully installed zoautil-py-1.1.0                                                                        
-Ý33mWARNING: You are using pip version 21.0.1; however, version 21.1.3 is available.                                
You should consider upgrading via the '/usr/lpp/IBM/cyp/v3r8/pyz/bin/python3.8 -m pip install --upgrade pip' command.

gitlab-runner@zgitlab:~/zansible$ ansible-playbook -i "znitro.hercules.com," host_setup.yaml -u sysprg1 -vvv

---------Replicating back to Repo------------
git add . "on all folders that have changed"
git commit -m "message"
git push -u origin main
---------------------------------------------





```

## ZOaU Samples 1.2 Announced

https://github.com/IBM/zoau.git

https://medium.com/theropod/the-journey-from-jcl-to-python-so-easy-even-an-old-mainframer-can-do-it-f088cc49366a

https://www.ibm.com/docs/en/zoau/1.2.0?topic=whats-new-noteworthy#version-1-2-0

