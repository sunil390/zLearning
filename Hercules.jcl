
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

--------------------------

SMS Changes

D SMS                                                 
IGD002I 16:47:59 DISPLAY SMS 902                      
SCDS = ACSVS.DFSMS.SCDS                               
ACDS = ACSVS.DFSMS.ACDS                               
COMMDS = ACSVS.DFSMS.COMMDS                           
ACDS LEVEL = z/OS V2.4                                
DINTERVAL = 150                                       
REVERIFY = NO                                         
ACSDEFAULTS = NO                                      
    SYSTEM     CONFIGURATION LEVEL    INTERVAL SECONDS
    DCUF       2021/05/29 16:47:48           15       

ACSNS.DFSMS.DCUF.ACS

sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
    ACSNS.DFSMS.DCUF.ACS(MGMTCLAS) - 01.09                  Columns 000
 ===>                                                          Scroll =
********************************* Top of Data *************************
PROC 1 MGMTCLAS                                                        
/*-------------------------------------------------------------------*/
/*                  M A N A G E M E N T   C L A S S                  */
/*                  ===============================                  */
/*                                                                   */
/*  DATE   RESP  DESCRIPTION OF CHANGE                       REQUEST */
/* ------  ----  ---------------------                       ------- */
/*                                                                   */
/*-------------------------------------------------------------------*/
/*                                                                   */
                                                                       
SELECT                                                                 
                                                                       
/*===================================================================*/
/* STORAGE GROUP FOR TSO DATASETS                                    */
/*-------------------------------------------------------------------*/
                                                                       
    WHEN (&STORCLAS EQ 'TSO') DO                                       
      WRITE ' TSO MGMTCLASS ASSIGNED'                                  
      SET &MGMTCLAS = 'TSO'                                            
      EXIT CODE(0)                                                     
      END                                                              
                                                                       
/*===================================================================*/
/* TEMPORARY FILES                                                   */
/*-------------------------------------------------------------------*/
                                                                       
    WHEN (&STORCLAS EQ 'TMPORARY') DO                                  
      WRITE ' TEMPORARY MGMTCLASS'                                     
      SET &MGMTCLAS = 'TMPORARY'                                       
      EXIT CODE(0)                                                     
      END                                                              
                                                                       
                                                                       
/*===================================================================*/
/* DEFAULT TO STRG MC                                                */
/*-------------------------------------------------------------------*/
   OTHERWISE                   
      DO                       
         SET &MGMTCLAS EQ ''   
         EXIT CODE(0)          
      END                      
   END                         
END                            

sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
    ACSNS.DFSMS.DCUF.ACS(DATACLAS) - 01.00                Member DATACL
 ===>                                                          Scroll =
********************************* Top of Data *************************
PROC 1 DATACLAS                                                        
/*-------------------------------------------------------------------*/
/*                      D A T A   C L A S S                          */
/*                      ===================                          */
/*    SELECTION ROUTINE FOR NEW DATA SET ALLOCATIONS                 */
/*                                                                   */
/* MMDDYY  RESP  DESCRIPTION OF CHANGE                        REQUEST*/
/* ------  ----  ------------------------------------------- ------- */
                                                                       
FILTLIST VALIDDASD INCLUDE('DASD','DISK','PROD','SYSALLDA','SYSDA',    
                           'SYSSQ','TEST','TSO','3380','3390')         
                                                                       
SELECT                                                                 
                                                                       
/*===================================================================*/
/*  DEFAULT TO NULL                                                  */
/*-------------------------------------------------------------------*/
                                                                       
    WHEN (&UNIT = &VALIDDASD)                                          
      SET &DATACLAS = 'DEFAULT'                                        
     OTHERWISE                                                         
      SET &DATACLAS = ''                                               
                                                                       
END                                                                    
END                                                                    


    ACSNS.DFSMS.DCUF.ACS(STORCLAS) - 01.26                  Columns 000
 ===>                                                          Scroll =
********************************* Top of Data *************************
PROC 1 STORCLAS                                                        
/*-------------------------------------------------------------------*/
/*                  S T O R A G E   C L A S S                        */
/*                  =========================                        */
/*    SELECTION ROUTINE FOR NEW DATA SET ALLOCATIONS                 */
/*                                                                   */
/*  DATE   RESP  DESCRIPTION OF CHANGE                       REQUEST */
/* ------  ----  ------------------------------------------- ------- */
/*-------------------------------------------------------------------*/
/*                                                                   */
                                                                       
