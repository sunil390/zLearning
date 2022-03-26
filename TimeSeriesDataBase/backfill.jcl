//BACKFILJ  JOB REGION=0M,CLASS=S,MSGCLASS=X,        
//            MSGLEVEL=(1,1),NOTIFY=&SYSUID          
//EXAMPLE  EXEC PGM=IKJEFT01,REGION=4096K,DYNAMNBR=30
//SYSPRINT DD  SYSOUT=*                              
//SYSEXEC  DD  DISP=SHR,DSN=IBMUSER.JCLS             
//SYSTSPRT DD  SYSOUT=*                              
//SYSTSIN  DD  *                                     
  VMLOADER                                           
