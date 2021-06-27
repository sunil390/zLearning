

Hercules Setup
-----------------

https://www.betaarchive.com/forum/viewtopic.php?t=39613

CPUSERIAL 000111
CPUMODEL  2064
MAINSIZE  256
CNSLPORT  3270
NUMCPU    1
NUMVEC    1
ARCHMODE  ESA/390
OSTAILOR  VSE
PGMPRDOS  LICENSED

001F    3270
0200    3270
0201    3270
0202    3270
0203    3270
0204    3270
0205    3270
0206    3270

0150    3390    DOSRES.cckd sf=shadow/DOSRES_*.shadow
0151    3390    SYSWK1.cckd sf=shadow/SYSWK1_*.shadow

The readme file on the disc gave me some idea of how to boot everything up. The "Messages during VSE IPL" section goes over everything, and it says to enter "0 DELETE" to fix the "overlap on unexpired file" message. After that, the VTAM logon screen will appear. Also, the 2.4.0 ADCD images do not have TCP/IP.

https://fsck.technology/software/IBM/z%20Install%20Media/IBM%20zVM%204.4.0%20%28ADCD%29/


At first IPL on a new processor "OVERLAP ON UNEXPIRED FILE"
0 DELETE will reformat the page dataset

* P/390 VSE/ESA Application Development CD-ROM Version 2.4.0           11/11/99

*------------------------------------------------------------------------------*
  B. VSE/ESA 2.4.0 Configuration
*------------------------------------------------------------------------------*

This VSE/ESA system was built following the installation process defined
in the VSE/ESA Version 2 Installation Manual (SC33-6704).

The following replies have been made to the VSE/ESA installation process:

   Addr DOSRES     = 140 for FBA, 150 for CKD
   Addr SYSWK1     = 141 for FBA, 151 for CKD
   Environment     = B
   Security        = NO
   Local SNA CU    = NO
   Local 3270 Addr = 200
   Local 3270 Addr = 201
   Local 3270 Addr = 202
   FCB/UCB         = default


The system uses the predefined environment B which includes:


VSIZE = 250M
No of Address Spaces = 12
No of Static Partitions = 12
No of Dynamic Partition Classes = 4
Supervisor Mode = ESA ($$A$SUPX)
Default IPL Proc = $IPLESA
Default JCL Proc = $$JCL


This system contains the following program products:
---------------------------------------------------

        PRODUCT                              NUMBER    VERSION
========================                    ========   =======
VSE/ESA Version 2.4                         5690-VSE
   VSE Central Functions                    5686-066
      VSE/SP UNIQUE CODE                    5686-066     6.4
         VSE/POWER
         VSE/ICCF
         VSE/VSAM
         VSE/Fast Copy
         VSE/ESA Distributed Workstation Feature
         REXX/VSE
         VSE/OLTEP
         LANRES/VSE
         VSE C Language Run-Time Support
         VisualLift Run-Time Environment
         OSA/SF for VSE/ESA
         OS/390 API's

   VTAM                                     5686-065     4.2
   CICS Transaction Server for VSE/ESA      5648-054     1.1
   CICS/VSE                                 5686-026     2.3
   LE/VSE                                   5686-094     1.4
   High Level Assembler for VSE             5696-234     1.3
   DITTO/ESA for VSE                        5648-099     1.3
   EREP                                     5656-260     3.5
   ICKDSF                                   5747-DS2     1.16

VSE/ESA 2.4 Installed Optional Products:

   BTAM-ES                                  5746-RC5     1.1.0
   CCCA/VSE                                 5685-CCC     2.1.0
   COBOL for VSE/ESA                        5686-068     1.1.0
   C for VSE/ESA                            5686-A01     1.1.0
   DB2 Server for VSE & VM                  5648-158     6.1.0
   DFSORT/VSE                               5746-SM3     3.4.0
   GDDM/PGF                                 5668-812     2.1.3
   GDDM/VSE                                 5686-057     3.2.0
   High Level Assembler Tool Kit            5696-234     1.3.0
   LE/VSE Debug Tool                        5686-A02     1.1.0
   MQSeries for VSE/ESA                     5686-A06     2.1.0
   PLI for VSE/ESA                          5686-069     1.1.0
   QMF/VSE                                  5648-061     3.3.0
   VisualGen Host Services                  5648-078     1.1.0
   VisualLift for MVS, VM & VSE             5648-109     1.1.2


