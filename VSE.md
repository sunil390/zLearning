VSE and z/VSE From Scratch
--------------------------

Internet Archive https://archive.org/details/VMESA240ADCDCD1 

VSE ADCD
https://www.betaarchive.com/forum/viewtopic.php?t=39613

```
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
```
The readme file on the disc gave me some idea of how to boot everything up. The "Messages during VSE IPL" section goes over everything, and it says to enter "0 DELETE" to fix the "overlap on unexpired file" message. After that, the VTAM logon screen will appear. Also, the 2.4.0 ADCD images do not have TCP/IP.


At first IPL on a new processor "OVERLAP ON UNEXPIRED FILE"
0 DELETE will reformat the page dataset

* P/390 VSE/ESA Application Development CD-ROM Version 2.4.0           11/11/99

*------------------------------------------------------------------------------*
  B. VSE/ESA 2.4.0 Configuration
*------------------------------------------------------------------------------*

This VSE/ESA system was built following the installation process defined
in the VSE/ESA Version 2 Installation Manual (SC33-6704).

The following replies have been made to the VSE/ESA installation process:
```
   Addr DOSRES     = 140 for FBA, 150 for CKD
   Addr SYSWK1     = 141 for FBA, 151 for CKD
   Environment     = B
   Security        = NO
   Local SNA CU    = NO
   Local 3270 Addr = 200
   Local 3270 Addr = 201
   Local 3270 Addr = 202
   FCB/UCB         = default
```

The system uses the predefined environment B which includes:

```
VSIZE = 250M
No of Address Spaces = 12
No of Static Partitions = 12
No of Dynamic Partition Classes = 4
Supervisor Mode = ESA ($$A$SUPX)
Default IPL Proc = $IPLESA
Default JCL Proc = $$JCL
```

This system contains the following program products:

```
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
```

MISSING PROGRAMS:

TCP/IP for VSE/ESA  5686-A04 V1.3.0


PREDEFINITIONS:

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

InterSkill Training - z/VSE Infrastructure and System Operation
---------------------------------------------------------------

System Initialization

```
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
```

```
 r rdr,tcpip00 

 PRELEASE RDR,VTAMSTRT
 PRELEASE RDR,CICSICCF
```

 Shutdown
 -----------

Entries on reader queue free and running.
 D RDR,FREE 

 MSG F2,DATA=CEMT P SHUT
 171 SHUT
 Z NET

 PEND - VSE/POWER Shutdown

 0 ROD - Record On Demand

 1 Y


Operator
-------------

```
PRTY - Query and set partition priorities

```
When issued with no parameters, the PRTY command will return a message with the current priority order for static partitions and 
dynamic partition classes. When issued with parameters, the PRTY command enables the operator to alter the priority order for one, some, or all partitions or classes.

The partition priorities are listed in the order of lowest priority first and highest priority last. In this example, the VSE/POWER partition F1 has the highest priority, while the dynamic class Z partitions have the lowest priority.

```
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

```
PDISPLAY A,PART, short form D A,PART, will display the current VSE/POWER active tasks associated with static or active dynamic partitions.

PDISPLAY QP, short form D QP, will display the current status of the VSE/POWER queue, data, and account files. It is important to know when they may be close to full.

The D BIGGEST command will display the largest entries on the VSE/POWER spool queues. By default, this command will display the sixteen largest spool entries
```

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
```

The PDISPLAY command, short form D, can also be used with wildcards to display many VSE/POWER objects. For example, to display all jobs in the RDR queue whose jobname begins with PAUSE you would issue D RDR,PAUSE*, as shown here.

The PRELEASE command, short form R, can be used to release a held job to now be dispatchable. This will change the disposition from L to K, or from H to D, and enable a job to run. For example, R RDR,PAUSEF9 will make that job eligible to run.

The PALTER command, short form A, can be used to alter attributes of a VSE/POWER spool entry, or the input classes of a static partition. For example A RDR,PAUSEF9,DISP=K,CLASS=8 will make that job eligible to run and change the class to 8.


CICS
------------

```
MSG F2,DATA=CEMT I TAS command to display the currently active CICS tasks.

 to inquire on data sets whose name starts with I and that also have F as part of the file name. CEMT I FILE(I*F*) will be the CICS command to be issued.

MSG F2,DATA=CEMT I FILE(I*F*) 
MSG F2,DATA=CEMT P SHUT
```

VTAM/TCPIP
-------------

VTAM DISPLAY NET command, short form D, will be used to display VTAM status information, followed by the TCP/IP QUERY TELNETDS command, short form Q, to display TCP/IP status information.

