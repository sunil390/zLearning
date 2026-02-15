#

## IMS SHMSG full issue

```jcl
000001 //SHMSGJ   JOB ACTINFO1,'PGMRNAME',CLASS=A,MSGCLASS=H,MSGLEVEL=(1,1),   JOB03820                             
000002 // NOTIFY=IBMUSER,REGION=0M                                             00002000                             
000003 //ALLOC    EXEC PGM=IEFBR14                                             00003100                             
000004 //SYSPRINT DD SYSOUT=*                                                  00003200                             
000005 //SYSUT1   DD DISP=SHR,DSN=IMS15.SHMSG.OLD                              00003300                             
000006 //SYSUT2   DD DISP=(NEW,CATLG,DELETE),DSN=IMS15.SHMSG,                  00003400                             
000007 // LIKE=IMS15.SHMSG.OLD,                                                00003500                             
000008 // UNIT=SYSALLDA,VOL=SER=USRVS1,                                        00003600                             
000009 // SPACE=(CYL,(20,0))                                                   00003700                             
000010 //SYSIN DD DUMMY                                                        00003800
```

1. R xx,/NRE FORMAT ALL BUILDQ.    

## CICS COnfig

```shell
//DELDEF   EXEC PGM=IXCMIAPU
//SYSPRINT DD   SYSOUT=*                   
//SYSABEND DD   SYSOUT=*                   
//SYSIN    DD   *
DATA TYPE(LOGR) REPORT(NO)  
DELETE LOGSTREAM NAME(CICSUSER.CICSTS61.DFHLOG)
DEFINE                                               
   LOGSTREAM                                         
   NAME(CICSUSER.CICSTS61.DFHLOG)                    
   HLQ(IXGLOGR)                                      
   MODEL(NO)                                         
   LS_SIZE(0)                                        
   STG_SIZE(3000)                                    
   LOWOFFLOAD(40)                                    
   HIGHOFFLOAD(80)                                   
   RETPD(0)                                          
   AUTODELETE(NO)                                    
   OFFLOADRECALL(YES)                                
   DASDONLY(YES)                                     
   DIAG(NO)                                          
   MAXBUFSIZE(64000)                                 
DELETE LOGSTREAM NAME(CICSUSER.CICSTS61.DFHSHUNT)    
DEFINE                                               
   LOGSTREAM                                         
   NAME(CICSUSER.CICSTS61.DFHSHUNT)                  
   HLQ(IXGLOGR)                                      
   MODEL(NO)                                         
   LS_SIZE(0)                                        
   STG_SIZE(500)                                     
   LOWOFFLOAD(40)                                    
   HIGHOFFLOAD(80)                                   
   RETPD(0)                                          
   AUTODELETE(NO)                                    
   OFFLOADRECALL(YES)                                
   DASDONLY(YES)                                     
   DIAG(NO)                                          
   MAXBUFSIZE(64000)    
DEFINE                                        
   LOGSTREAM                                  
   NAME(VS01.DFHLOG.MODEL)                    
   HLQ(IXGLOGR)                               
   MODEL(YES)                                 
   LS_SIZE(0)                                 
   STG_SIZE(3000)                             
   LOWOFFLOAD(40)                             
   HIGHOFFLOAD(80)                            
   RETPD(0)                                   
   AUTODELETE(NO)                             
   OFFLOADRECALL(YES)                         
   DASDONLY(YES)                              
   DIAG(NO)                                   
   MAXBUFSIZE(64000)                          
DELETE LOGSTREAM NAME(VS01.DFHSHUNT.MODEL)    
DEFINE                                        
   LOGSTREAM                                  
   NAME(VS01.DFHSHUNT.MODEL)                  
   HLQ(IXGLOGR)                               
   MODEL(YES)                                 
   LS_SIZE(0)                                 
   STG_SIZE(500)                              
   LOWOFFLOAD(40)                             
   HIGHOFFLOAD(80)                            
   RETPD(0)                                   
   AUTODELETE(NO)                             
   OFFLOADRECALL(YES)                         
   DASDONLY(YES)                              
   DIAG(NO)                                   
   MAXBUFSIZE(64000)  
               

```


# Startup

```shell
S CSFDF
S SSHD
F RMF,START III
S GPMSERVE
S CFZCIM
S IZUANG1
S IZUSVR1
```