MISSING PROGRAMS:
-----------------
TCP/IP for VSE/ESA  5686-A04 V1.3.0


PREDEFINITIONS:
---------------
Two ICCF Administrator ID's have been created in addition to the SYSA
userid. They are SIE1 and P390. All administrator password's are the same
as the userid. It is recommended that you change these passwords immediately
after system installation. All three userids have ICCF library 10 as their
primary library. This was the library used for system installation and
customization. All customization was done using skeletons from ICCF library 59
and the modified jobs are located in ICCF library 10. A CICS\VSE 2.3 system
has been configured and is autostarted in partition F4 for co-existance and
testing purposes. This CICS can be disabled by modifying the SKUSERBG
member in ICCF library 10 and recataloging the USERBG.PROC if it is not
needed.

In addition there is a sample source program for PCOPY and associated
Job control members in VSE/ESA ICCF Library 59 (PCOP*). This sample is
provided on an "as is" basis. For details refer to the description in
the program header. This sample program has not been tested on a R/390.


*------------------------------------------------------------------------------*
  D. IPLing standalone utilities         d:\VSE\VSEUTILS.IPL
*------------------------------------------------------------------------------*

The VSEUTILS.IPL contains standalone versions of:
  - ICKDSF   : ICKDSF 1.16.0P - you MUST use this version for CKD volumes!
  - FASTCOPY : VSE FASTCOPY BACKUP/RESTORE 6.4.0
  - DITTO    : DITTO/ESA 1.3.0


Instructions for IPLing the VSEUTILS.IPL file:
      IPL 500 CLEAR
  1. To give the initial 3270 console interrupt, go to the first local
     3270 session, make it active, and then press ENTER. If nothing
     happens, then press the right-hand mouse button and select "ATTN"
     from the pop-up menu.



http://www.vmworkshop.org/2019/present/zvsehtip.pdf

SIR
SIR SYS
SIR MON
QUERY TD
SYSDEF TD,RESETCNT
SIR SMF=ON
SIR SMF=OFF


System Initialization
---------------------

IJSYSRES.SYSLIB 
    -   $ASIPROC.PROC - Paremeters , JCL Procedures
    -   $IPLxxx.PROC - I/O Device, Page Datasets, Lock communication file, Supervisor parameters, Shared virtual area definitions
    -   $0JCLxxx.PROC - BG Partition sizes, system labels, Library search chains, logical unit assignments
    -   $xJCLxxx.PROC - F1-FB forground library search chains and Logical unit assignments