```
QUERY ACTIVE,TYPE=TELNETD

delete telnetd,id=xxx
v net,inact,id=xxxx

v net,act,id=xxx
define telnetd,id=xxx
```



zVSE 4.1
----------

https://fsck.technology/software/IBM/z%20Install%20Media/IBM%20zVSE%204.1.1/

```
#------------------------------------------------------------------- 
# Configuration file for Hercules ESA/390 emulator
#-------------------------------------------------------------------

CPUSERIAL 071060
CPUMODEL  7060
MAINSIZE  512
XPNDSIZE  0
CNSLPORT  3270
NUMCPU    1
ARCHMODE  ESAME
LOADPARM  É.T
SYSEPOCH  1900
TZOFFSET  -0000
OSTAILOR  VSE
DEVTMAX   0
PGMPRDOS  LICENSED

# ------------------------------------------------------------------ 
#  Consoles
# ------------------------------------------------------------------ 
0200	3270
0201	3270          
0202	3270          
0203	3270

# ------------------------------------------------------------------
# 0400.2 LCS -n 192.168.2.81 -m 02:00:5E:A8:02:11  192.168.2.44

0400.2 LCS -n 192.168.2.22 -m 02:00:5E:A8:02:11  192.168.2.44

# ------------------------------------------------------------------

0100    3390    D:\Z\ZVSE\zvse1.cckd
0101    3390    D:\Z\ZVSE\zvse2.cckd

0581    3480    D:\Z\ZVSE\zvseen.aws
0582    3480    D:\Z\ZVSE\zvsecobol.aws
0583    3480    D:\Z\ZVSE\zvsexbase.aws
0584    3480    D:\Z\ZVSE\zvsedb2.aws

```

ipl from zvseen.aws

follow steps 4.2 onwards in Hands-On Lab: z/VSE Tape-less Installation  http://www.vmworkshop.org/docs/2016/vseinst.PDF

DB2 Install question.

```
detach 581
attach 0581    3480    D:\Z\ZVSE\zvsexbase.aws
```
follow steps 5.1 onwards in Hands-On Lab: z/VSE Tape-less Installation

Signon with POST and password as BASE

follow steps 5.2 onwards in Hands-On Lab: z/VSE Tape-less Installation



Roger Bowler’s VSE survival guide for z/OS systems programmers
--------------------------------------------------------------

http://www.rogerbowler.fr/vseguide.htm


**VSE console commands**
```
D A   Display active jobs
MAP   Display partitions
VOLUME Display disk and tape units
D RDR Display jobs in reader queue
D LST Display jobs in print queue
D PUN Display jobs in print queue
D xxx,prefix* (xxx=RDR/LST/PUN) Display jobs beginning with prefix
A RDR,jobname,DISP=H  Hold job in reader queue
A RDR,jobname,CLASS=A Change class of job in reader queue
R RDR,jobname Release held job
R RDR,PAUSEBG Obtain a command prompt
L RDR,jobname[,nnnn] Delete job from reader queue where nnnn is job number (take care not to enter L RDR,ALL)
```

**ICCF Editor** 

```
F6    Find 
F7    Scroll back
F8    Scroll forward
F9    Top of file
F10   Scroll left
F11   Scroll right
F12   End of file
L string  Find next
LU string Find previous
C/old/new/* G Global change
N n Scroll forward n lines
U n Scroll back n lines
```
To recall the last command, You can't. But you can prefix a command by & to make it stay in the entry area.


**Line commands**
```
An    Insert n blank lines
Dn    Delete n lines
Cn    Copy n lines to scratchpad
Mn    Move n lines to scratchpad
I     Insert scratchpad after this line
"n    Duplicate this line n times
```

**VSE JCL statements**

POWER job card

```
* $$ JOB JNM=jobname,CLASS=0,DISP=L
DISP=D means run and then delete from reader queue
DISP=H means hold in reader queue without running
DISP=K means run and then keep in reader queue for rerun
DISP=L means leave in reader queue until released, then keep for rerun

POWER list card
* $$ LST DISP=D,CLASS=A,DEST=(,vmuserid)

LIBDEF card is analogous to MVS STEPLIB
// LIBDEF *,SEARCH=(PRD1.BASE,PRD2.CONFIG)

Issue a POWER command from JCL
// PWR PRELEASE RDR,jobname

POWER end of job card
* $$ EOJ
```

**Clearing the account file**

When the account file is full, the system will grind to a halt with one or more of the following messages on the console or the user's terminal:

1Q32A NO MORE ACCOUNT FILE (IJAFILE) SPACE FOR SAS ,GSP
UNABLE TO CONTINUE - SPOOLING SYSTEM IS SHORT ON SPOOL OR ACCOUNT FILE SPACE.
Issuing the PACCOUNT command at the system console will delete the account file data and allow the system to continue:
```
J DEL
```
Clears the account file (J is the abbreviation for PACCOUNT)

**VSE timezone settings for Central European Summer Time**

To have VSE automatically select the correct timezone at IPL, include the following statements in member $IPLESA.PROC of library IJSYSRS.SYSLIB and remove the SET ZONE statement (if any) from your IPL procedure.
```
SET ZONEDEF,ZONE=EAST/01/00,CET
SET ZONEDEF,ZONE=EAST/02/00,CES                  
SET ZONEBDY,DATE=03/29/2009,CLOCK=02/00/00,CES   
SET ZONEBDY,DATE=10/25/2009,CLOCK=03/00/00,CET   
SET ZONEBDY,DATE=03/28/2010,CLOCK=02/00/00,CES   
SET ZONEBDY,DATE=10/31/2010,CLOCK=03/00/00,CET   
SET ZONEBDY,DATE=03/27/2011,CLOCK=02/00/00,CES   
SET ZONEBDY,DATE=10/30/2011,CLOCK=03/00/00,CET   
SET ZONEBDY,DATE=03/25/2012,CLOCK=02/00/00,CES   
SET ZONEBDY,DATE=10/28/2012,CLOCK=03/00/00,CET
```

**Starting jobs automatically at IPL**

Submit the job with DISP=L on the POWER job card
Edit member SKUSERBG in ICCF library 59, adding the following statement just before the /+ card: // PWR PRELEASE RDR,jobname
Run the job COPYUBG from member SKPREPC2 in ICCF library 59 to copy SKUSERBG to USERBG.PROC in library IJSYSRS.SYSLIB

**VSE catalogs**

Catalogs have two names: a 7-character name called the "catalog name", and a 44-character name called the "catalog id". The "catalog name" is the name you specify on the CAT= parameter of the DLBL statement when you refer to a file cataloged in that catalog.

