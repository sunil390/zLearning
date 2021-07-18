
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