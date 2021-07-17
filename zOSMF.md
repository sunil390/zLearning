
z/OSMF area to be configured Description

Nucleus Nucleus IZUNUSEC
Notifications task Core service IZUNFSEC
z/OS data set and file REST services Core service IZURFSEC
z/OS jobs REST services Core service IZURJSEC
Swagger service Core service IZUSWSEC
TSO/E address space services Core service IZUTSSEC
z/OSMF administrative tasks Core service IZUATSEC
z/OSMF settings service Core service IZUSTSEC
z/OSMF Workflows task Core service IZUWFSEC

Nucleus, plus all core services IZUSEC , RC=04

Capacity Provisioning service Optional service IZUCPSEC
Cloud Provisioning services Optional service IZUPRSEC
Console services Optional service IZUGCSEC
Incident Log service Optional service IZUILSEC
ISPF service Optional service IZUISSEC
Network Configuration Assistant service Optional service IZUCASEC
Resource Monitoring service Optional service IZURMSEC
Security Configuration Assistant Optional service IZUSASEC
Software Management service Optional service IZUDMSEC
Sysplex Management service Optional service • IZUSPSEC , IZUDCSEC
Workload Management service Optional service IZUWMSEC
z/OS Encryption Readiness Technology (zERT)
Network Analyzer Optional service IZUNASEC
Use the autostart capability Advanced configuration IZUASSEC
Use ICSF services Advanced configuration IZUICSEC
Use AT-TLS connections Advanced configuration IZUTLSEC
Create the z/OSMF key ring and certificate Advanced configuration IZUSKSEC


Java   /usr/lpp/java/J8.0_64
 JAVA_HOME statement in your IZUPRMxx

cd / Libery Profile /usr/lpp/liberty_zos

 IZUSVR1 started procedure on the keyword WLPDIR=

/usr/lpp/zosmf 

CEASEC

SYS1.PARMLIB(CEASEC00)

Multiple CEA Parm members
F CEA,CEA=(01,02,03)

```
F CEA,D,PARMS                                             
CEA0023I COMMON EVENT ADAPTER     085                     
STATUS: ACTIVE-MINIMUM   CLIENTS: 0  INTERNAL: 0          
CEA = (00)                                                
SNAPSHOT           = N                                    
HLQLONG            = CEA         HLQ          =           
BRANCH             =             COUNTRYCODE  =           
CAPTURE RANGE FOR SLIP DUMPS:                             
LOGREC             = 01:00:00    LOGRECSUMMARY= 04:00:00  
OPERLOG            = 00:30:00                             
CAPTURE RANGE FOR ABEND DUMPS:                            
LOGREC             = 01:00:00    LOGRECSUMMARY= 04:00:00  
OPERLOG            = 00:30:00                             
CAPTURE RANGE FOR CONSOLE DUMPS:                          
LOGREC             = 01:00:00    LOGRECSUMMARY= 04:00:00  
OPERLOG            = 00:30:00                             
TSOASMGR:                                                 
RECONSESSIONS      = 0           RECONTIME    = 00:00:00  
MAXSESSIONS        =   50        MAXSESSPERUSER=   10     
```

NETSTAT SOCKET
NETSTAT BYTE

Global Mountpoint /global/zosmf

dataset search function IZURFSEC

CONNECT userid GROUP(IZUADMIN)

Job IZUAUTH

zOSMF User IZUUSER Group.


IZUMKFS Creates and Mounts file system /global/zosmf  SYS1.OMVS.SIZUUSRD.X24OA1


S IZUANG1
S IZUSVR1,IZUPRM=PRV is the default.

F IZUSVR1,DISPLAY IZU


PERMIT IZUDFLT.** CLASS(ZMFAPLA) ID(IZUADMIN) ACCESS(READ)
PERMIT CEA.* CLASS(SERVAUTH) ID(IZUADMIN) ACCESS(READ)    
SETROPTS RACLIST(ZMFAPLA) REFRESH                            
SETROPTS RACLIST(SERVAUTH) REFRESH                        



