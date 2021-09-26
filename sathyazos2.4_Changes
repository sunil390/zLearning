added 2 volume IMS001.z and X24OA2.z
IMS001 contains IMS V15 datasets
X24OA2 contains MINICONDA OMVS Dataset which needs to be mounted on /usr/lpp/miniconda 

Added auto shutdown of lpar using CBT on IMS001 you can find XMI and REXX

Changed TELNET USSTAB 

Installed ZOWE and started STC. It takes more time than zOSMF to initilaize

# Setup

```jcl
//ZFSJOB   JOB REGION=0M,CLASS=S,MSGCLASS=X,       
//            MSGLEVEL=(1,1),NOTIFY=&SYSUID        
//MOUNT    EXEC PGM=IKJEFT1A                       
//SYSTSPRT DD   SYSOUT=*                           
//SYSTSIN  DD   *                                  
  BPXBATCH SH mkdir -p /usr/lpp/miniconda          
  BPXBATCH SH chmod -R 755 /usr/lpp/miniconda      
  MOUNT FILESYSTEM('SYS1.OMVS.CONDA.X24OA2.ZFS') - 
        MOUNTPOINT('/usr/lpp/miniconda') -         
        TYPE(ZFS)  MODE(RDWR) -                    
        PARM('AGGRGROW')                           
/*                                                 
```