FILTLIST TSO     INCLUDE(SYS*.ISPF.**,                                 
                         SYS*.LOG.MISC.**,                             
                         SYS*.SPFLOG%.**,                              
                         SYS*.SPFTEMP%.**,                             
                         SYS*.SRCHFOR.**,                              
                         SYS*.HCD.MSGLOG,                              
                         SYS*.HCD.TERM,                                
                         SYS*.HCD.TRACE,                               
                         SYS*.CLIST,                                   
                         SYS*.**.CNTL*.**,                             
                         SYS*.DITPROF.**,                              
                         SYS*.LIST*.**,                                
                         SYS*.SUPERC.**,                               
                         SYS.SPF*.**,                                  
                 EXCLUDE(ACS%S.**,AUSNP.**,SYS1.**,SYS2.**)            
                                                                       
FILTLIST SDT     INCLUDE('SYS055','SYS195','SYS279','SYS307','SYS361') 
                                                                       
SELECT                                                                 
                                                                       
                                                                       
/*********************************************************************/
/* HANDLE SDT IDS FOR SYSTEM CONFIGURATIONS                          */
/*********************************************************************/
   WHEN ( &USER EQ &SDT )                                              
      DO                                                               
         SET &STORCLAS EQ ''                                            
         EXIT CODE(0)                                                   
      END                                                               
                                                                        
                                                                        
/*===================================================================*/ 
/* TSO DATASET ALLOCATION                                            */ 
/*-------------------------------------------------------------------*/ 
    WHEN (&HLQ EQ &USER) DO                                             
      WRITE ' TSO STORCLAS ASSIGNED'                                    
      SET &STORCLAS = 'TSO'                                             
      EXIT CODE(0)                                                      
      END                                                               
                                                                        
    WHEN (&DSN EQ &TSO) DO                                              
      WRITE ' TSO STORCLAS ASSIGNED'                                    
      SET &STORCLAS = 'TSO'                                             
      EXIT CODE(0)                                                      
      END                                                               
                                                                        
                                                                        
/*===================================================================*/ 
/* TEMPORARY DATASET ALLOCATION                                      */ 
/*-------------------------------------------------------------------*/ 
                                                                        
    WHEN (&DSTYPE EQ 'TEMP') DO                                         
      WRITE ' TEMPORARY DATASET'                                        
      SET &STORCLAS = 'TMPORARY'                                        
      EXIT CODE(0)                                                      
      END                                                               
                                                                        
                                                                        
/*===================================================================*/ 
/* DEFAULT TO NULL SC                                                */ 
/*-------------------------------------------------------------------*/ 
   OTHERWISE                                                            
      DO                                                                
         SET &STORCLAS EQ ''    
         EXIT CODE(0)           
      END                       
   END                          
END                             


    ACSNS.DFSMS.DCUF.ACS(STORGRP) - 01.11                   Columns 000
 ===>                                                          Scroll =
********************************* Top of Data *************************
PROC &STORGRP                                                          
/*-------------------------------------------------------------------*/
/*                  S T O R A G E   G R O U P                        */
/*                  =========================                        */
/*    SELECTION ROUTINE FOR NEW DATA SET ALLOCATIONS                 */
/*                                                                   */
/*                  S T O R A G E   G R O U P                        */
/*                  =========================                        */
/*  DATE   RESP  DESCRIPTION OF CHANGE                      REQUEST  */
/* ------  ----  ------------------------------------------ -------- */
/*-------------------------------------------------------------------*/
                                                                       
SELECT                                                                 
                                                                       
/*===================================================================*/
/* STORAGE GROUP ALLOCATION FOR TSO DATASETS                         */
/*-------------------------------------------------------------------*/
                                                                       
    WHEN (&STORCLAS EQ 'TSO') DO                                       
      WRITE ' TSO STORGROUP ASSIGNED'                                  
      SET &STORGRP  = 'TSO'                                            
      EXIT CODE(0)                                                     
      END                                                              
                                                                       
/*===================================================================*/
/* STORAGE GROUP ALLOCATION FOR TEMPORARY DATASETS                   */
/*-------------------------------------------------------------------*/
                                                                       
    WHEN (&STORCLAS EQ 'TMPORARY') DO                                  
      WRITE ' TEMPORARY DATASETS'                                      
      SET &STORGRP  = 'TMPORARY'                                       
      EXIT CODE(0)                                                     
      END                                                              
                                                                       
/*===================================================================*/
/* DEFAULT TO STRG SG                                                */
/*-------------------------------------------------------------------*/
    OTHERWISE                  
         DO                    
       SET &STORGRP EQ 'DEFLT' 
       EXIT CODE(0)            
    END                        
 END                           
END                            



