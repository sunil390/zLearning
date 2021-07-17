
# CIM

<https://www.ibm.com/docs/en/zos/2.4.0?topic=setup-quick-guide-cim-server-verification>

1. Set up the security for the CIM server
CFZSEC from the installation SAMPLIB - Done

2. Customize the file systems and directories used by the CIM server

CFZRCUST from the installation SAMPLIB

```jcl
/etc/wbem

PEGASUS_HOME=/usr/lpp/wbem
LIBPATH=/usr/lpp/wbem/lib:/usr/lpp/wbem/provider:/usr/lib
_CEE_RUNOPTS=FILETAG(AUTOCVT,AUTOTAG) STACK(32K,32K,ANYWHERE,KEEP,96K,32K) THREADSTACK(ON,128K,64K,ANYWHERE,KEEP,96K,32K) HEAP(32M,8M,ANYWHERE,KEEP,8K,4K) ANYHEAP(7M,1M,ANYWHERE,FREE) HEAPP(ALIGN,8,1,16,3,32,6,56,8,80,5,248,5,2064,13,4104,27,8208,4,16392,1,32784,2,65536,10) TERMTHDACT(UADUMP) DYN(*USERID,DYNAMIC,TDUMP)
_BPX_SHAREAS=NO
_BPXK_AUTOCVT=ON
_TAG_REDIR_ERR=TXT
_TAG_REDIR_IN=TXT
_TAG_REDIR_OUT=TXT
_BPXK_GPSENT_SECURITY=THREAD
#OSBASE_TRACE=0
#OSBASE_TRACE_FILE=/tmp/wbemosbase.trc
#RMF_CIM_HOST=127.0.0.1
#RMF_CIM_PORT=8803
#RMF_CIM_TRACE=0
#RMF_CIM_TRACE_FILE=/tmp/wbemosmonitoring.trc
```

3.BPXPRMDF

```jcl
MOUNT FILESYSTEM('SYS1.OMVS.SCFZZFS.&ZSOM1')  
 MOUNTPOINT('/var/wbem')
 TYPE(ZFS) MODE(RDWR)
```

4.Use the default TCP/IP ports 5988 and 5989

5.Start the CIM server (once per z/OS system).

Copy the CFZCIM started task procedure from the installation PROCLIB

```rexx
START CFZCIM
  
RDEFINE FACILITY BPX.POE UACC(NONE)
PERMIT BPX.POE CLASS(FACILITY) ID(CFZSRVGP) ACCESS(UPDATE)
PERMIT CIMSERV CLASS(WBEM) ID(IZUADMIN) ACCESS(UPDATE)
SETROPTS RACLIST(WBEM) REFRESH
SETROPTS RACLIST(FACILITY) REFRESH

CFZ12530E: Cannot switch to user IZUSVR because a SAF authorization
error occurred. For the reason, see the SAF RACROUTE EXTRACT service
reason code 0x0BE80820.

RDEFINE APPL OMVSAPPL    UACC(NONE)
PERMIT OMVSAPPL CLASS(APPL) ID(IZUADMIN) ACCESS(READ)
SETROPTS RACLIST(APPL) REFRESH

PERMIT OMVSAPPL CLASS(APPL) ID(CFZSRVGP) ACCESS(READ)
SETROPTS RACLIST(APPL) REFRESH
```

Problem:
CFZ12530E: Cannot switch to user IZUSVR because a SAF authorization 
error occurred. For the reason, see the SAF RACROUTE EXTRACT service
reason code 0x0BE80820.                                             

Solution:
 PERMIT CFZAPPL  CLASS(APPL) ID(IZUSVR) ACCESS(READ)   
 SETROPTS RACLIST(APPL) REFRESH                        

---
CFZ12530E: Cannot switch to user SYSPRG1 because a SAF authorization
error occurred. For the reason, see the SAF RACROUTE EXTRACT service
reason code 0x0BE80820.                                             

 PERMIT CFZAPPL  CLASS(APPL) ID(SYSPRG1) ACCESS(READ)  
 SETROPTS RACLIST(APPL) REFRESH                        