## Security Configuration Assistant

  RDEFINE OPERCMDS MVS.MCSOPER.*            UACC(NONE)                  
  RDEFINE OPERCMDS MVS.VARY.TCPIP.OBEYFILE   UACC(NONE)                 
  RDEFINE OPERCMDS MVS.DISPLAY.XCF           UACC(NONE)                 
  RDEFINE OPERCMDS MVS.DISPLAY.TCPIP         UACC(NONE)                 
  RDEFINE OPERCMDS MVS.DISPLAY.JOB           UACC(NONE)                 
  PE MVS.MCSOPER.*           CLASS(OPERCMDS) ID(IZUADMIN) ACC(READ)     
  PE MVS.VARY.TCPIP.OBEYFILE CLASS(OPERCMDS) ID(IZUADMIN) ACC(CONTROL)  
  PE MVS.DISPLAY.XCF  CLASS(OPERCMDS)  ID(IZUADMIN) ACC(READ)           
  PE MVS.DISPLAY.TCPIP  CLASS(OPERCMDS)  ID(IZUADMIN) ACC(READ)         
  PE MVS.DISPLAY.JOB  CLASS(OPERCMDS)  ID(IZUADMIN) ACC(READ)           
  SETROPTS RACLIST(OPERCMDS) REFRESH                                    

  RDEF ZMFCLOUD IZUDFLT.ZOSMF.SECURITY.ADMIN UACC(NONE) OWNER(SYS1)     
  PE IZUDFLT.ZOSMF.SECURITY.ADMIN CLASS(ZMFCLOUD) ID(IZUSECAD) ACC(READ)
  PE IZUDFLT.ZOSMF.SECURITY.ADMIN CLASS(ZMFCLOUD) ID(SYSPRG1) ACC(READ) 
  SETROPTS RACLIST(ZMFCLOUD) REFRESH                                    

Software Management
  RDEFINE UNIXPRIV SUPERUSER.FILESYS.MOUNT  UACC(NONE) OWNER(SYS1)      
  PE SUPERUSER.FILESYS.MOUNT CLASS(UNIXPRIV) ID(IZUADMIN) ACCESS(UPDATE)
  PE SUPERUSER.FILESYS.MOUNT CLASS(UNIXPRIV) ID(IZUUSER) ACCESS(UPDATE) 
  SETROPTS RACLIST(UNIXPRIV) REFRESH                                    

Incident log

  RDEFINE SERVAUTH     CEA.CEAGETPS UACC(NONE) OWNER(SYS1)        
  RDEFINE SERVAUTH     CEA.CEADOCMD UACC(NONE) OWNER(SYS1)        
  RDEFINE SERVAUTH     CEA.CEAPDWB* UACC(NONE) OWNER(SYS1)        
  RDEFINE SERVAUTH     CEA.CEADOCONSOLECMD UACC(NONE) OWNER(SYS1) 
  PE CEA.CEAGETPS CLASS(SERVAUTH) ID(IZUADMIN) ACC(UPDATE)        
  PE CEA.CEADOCMD CLASS(SERVAUTH) ID(IZUADMIN) ACC(UPDATE)        
  PE CEA.CEAPDWB* CLASS(SERVAUTH) ID(IZUADMIN) ACC(UPDATE)        
  PE CEA.CEADOCONSOLECMD CLASS(SERVAUTH) ID(IZUUSER)  ACC(UPDATE) 
  PE CEA.CEAGETPS CLASS(SERVAUTH) ID(IZUUSER)  ACC(UPDATE)        
  PE CEA.CEADOCMD CLASS(SERVAUTH) ID(IZUUSER)  ACC(UPDATE)        
  PE CEA.CEAPDWB* CLASS(SERVAUTH) ID(IZUUSER)  ACC(UPDATE)        
  PE CEA.CEADOCONSOLECMD CLASS(SERVAUTH) ID(IZUUSER)  ACC(UPDATE) 
  SETROPTS RACLIST(SERVAUTH) REFRESH                              

  Operator Console

  RDEF OPERCMDS MVS.DISPLAY.EMCS UACC(NONE) OWNER(SYS1)          
  RDEF OPERCMDS MVS.DISPLAY.TIMEDATE UACC(NONE) OWNER(SYS1)      
  RDEF OPERCMDS MVS.DISPLAY.OMVS UACC(NONE) OWNER(SYS1)          
  PE MVS.DISPLAY.EMCS CLASS(OPERCMDS) ID(SYSPRG1) ACC(READ)      
  PE MVS.DISPLAY.TIMEDATE   CLASS(OPERCMDS) ID(SYSPRG1) ACC(READ)
  PE MVS.DISPLAY.OMVS CLASS(OPERCMDS) ID(SYSPRG1) ACC(READ)      
  SETROPTS RACLIST(OPERCMDS) REFRESH                             