Loadparm
    1. Console Type I - Integrated , L - Local
    2. Message Suppression, S - Suppress, . to display during IPL
    3. IPL Prompting , P prompt, . no prompt
    4. Startup mode prompting, P prompt, . no prompt
    5. formerly used for turbo dispatcher
    6-8. reserved.

 $ASIPROC.PROC
 CPU=FF123AC62094,IPL=$IPLX
 CPU=FF98EB542094,IPL=$IPLESA,JCL=$$JCL
 CPU=376FA7263906,IPL=$IPLP1,JCL=$$JCLP1
 CPU=37AF5AD53906,IPL=$IPLT9,JCL=$$JCLT9
 CPU=FF016B152817,IPL=$IPLV6,JCL=$$JCLV6
 CPU=00016B152817,IPL=$IPLN6,JCL=$$JCLN6

 $IPLV6.PROC
 0009,$$A$SUPI,VSIZE=2048M,VIO=512K,VPOOL=64K,LOG,IODEV=1024    
 ADD 009,3277                                                   
 ADD 00C,3505                                                    
 ADD 00D,3525P                                                  
 ADD 00E,PRT1                                                   
 ADD 123:126,ECKD,SHR
 ADD 400:402,OSAX                                               
 ADD 560,3490E,08                                               
 ADD FF0:FF9,3277                                           
 DLF VOLID=DOSRES,CYL=390,NCYL=8,DSF=Y,TYPE=N,NCPU=9
 SET ZONE=WEST/00/00                                        
 DEF SYSCAT=DOSRES,SYSREC=SYSWK1                                          
 SYS BUFSIZE=1500,NPARTS=120,DASDFP=YES,SEC(YES,NOTAPE),PASIZE=512M
 SYS SDSIZE=96K,SPSIZE=0K,BUFLD=YES,SERVPART=FB,TRKHLD=12  
 DPD VOLID=DOSRES,CYL=398,NCYL=36,TYPE=N,DSF=N
 DPD VOLID=DOSRES,CYL=434,TYPE=N,DSF=N        
 SVA SDL=700,GETVIS=(768K,20M),PSIZE=(652K,8M)


 $0JCLV6.PROC      (part 1 of 2)
 STDOPT ACANCEL=NO,DATE=MDY,DECK=NO,DUMP=PART,SYSDUMP=YES,SXREF=YES
 SYSDEF SYSTEM,NTASKS=255,TASKS=OLD
 // VDISK UNIT=FDF,BLKS=2880,VOLID=VDIDLA,USAGE=DLA
 // OPTION STDLABEL
 // DLBL IJSYSRS,'VSE.SYSRES.LIBRARY',99/366,SD
 // EXTENT SYSRES,DOSRES,1,0,1,899
 // DLBL IJQFILE,'VSE.POWER.QUEUE.FILE',99/366,DA
 // EXTENT SYS001,DOSRES,1,0,945,15
 // DLBL IJDFILE,'VSE.POWER.DATA.FILE',99/366,DA
 // EXTENT SYS002,SYSWK1,1,0,6330,1920
 // DLBL IJSYSCN,'VSE.HARDCOPY.FILE',99/366,SD
 // EXTENT SYSREC,SYSWK1,1,0,8355,60
 // DLBL IJSYSRC,'VSE.RECORDER.FILE',99/366,SD
 // EXTENT SYSREC,SYSWK1,1,0,8415,60
 // EXEC PROC=SETSDL    SET SDL
 PRTY BG,FA,F9,F8,F6,F5,F4,F2,F7,FB,F3,F1
 SET HC=YES,RF=YES,LINECT=66
 // JOB BGINIT
 EXPLAIN ON


 $0JCLV6.PROC      (part 2 of 2)
 ALLOC F1=32M,BG=32M,F2=256M,F3=15M,F4=32M,F5=32M
 ALLOC F6=32M,F7=32M,F8=2M,F9=1M,FA=32M,FB=2M
 SIZE F1=1500K,BG=1280K,F2=256M,F3=600K,F4=2M,F5=1M
 SIZE F6=1M,F7=1M,F8=2M,F9=1M,FA=1M,FB=512K
 SYSDEF DSPACE,DSIZE=256M,COMMAX=20
 NPGR BG=255,F1=50,F2=255,F3=100,F4=200,F5=100
 NPGR F6=100,F7=100,F8=200,F9=100,FA=100,FB=50
 START F1
 STOP
 ASSGN SYSIN,FEC
 ASSGN SYSPCH,FED
 ASSGN SYSLST,FEE
 ASSGN SYSLNK,DISK,VOL=DOSRES,SHR   SYSTEM LINK FILE
 ASSGN SYS001,DISK,VOL=SYSWK1,SHR   SYSTEM WORK FILE 1
 ASSGN SYS002,DISK,VOL=SYSWK1,SHR   SYSTEM WORK FILE 2
 ASSGN SYS003,DISK,VOL=SYSWK1,SHR   SYSTEM WORK FILE 3
 ASSGN SYS004,DISK,VOL=SYSWK1,SHR   SYSTEM WORK FILE 4
 // EXEC PROC=USERBG
 /&


 $4JCLV6.PROC
 LIBDEF DUMP,CATALOG=SYSDUMP.F4,PERM                                 
 LIBDEF PHASE,SEARCH=(PRD2.CONFIG,PRD1.BASE,PRD2.SCEEBASE,PRD2.PROD,    X
                PRD2.DBASE,PRD2.COMM),PERM                              
 LIBDEF OBJ,SEARCH=(PRD2.CONFIG,PRD1.BASE,PRD2.SCEEBASE,PRD2.PROD,      X
                PRD2.DBASE,PRD2.COMM),PERM                              
 LIBDEF SOURCE,SEARCH=(PRD2.CONFIG,PRD2.SCEEBASE,PRD1.BASE,PRD1.MACLIB, X
                PRD2.PROD,PRD2.DBASE,PRD2.COMM),PERM                  
 ASSGN SYSIN,FEC,PERM                                         
 ASSGN SYSPCH,FED                                                     
 ASSGN SYSLST,FEE                                                       
 ASSGN SYSLNK,DISK,VOL=DOSRES,SHR           SYSTEM LINK FILE            
 ASSGN SYS001,DISK,VOL=SYSWK1,SHR           SYSTEM WORK FILE 1          
 ASSGN SYS002,DISK,VOL=SYSWK1,SHR           SYSTEM WORK FILE 2          
 ASSGN SYS003,DISK,VOL=SYSWK1,SHR           SYSTEM WORK FILE 3          
 ASSGN SYS004,DISK,VOL=SYSWK1,SHR           SYSTEM WORK FILE 4 


 r rdr,tcpip00 

 PRELEASE RDR,VTAMSTRT
 PRELEASE RDR,CICSICCF


 Shutdown
 -----------

