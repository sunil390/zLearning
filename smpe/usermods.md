# UserMODs

## ZAP Usermod to add RSU Level 

1. [cvt mapping](https://www.ibm.com/docs/en/zos/2.4.0?topic=correlator-cvt-information)
2. [iplinfo](http://www.mzelden.com/mvsfiles/iplinfo.txt)
3. cvt mappings name display - rexx
```.py
/* REXX program to display the contents of the CVT Structure  */                 
cvt = c2d(Storage(10,4))                                                         
ecvt     = C2d(Storage(D2x(cvt + 140),4))  /* point to CVTECVT     */            
ecvtipa  = C2d(Storage(D2x(ecvt + 392),4)) /* point to IPA         */            
ipascat  = Storage(D2x(ecvtipa + 224),63)  /* SYSCAT  card image   */            
mcatdsn  = Strip(Substr(ipascat,11,44))    /* master catalog dsn   */            
mcatvol  = Substr(ipascat,1,6)             /* master catalog VOLSER*/            
prodname = Storage(D2x(CVT - 40),8)                                              
prodfmid = Storage(D2x(CVT - 32),8)                                              
cvtverid = Storage(D2x(CVT - 24),16)                                             
say 'z/OS CP =' prodname                                                         
say 'z/OS FMID =' prodfmid                                                       
say 'z/OS Cloning level =' cvtverid                                              
say 'z/OS mcat          =' mcatdsn                                               
say 'z/OS mcat volume   =' mcatvol                                               
Exit
```
4. UserMod to apply UserModification flags [xephone](https://www.cbttape.org/xephon/xephonm/mvs9908.pdf)



