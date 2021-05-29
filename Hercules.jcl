
Standardise the z/OS 2.4 Setup

//REFVTOC  JOB  CLASS=A,MSGLEVEL=(1,1),MSGCLASS=A,
//         NOTIFY=&SYSUID                         
//S1        EXEC  PGM=ICKDSF                      
//VOLDD     DD DISP=SHR,UNIT=3390,VOL=SER=X24DTD  
//SYSPRINT  DD    SYSOUT=A                        
//SYSIN     DD    *                               
 REFORMAT DDNAME(VOLDD) VERIFY(X24DTD) REFVTOC    
/*                                                

//INITVOL JOB (1234),'DRVUSER',CLASS=A,                                
// MSGLEVEL=(1,1),NOTIFY=&SYSUID,MSGCLASS=A                            
//* INITIALIZE A VOLUME                                                
//STEP1 EXEC PGM=ICKDSF                                                
//SYSPRINT DD SYSOUT=*                                                 
//SYSIN DD *                                                           
  INIT UNITADDRESS(2034) VOLID(DFTMP0) DEVICETYPE(3390) NOVERIFY STGR -
  INDEX(15,0,045) VTOC(0,1,224) PURGE MAP NOCHECK NOVALIDATE NORECLAIM 


//IBMUSERA JOB REGION=0M,NOTIFY=&SYSUID
//ALCONTIG EXEC PGM=IEFBR14            
//RACFPRIM DD DSN=SYS1.RACF.PRIM,      
//      DISP=(NEW,CATLG,DELETE),       
//      UNIT=3390,                     
//      VOL=SER=X24DTD,                
//      DCB=(BLKSIZE=4096,RECFM=F,     
//      LRECL=4096,                    
//      DSORG=PS),                     
//      SPACE=(CYL,(47,0),,CONTIG)     
//RACFBACK DD DSN=SYS1.RACF.BACK,      
//      DISP=(NEW,CATLG,DELETE),       
//      UNIT=3390,                     
//      VOL=SER=X24DTD,                
//      DCB=(BLKSIZE=4096,RECFM=F,     
//      LRECL=4096,                    
//      DSORG=PS),                     
//      SPACE=(CYL,(47,0),,CONTIG)     


//IODFCP   JOB  CLASS=A,MSGLEVEL=(1,1),MSGCLASS=A,               
//         NOTIFY=&SYSUID                                        
//ALLOC    EXEC PGM=IDCAMS                                       
//SYSPRINT DD   SYSOUT=*                                         
//SYSIN    DD   *                                                
     DEFINE CLUSTER (NAME (SYS1.IODF25.CLUSTER) -                
                     LINEAR                     -                
                     RECORDS (1024)             -                
                     VOLUMES(X24DTD)            -                
                     )                          -                
            DATA (NAME (SYS1.IODF25))                            
//INIT1    EXEC PGM=CBDMGHCP,PARM='INITIODF SIZE=1024,ACTLOG=NO' 
//HCDCNTL  DD *                                                  
THIS IODF IS A COPY OF SYS1.IODF00                               
/*                                                               
//HCDIODFT DD   DSN=SYS1.IODF25,DISP=OLD                         
//HCDMLOG  DD   SYSOUT=*,DCB=(RECFM=FBA,LRECL=133,BLKSIZE=6650)  
//*                                                              
//COPY1    EXEC PGM=CBDMGHCP,PARM='COPYIODF'                     
//HCDIODFS DD   DSN=SYS1.IODF24,DISP=SHR                         
//HCDIODFT DD   DSN=SYS2.IODF25,DISP=OLD                         
//HCDMLOG  DD   SYSOUT=*,DCB=(RECFM=FBA,LRECL=133,BLKSIZE=6650)  

//IBMUSERA JOB REGION=0M,NOTIFY=&SYSUID                         
//DIAGNP1      EXEC PGM=IRRUT200                                
//SYSPRINT  DD SYSOUT=*                                         
//SYSRACF   DD DSN=SYS1.RACFP,                                  
//             DISP=OLD,                                        
//             UNIT=3390,                                       
//             VOL=SER=SYS1B1                                   
//SYSUT1    DD UNIT=3390,                                       
//             SPACE=(CYL,(100))                                
//SYSUT2    DD SYSOUT=*                                         
//SYSIN     DD *                                                
    INDEX                                                       
    MAP ALL                                                     
    END                                                         
//*                                                             
//COPYP2       EXEC PGM=IRRUT400,PARM='LOCKINPUT,FREESPACE(20)' 
//SYSPRINT  DD SYSOUT=*                                         
//INDD1     DD DSN=SYS1.RACFP,                                  
//             DISP=OLD,                                        
//             UNIT=3390,                                       
//             VOL=SER=SYS1B1                                   
//OUTDD1    DD DSN=SYS1.RACF.PRIM,                              
//             DISP=OLD                                         
//*                                                             
//UNLKP3       EXEC PGM=IRRUT400,PARM='UNLOCKINPUT'             
//SYSPRINT  DD SYSOUT=*                                         
//INDD1     DD DSN=SYS1.RACFP,                                  
//             DISP=OLD,                                        
//             UNIT=3390,                                       
//             VOL=SER=SYS1B1                                   
/*                                                              
//*                                                             
//DIAGNB4      EXEC PGM=IRRUT200                                
//SYSPRINT  DD SYSOUT=*                                         
//SYSRACF   DD DSN=SYS1.RACFB,                                  
//             DISP=OLD,                                        
//             UNIT=3390,                                       
//             VOL=SER=SYS1B1                                   
//SYSUT1    DD UNIT=3390,                                       
//             SPACE=(CYL,(100))                                
//SYSUT2    DD SYSOUT=*                                         
//SYSIN     DD *                                                
    INDEX                                                       
    MAP ALL                                                     
    END                                                         
//*                                                             
//COPYB5       EXEC PGM=IRRUT400,PARM='LOCKINPUT,FREESPACE(20)' 
//SYSPRINT  DD SYSOUT=*                                         
//INDD1     DD DSN=SYS1.RACFB,                                  
//             DISP=OLD,                                        
//             UNIT=3390,                                       
//             VOL=SER=SYS1B1                                   
//OUTDD1    DD DSN=SYS1.RACF.BACK,                              
//             DISP=OLD                                         
//*                                                             
//UNLKB6       EXEC PGM=IRRUT400,PARM='UNLOCKINPUT'             
//SYSPRINT  DD SYSOUT=*                                         
//INDD1     DD DSN=SYS1.RACFB,                                  
//             DISP=OLD,                                        
//             UNIT=3390,                                       
//             VOL=SER=SYS1B1                                   
/*                                                              

  SYS1.PARMLIB(IRRPRMDF) - 01.03     
==>                                  
                                     
DATASETNAMETABLE                     
                                     
  /* Entry 1 - First data set pair   
  ENTRY                              
    PRIMARYDSN(SYS1.RACF.PRIM)       
    BACKUPDSN(SYS1.RACF.BACK)        
    UPDATEBACKUP(NOSTATS)            
    BUFFERS(255)                     

