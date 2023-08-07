# UserMODs

## ZAP Usermod to add RSU Level 

1. [cvt mapping](https://www.ibm.com/docs/en/zos/2.4.0?topic=correlator-cvt-information)
2. [iplinfo](http://www.mzelden.com/mvsfiles/iplinfo.txt)
3. cvt mappings name display - rexx
```.py
/* REXX program to display the contents of the CVT Structure  */                 
cvt = c2d(Storage(10,4))                                                         
ecvt     = C2d(Storage(D2x(cvt + 140),4))  /* point to CVTECVT     */            
ecvtipa  = C2d(Storage(D2x(ecvt + 392),4)) /* point to IPA         */            
ipascat  = Storage(D2x(ecvtipa + 224),63)  /* SYSCAT  card image   */            
mcatdsn  = Strip(Substr(ipascat,11,44))    /* master catalog dsn   */            
mcatvol  = Substr(ipascat,1,6)             /* master catalog VOLSER*/            
prodname = Storage(D2x(CVT - 40),8)                                              
prodfmid = Storage(D2x(CVT - 32),8)                                              
cvtverid = Storage(D2x(CVT - 24),16)                                             
say 'z/OS CP =' prodname                                                         
say 'z/OS FMID =' prodfmid                                                       
say 'z/OS Cloning level =' cvtverid                                              
say 'z/OS mcat          =' mcatdsn                                               
say 'z/OS mcat volume   =' mcatvol                                               
Exit
```
4. UserMod to apply UserModification flags [xephone](https://www.cbttape.org/xephon/xephonm/mvs9908.pdf)

```jcl
//SYSPRG1A  JOB REGION=0M,CLASS=S,MSGCLASS=X,              
//            MSGLEVEL=(1,1),NOTIFY=&SYSUID                
//SMPE    EXEC PGM=GIMSMP,REGION=0M                        
//STEPLIB  DD DISP=SHR,DSN=SYS1.MIGLIB                     
//         DD DISP=SHR,DSN=SYS1.ASM.SASMMOD1               
//SMPCSI   DD DISP=SHR,DSN=SMPE.ZS24M27.R2012.GLOBAL.CSI   
//SMPPTS   DD DISP=SHR,DSN=SMPE.ZS24M27.R2012.X24PE1.SMPPTS
//SMPLOG   DD SYSOUT=*                                     
//SMPLOGA  DD SYSOUT=*                                     
//SMPLIST  DD SYSOUT=*                                     
//SMPOUT   DD SYSOUT=*                                     
//SMPRPT   DD SYSOUT=*                                     
//SYSPRINT DD SYSOUT=*                                     
//SMPWRK1  DD UNIT=SYSDA,SPACE=(CYL,(2,1,5)),              
//            DISP=(,DELETE),DCB=BLKSIZE=6160              
//SMPWRK2  DD UNIT=SYSDA,SPACE=(CYL,(2,1,5)),              
//            DISP=(,DELETE),DCB=BLKSIZE=6160              
//SMPWRK3  DD UNIT=SYSDA,SPACE=(CYL,(2,1,5)),              
//            DISP=(,DELETE),DCB=BLKSIZE=3120              
//SYSUT1   DD UNIT=SYSDA,SPACE=(CYL,(2,1))                 
//SYSUT2   DD UNIT=SYSDA,SPACE=(CYL,(2,1))                 
//SYSUT3   DD UNIT=SYSDA,SPACE=(CYL,(2,1))                 
//SYSUT4   DD UNIT=SYSDA,SPACE=(CYL,(2,1))                 
//SMPHOLD  DD DUMMY                                        
//SMPCNTL  DD *                                            
  SET BDY(MVST100) .                                       
    RESTORE S(UMOD001) .                                   
  RESETRC .                                                
  SET BOUNDARY(GLOBAL) .                                   
    REJECT S(UMOD001) BYPASS(APPLYCHECK) .                 
  RESETRC .                                                
  SET BOUNDARY(GLOBAL) .                                   
    RECEIVE S(UMOD001) .                                   
  SET BDY(MVST100) .                                       
    APPLY S(UMOD001) .                                     
    LIST SYSMOD(UMOD001) .                                 
//SMPPTFIN DD *        DATA,DLM=$$                         
++USERMOD (UMOD001) .                                      
++VER(Z038) FMID(HBB77C0) PRE(UJ02280) .           
++ZAP (IEAVCVT) DISTLIB(AOSC5) .                   
  NAME IEANUC01 IEAVCVT                            
  VER 28 4040404040404040                          
  REP 28 D4C4C3E4F2F3F8F1                          
  IDRDATA UMOD001                                  
//*                                                
//S EXEC PGM=AMASPZAP                              
//SYSLIB DD DSN=SYS1.NUCLEUS,DISP=SHR,UNIT=SYSDA   
//SYSPRINT DD SYSOUT=*                             
//SYSIN DD *                                       
  NAME IEANUC01 IEAVCVT                            
  DUMPT IEANUC01 IEAVCVT                           
/*
```

