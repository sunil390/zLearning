#

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

