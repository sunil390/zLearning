# Input.

<https://www.ibm.com/docs/en/zos/2.4.0?topic=output-approaches-automation-health-checker-zos>

```jcl
//HZSPRINT JOB 'ACCOUNTING INFORMATION','HZSPRINT JOB',  
//         CLASS=A,MSGCLASS=A,MSGLEVEL=(1,1)             
//HZSPRINT EXEC PGM=HZSPRNT,TIME=1440,REGION=0M,
//    PARM=('CHECK(*,*)',      
//    'EXCEPTIONS') 
//SYSOUT   DD DSN=HCHECKER.PET.CHKEXCPT.SEQ.REPORT,DISP=MOD
```

RC 1202- sysout record length issue.

<https://www.ibm.com/docs/en/zos/2.4.0?topic=output-using-hzsprint-utility>

```jcl
//HZSPRINT JOB                                                      
//*...                                                              */ 
//HZSPRINT EXEC PGM=HZSPRNT,TIME=1440,REGION=0M,PARMDD=SYSIN       
//SYSIN DD *,DLM='@@'                                              
CHECK(*,*)                                                         
,EXCEPTIONS                                                        
@@                                                                 
//SYSOUT   DD SYSOUT=A,DCB=(LRECL=256)                     


1200 : XFACILIT is not RACListes

  RDEFINE XFACILIT HZS.* UACC(NONE) OWNER(SYS1)         
  PERMIT HZS.* CLASS(XFACILIT) ID(SYSPRG1) ACC(READ)    
  SETROPTS RACLIST(XFACILIT) REFRESH                     

```




# Data Store.


# Machine Learning.