PE IZUDFLT.ZOSMF.ZERT_NETWORK_ANALYZER     -  
   CLASS(ZMFAPLA) ID(SYSPRG1) ACC(READ)       
PE IZUDFLT.IzuZertNetworkAnalyzer.izuUsers -  
   CLASS(EJBROLE) ID(SYSPRG1) ACC(READ)       
SETROPTS RACLIST(EJBROLE) REFRESH             
SETROPTS RACLIST(ZMFAPLA) REFRESH             

RDEF SERVAUTH EZB.NETWORKUTILS.CLOUD.DCUF    UACC(NONE) OWNER(SYS1) 
PE EZB.NETWORKUTILS.CLOUD.DCUF CLASS(SERVAUTH) ID(IZUSVR) ACC(READ) 
SETROPTS RACLIST(SERVAUTH) REFRESH                                  

RDEFINE SERVAUTH     CEA.CEADOCONSOLECMD UACC(NONE) OWNER(SYS1)
PE CEA.CEADOCONSOLECMD CLASS(SERVAUTH) ID(SYSPRG1)  ACC(UPDATE)
SETROPTS RACLIST(SERVAUTH) REFRESH                             

  PE IZUDFLT.com.ibm.ws.management.security.resource.* -             
       CLASS(EJBROLE) ID(IZUUSER) ACC(READ)                          
  PE IZUDFLT.com.ibm.ws.management.security.resource.* -             
       CLASS(EJBROLE) ID(IZUADMIN) ACC(READ)                         
  PE IZUDFLT.com.ibm.ws.management.security.resource.Administrator - 
       CLASS(EJBROLE) ID(IZUUSER) ACC(READ)                          
  PE IZUDFLT.com.ibm.ws.management.security.resource.Administrator - 
       CLASS(EJBROLE) ID(IZUADMIN) ACC(READ)                         
  SETROPTS RACLIST(EJBROLE) REFRESH                                  

   RDEFINE OPERCMDS mvs.mcsoper.srg1DCUF UACC(NONE)            
   PERMIT mvs.mcsoper.srg1DCUF CLASS(OPERCMDS) ACCESS(read) +  
       ID(sysprg1)                                             
  SETROPTS RACLIST(OPERCMDS) REFRESH                           

<https://www.ibm.com/support/pages/apar/OA58786>

    RDEFINE TSOAUTH CONOPER UACC(NONE) OWNER(SYS1)          
  PERMIT CONOPER CLASS(TSOAUTH) ID(SYSPRG1) ACCESS(READ)  
  SETROPTS RACLIST(TSOAUTH) REFRESH                       

Problem:
CFZ12530E: Cannot switch to user IZUSVR because a SAF authorization 
error occurred. For the reason, see the SAF RACROUTE EXTRACT service
reason code 0x0BE80820.                                             

Solution:
 PERMIT CFZAPPL  CLASS(APPL) ID(IZUSVR) ACCESS(READ)   
 SETROPTS RACLIST(APPL) REFRESH                        

---
  PE MVSADMIN.WLM.POLICY CLASS(FACILITY) ID(SYSPRG1) ACC(UPDATE) 
  SETROPTS RACLIST(FACILITY) REFRESH                             

---
CFZ12530E: Cannot switch to user SYSPRG1 because a SAF authorization
error occurred. For the reason, see the SAF RACROUTE EXTRACT service
reason code 0x0BE80820.                                             

 PERMIT CFZAPPL  CLASS(APPL) ID(SYSPRG1) ACCESS(READ)  
 SETROPTS RACLIST(APPL) REFRESH                        

----












