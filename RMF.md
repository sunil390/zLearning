# RMF

```jcl
  AG OMVSGRP OMVS(GID(2)) OWNER(SYS1) supgroup(sys1)               
  ADDUSER RMF      DFLTGRP(omvsgrp) OMVS(UID(100) HOME('/'))       
  ADDUSER RMFGAT   DFLTGRP(omvsgrp) OMVS(UID(101) HOME('/'))       
  ADDUSER GPMSERVE DFLTGRP(omvsgrp) OMVS(UID(102) HOME('/'))       
  RDEFINE STARTED RMF.*      STDATA(USER(RMF)      TRUSTED(YES))   
  RDEFINE STARTED RMFGAT.*   STDATA(USER(RMFGAT)   TRUSTED(YES))   
  RDEFINE STARTED GPMSERVE.* STDATA(USER(GPMSERVE) TRUSTED(YES))   
  RDEFINE STARTED GPM4CIM.*  STDATA(USER(GPMSERVE) TRUSTED(YES))   
  SETROPTS RACLIST(STARTED) REFRESH                                
  PERMIT  BPX.WLMSERVER CLASS(FACILITY) ID(GPMSERVE) ACCESS(READ)  
```

```
MODIFY GPMSERVE,OPTIONS                  
+GPM061I OPTIONS IN EFFECT:              
+GPM061I  CACHESLOTS(4)                  
+GPM061I  SERVERHOST(*)                  
+GPM061I  DEBUG_LEVEL(0)                 
+GPM061I  HTTPS(ATTLS)                   
+GPM061I  CLIENT_CERT(NONE)              
+GPM061I  TIMEOUT(0)                     
+GPM061I  SESSION_PORT(8801)             
+GPM061I  MAXSESSIONS_INET(5)            
+GPM061I  HTTP_PORT(8803)                
+GPM061I  MAXSESSIONS_HTTP(20)           
+GPM061I  HTTP_ALLOW(*)                  
+GPM061I  HTTP_NOAUTH()                  
+GPM061I  DM_PORT(8802)                  
+GPM061I  DM_ACCEPTHOST(*)               
+GPM061I  MAXSESSIONS_UNIX(1)            
+GPM061I  UNIXSOCKET_PATH(/TMP/GPMSERVE) 

    SYS1.PARMLIB(GPMSRV00)
 ===>                     
/*************************
MAXSESSIONS_HTTP(20)      
HTTP_PORT(8803)           
HTTP_ALLOW(*)             
HTTP_NOAUTH(*)            
HTTPS(NO)

http://192.168.2.44:8803/

 PERMIT *.*     CLASS(FACILITY) ID(GPMSERVE) ACC(READ)    
 SETROPTS RACLIST(FACILITY) REFRESH                       
```

### Program Control

```jcl
  RALT PROGRAM * ADDMEM('SYS1.SERBLINK'/'******'/NOPADCHK) +  
                        UACC(READ)                            
  SETROPTS WHEN(PROGRAM) REFRESH                              
```