ICCF path 225 (Resource Definition - File and Catalog Management - Display or Process a Catalog, Space) will give you a list of the catalogs defined on your system, which typically might look like this:
```
CATALOG ID                                       CATALOG NAME
VSAM.MASTER.CATALOG                                IJSYSCT   
VSESP.USER.CATALOG                                 VSESPUC   
```
By defining a DLBL with name IJSYSUC, you can do the equivalent of a JOBCAT statement in OS/390:
```
// DLBL IJSYSUC,'VSESP.USER.CATALOG',,VSAM
```
**VSE VTAM mode tables**
```
ISTINCLM.Z and ISTINCLM.PHASE in library PRD1.BASE
IESINCLM.A and IESINCLM.PHASE in library IJSYSRS.SYSLIB
```
**VSE VTAM USS tables**
The VTAM USS table is built from source members VTMUSSCD.A, VTMUSSTZ.A, VTMUSSTX.A in PRD2.CONFIG. The load modules are VTMUSSTR.PHASE (for SNA terminals) and VTMUSSTB.PHASE (for non-SNA terminals) in PRD2.CONFIG. The default tables are in IJSYSRS.SYSLIB.
To rebuild the tables see member SKVTMUSS in ICCF library 59.
To reload the new table:
```
F NET,TABLE,OPTION=LOAD,NEWTAB=VTMUSSTB
```
(note: unlike MVS, it's always F NET, regardless of the VTAM jobname)

**VSE VTAM buffer trace**
```
F NET,TRACE,TYPE=BUF,ID=luname (note: unlike MVS, it's always F NET, regardless of the VTAM jobname)
Run test
F NET,NOTRACE,TYPE=BUF,ID=luname
F NET,SUBTASK,ID=TPRINT,FUNCTION=ATTACH
F3 0120 IST907A SNAPSHOT MODE TPRINT? ENTER Y OR N
120 n
F3 0120 IST905A ENTER TRACE PRINT OPTIONS OR 'CANCEL'
120 print buf=telnlu03
Default options are: BUF=ALL,CLEAR=NO,IO=ALL,LINE=ALL,TNST=ALL,VIT,FORMAT=YES
You can also specify: INTERVAL=(hh:mm:ss,hh:mm:ss)
F3 0120 4933D EQUAL FILE ID IN VTOC TRFILE SYS001=261 VSEWK1
VTAM.TRACE.FILE
120 delete
```
The VTAM SYSLST output can be viewed using ICCF administrator option 326 (Operations - Manage Batch Queues - In-Creation Queue)

**VSE CICS message log**
The CICS message log (MSGUSR) is written to queue CSMT, which is redirected to queue IESL, and processed by transaction IESX which writes the messages into the CICS SYSLST. You can view the messages while CICS is running using ICCF administrator option 326 (Operations - Manage Batch Queues - In-Creation Queue).

Alternatively you can use CEMT I TDQ(IESL) and reset the trigger level to prevent the messages being written to SYSLST, then use the CEMS transaction to create a report from the messages which have accumulated on queue IESL. The report will be written to the LST queue under jobname IESL (note: you must enter a title, or the report will not be written).

**VSE PC File Transfer**
If the PC Host Transfer File does not yet exist, run the job IWSTRFL (in ICCF library 59 member SKIWSTF) to define the VSAM file PC.HOST.TRANSFER.FILE and to define it as file INWFILE in the standard labels. Then use this CEDA command to define the file to CICS:
```
     DEF FILE(INWFILE) GROUP(FCTSP)
         DESC(PC HOST TRANSFER FILE)
         STATUS(ENABLED) OPENTIME(STARTUP) RECORDFORMAT(V)
         ADD(YES) BROWSE(YES) DELETE(YES) READ(YES) UPDATE(YES)
```     
Make sure your terminal is using a logmode with the 3270 Query bit set. If using TCP/IP, the logmode is specified in the DEFINE TELNETD statement. This is what worked for me:
```
     DEFINE TEL,ID=LU,MENU=SYSPMENU,TERM=TELNLU,CO=8,PORT=23, -            
     LOGMODE=NSX32702,LOGMODE3=NSX32703,LOGMODE4=NSX32704,LOGMODE5=NSX32705
```     
You also need to get CICS to use a TYPETERM which contains the EXTENDEDDS(YES) parameter. I used TYPETERM(VSE3278Q) in GROUP(VSETYPE). TYPETERM(VSE3278Q) is referenced by the autoinstall definition TERM(D910) in GROUP(VSETERM). It won't work if CICS autoinstall chooses the definition TERM(D901) which references TYPETERM(VSE32782).
Use the CICS transaction INWQ to determine whether you have correctly picked up the logmode with the query bit. INWQ will respond with the message xxxx=DFT if the query bit is set, or xxxx=CUT if not (where xxxx is your terminal id).
Make sure the DFT setting is enabled in your 3270 emulator's file transfer options.
These are the options I used to upload an EBCDIC jobstream from the PC into the host transfer file:
     send jclfile.bin sysajob ( file=htf lrecl=80 binary )
     
The transferred file is then accessible using ICCF option 3 (Operations) then 8 (Personal Computer Move Utilities) which gives you the option of moving the file into an ICCF library.
Alternatively, you can submit the job directly into the POWER reader queue. These are the options I used:
     send jclfile.bin ( file=rdr lrecl=80 binary nouc )
     
You can also transfer files to and from VSE libraries, VSAM files, CICS TS queues, or the POWER LST or PUN queue. See the manual "VSE/ESA Programming and Workstation Guide" for details.
Note: Even successful transfers seem to end with the message:
     INW0002I  Transmission error. Module=INWPGET1 RC=0200

## z/VSE Basics

```
query TD                                                        
AR 0015  CPU   STATUS    SPIN_TIME    NP_TIME TOTAL_TIME NP/TOT 
AR 0015   00   ACTIVE            0      17866      26568  0.672 
AR 0015   01   INACTIVE                                         
AR 0015   02   INACTIVE                                         
AR 0015   03   INACTIVE                                         
AR 0015   04   INACTIVE                                         
AR 0015   05   INACTIVE                                         
AR 0015   06   INACTIVE                                         
AR 0015   07   INACTIVE                                         
AR 0015                 ----------------------------------------
AR 0015 TOTAL                    0      17866      26568  0.672 
AR 0015                                                         
AR 0015               NP/TOT: 0.672      SPIN/(SPIN+TOT): 0.000 
AR 0015  OVERALL UTILIZATION:   0%        NP UTILIZATION:   0%  
AR 0015                                                         
AR 0015  ELAPSED TIME SINCE LAST RESET:      8454462            
AR 0015 1I40I  READY                                            

volume                                                                        
AR 0015 CUU  CODE DEV.-TYP   VOLID  USAGE   SHARED    STATUS    CAPACITY      
AR 0015 100  6E   3390-006  DOSRES  USED                             2226 CYL 
AR 0015 101  6E   3390-006  SYSWK1  USED                             2226 CYL 
AR 0015 581  5400 3480-D31  *NONE*  UNUSED              SYNC            0 BLK 
AR 0015 582  5400 3480-D31  *NONE*  UNUSED              SYNC            0 BLK 
AR 0015 583  5400 3480-D31  *NONE*  UNUSED              SYNC            0 BLK 
AR 0015 584  5400 3480-D31  NLSVSE  UNUSED              SYNC            0 BLK 
AR 0015 FDF  90   FBA0-00   VDIDLA  USED                             2880 BLK 
AR 0015 1I40I  READY                                                          
status 100                                                                    
AR 0015 SCHIB DEV  INT-PARM ISC FLG LP PNO LPU PI MBI  PO PA CHPID0-3 CHPID4-7
AR 0015 0006  0100 000053B8   3  81 80  00  80 80 0000 80 80 01000000 00000000
AR 0015 1I40I  READY                                                          

sir                                                                       
AR 0015 CPUID     = FD01106070600000                                      
AR 0015 PROCESSOR = HRC 7060-EMULZZ (71060ZZ)  LPAR = HERCULES  No. = 0001
AR 0015 VM-SYSTEM =                 (0000)   USERID =          VMCF = OFF 
AR 0015      CPUs = 0000                       Cap. =  00%                
AR 0015 PROC-MODE = z/Arch          IPL(100)    14:21:10      08/07/2021  
AR 0015 SYSTEM    = z/VSE           4.1.1                     10/15/2007  
AR 0015             VSE/AF          8.1.0       DY46717       09/12/2007  
AR 0015             VSE/POWER       8.1.0       DY46782       07/31/2007  
AR 0015 IPL-PROC  = $IPLESA         JCL-PROC  = $$JCL                     
AR 0015 SUPVR     = $$A$SUPI        TURBO-DISPATCHER (51) ACTIVE          
AR 0015                             HARDWARE COMPRESSION ENABLED          
AR 0015 SEC. MGR. = BASIC           SECURITY  = ONLINE                    
AR 0015 CPU-ADDR. = 0000(IPL)   ACTIVE                                    
AR 0015   ACTIVE  = 0000:00:00.166   WAIT = 0000:01:32.077                
AR 0015   PARALLEL= 0000:00:00.035   SPIN = 0000:00:00.000                
AR 0015 CPU-ADDR. = 0001        CPU INACTIVE NOT PREFIXED                 
AR 0015 CPU-ADDR. = 0002        CPU INACTIVE NOT PREFIXED                 
AR 0015 CPU-ADDR. = 0003        CPU INACTIVE NOT PREFIXED                 
AR 0015 CPU-ADDR. = 0004        CPU INACTIVE NOT PREFIXED                 
AR 0015 CPU-ADDR. = 0005        CPU INACTIVE NOT PREFIXED                 
AR 0015 CPU-ADDR. = 0006        CPU INACTIVE NOT PREFIXED                 
AR 0015 CPU-ADDR. = 0007        CPU INACTIVE NOT PREFIXED                 
AR 0015 CPU timings MEASUREMENT INTERVAL    0000:01:33.292                
AR 0015 TASKS ATT.= 00015           HIGH-MARK = 00015    MAX = 00164      
AR 0015 DYN.PARTS = 00000           HIGH-MARK = 00001    MAX = 00048      
AR 0015                                                                   
AR 0015 COPY-BLKS = 00013           HIGH-MARK = 00035    MAX = 01522      
AR 0015 CHANQ USED= 00003           HIGH-MARK = 00007    MAX = 00069      
AR 0015 LBL.-SEGM.= 00007           HIGH-MARK = 00007    MAX = 00717      
AR 0015 PGIN  TOT.= 0000000001      EXP.AVRGE.= 0000000000/SEC            
AR 0015 PGOUT TOT.= 0000000001                                            
AR 0015       UNC.= 0000000001      EXP.AVRGE.= 0000000000/SEC            
AR 0015       PRE = 0000000000      EXP.AVRGE.= 0000000000/SEC            
AR 0015 LOCKS EXT.= 0000000674      LOCKS INT.= 0000005922                
AR 0015      FAIL = 0000000022           FAIL = 0000000025                
AR 0015 LOCK I/O  = 0000000000      LOCK WRITE= 0000000000                
AR 0015 1I40I  READY                                                      

sir chpid                                                     
AR 0015 CHPID CHLA SWLA LSN  CHPP     CHANNEL-PATH-DESCRIPTION
AR 0015  01                       EMULATED-I/O CHANNEL (EIO)  
AR 0015  02                       EMULATED-I/O CHANNEL (EIO)  
AR 0015  04                       EMULATED-I/O CHANNEL (EIO)  
AR 0015  05                       EMULATED-I/O CHANNEL (EIO)  
AR 0015 1I40I  READY                                          

```