Entries on reader queue free and running.
 D RDR,FREE 

 MSG F2,DATA=CEMT P SHUT

 171 SHUT

 Z NET

 PEND - VSE/POWER Shutdown

 1 ROD - Record On Demand

 1 Y


Operator
-------------

PRTY - Query and set partition priorities

When issued with no parameters, the PRTY command will return a message with the current priority order for static partitions and 
dynamic partition classes. When issued with parameters, the PRTY command enables the operator to alter the priority order for one, some, or all partitions or classes.

The partition priorities are listed in the order of lowest priority first and highest priority last. In this example, the VSE/POWER partition F1 has the highest priority, while the dynamic class Z partitions have the lowest priority.

 PRTY F9,ABOVE,F4                                                              
 AR 0015 1Y63I  INVALID KEYWORD: ABOVE                                         
 AR 0015 1I40I  READY                                                           

 PRTY F4,BELOW,F9                                                               
 AR 0015 PRTY Z,Y,S,R,P,C,BG,FA,F4,F9,F8,F6,F5,F2,F7,FB,F3,F1                  
 AR 0015                                                                       
 AR 0015 1I40I  READY                                                           

 PRTY Z,Y,S,R,P,C,BG,FA,F8,F6,F5,F4,F9,F2,F7,FB,F3,F1                          
 AR 0015 PRTY Z,Y,S,R,P,C,BG,FA,F8,F6,F5,F4,F9,F2,F7,FB,F3,F1                  
 AR 0015                                                                        
 AR 0015 1I40I  READY 

MAP - Display Storage Layout , Shows Jobs in progress
MAP CLASS=ALL

PDISPLAY DYNC / D DYNC - display the currently active VSE/POWER dynamic class table.

AUTOIPL

PDISPLAY A,PART, short form D A,PART, will display the current VSE/POWER active tasks associated with static or active dynamic partitions.

