
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

# Data Store.


# Machine Learning.