PDISPLAY QP, short form D QP, will display the current status of the VSE/POWER queue, data, and account files. It is important to know when they may be close to full.

The D BIGGEST command will display the largest entries on the VSE/POWER spool queues. By default, this command will display the sixteen largest spool entries

L LST,OPJOB2,43448 to purge your first chosen spool entry

d biggest,limit=7

paccount 581
j disk,acctsve
paccount del
j pun 

d pun,full=yes

 D RDR,FREE                                                                    
 AR 0015 1C39I COMMAND PASSED TO VSE/POWER                                     
 F1 0001 1R46I  READER QUEUE   P D C S  CARDS BU                               
 F1 0001 1R46I  CICSICCF 44021 3 * 2       71   PART=F2 FROM=(SYSA)            
 F1 0001 1R46I  VTAMSTRT 44020 3 * 3       20   PART=F3 FROM=(SYSA)            
 F1 0001 1R46I  DTVJOB7  43629 3 K 5        7   RUN=22:30,01/11 FROM=(SYSA)    
 F1 0001 1R46I  TCPIP00  44023 3 * 7       11   PART=F7 FROM=(SYSA)            

 D RDR,FREER                                                                    
 AR 0015 1C39I COMMAND PASSED TO VSE/POWER                                     
 F1 0001 1R46I  READER QUEUE   P D C S  CARDS BU                               
 F1 0001 1R46I  CICSICCF 44021 3 * 2       71   PART=F2 FROM=(SYSA)            
 F1 0001 1R46I  VTAMSTRT 44020 3 * 3       20   PART=F3 FROM=(SYSA)            
 F1 0001 1R46I  TCPIP00  44023 3 * 7       11   PART=F7 FROM=(SYSA)            

 D WRUN,FULL=YES                                                               
 AR 0015 1C39I COMMAND PASSED TO VSE/POWER                                     
 F1 0001 1R46I  READER QUEUE   P D C S  CARDS BU(WAIT FOR RUN SUBQUEUE)        
 F1 0001 1R46I  DTVJOB7  43629 3 K 5        7   RUN=22:30,01/11 FROM=(SYSA)    
 F1 0001        D=01/07/2019 DBGP=000001                                       
 F1 0001        DUETIME=22:30 DUEDAY=(FRI) RERUN=YES                           
 F1 0001        SECN=AAAA QNUM=01771 T=04:45:22 TKN=00000299                   
 F1 0001        DE=01/07/2019 TE=04:45:22  


The PDISPLAY command, short form D, can also be used with wildcards to display many VSE/POWER objects. For example, to display all jobs in the RDR queue whose jobname begins with PAUSE you would issue D RDR,PAUSE*, as shown here.

The PRELEASE command, short form R, can be used to release a held job to now be dispatchable. This will change the disposition from L to K, or from H to D, and enable a job to run. For example, R RDR,PAUSEF9 will make that job eligible to run.

The PALTER command, short form A, can be used to alter attributes of a VSE/POWER spool entry, or the input classes of a static partition. For example A RDR,PAUSEF9,DISP=K,CLASS=8 will make that job eligible to run and change the class to 8.


CICS
------------

MSG F2,DATA=CEMT I TAS command to display the currently active CICS tasks.

 to inquire on data sets whose name starts with I and that also have F as part of the file name. CEMT I FILE(I*F*) will be the CICS command to be issued.

MSG F2,DATA=CEMT I FILE(I*F*) 

MSG F2,DATA=CEMT P SHUT

VTAM/TCPIP
-------------

VTAM DISPLAY NET command, short form D, will be used to display VTAM status information, followed by the TCP/IP QUERY TELNETDS command, short form Q, to display TCP/IP status information.

QUERY ACTIVE,TYPE=TELNETD

delete telnetd,id=xxx
v net,inact,id=xxxx

v net,act,id=xxx
define telnetd,id=xxx




