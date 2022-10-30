
```
After seeing the posts this week about ISRONLY in ISP.SISPSAMP, I am
trying to write a SMPE usermod that will:
1) Copy/move ISRONLY from SISPSAMP to SISPEXEC
2) Add alias "ONLY" to it.

Does anyone have any samples/pointers on how to do this?

Thanks in advance,

Dave

Mark Zelden


Perhaps Kurt Quackenbush (or someone else) would have a better way
or "more proper" way to do it, but I think this should work:

++USERMOD (UMISPMZ) .
++VER (Z038) FMID(HIF5H02) .
++EXEC(ISRONLY) DISTLIB(AISPEXEC) ALIAS(ONLY)
SYSLIB(SISPEXEC) TXLIB(SISPSAMP).
++JCLIN.
//STEP1 EXEC PGM=IEBCOPY
//SISPSAMP DD DSN=SISPSAMP,DISP=SHR
//SISPEXEC DD DSN=SISPEXEC,DISP=SHR
//SYSIN DD *
COPY INDD=SISPSAMP,OUTDD=SISPEXEC TYPE=DATA
SELECT MEMBER=ISRONLY
SELECT MEMBER=ONLY ALIAS OF ISRONLY
/*


Regards,

Mark

Kurt Quackenbush

I was out of the office for a couple of days, so I'm a little late, but
here's my 2 cents: The above USERMOD should indeed work, except you can
scrap the JCLIN since it has no affect and is ignored by SMP/E. That
is, all "TYPE=DATA" copy steps are ignored.

Kurt Quackenbush -- IBM, SMP/E Development

Mark Zelden


jeff...@gmail.com
unread,
Jul 3, 2009, 6:19:22 AM
to
Yes, but this strikes me as incomplete.
I did try an APPLY CHECK of the proposed USERMOD (minus the JCLIN) and
it appeared to produce the desired result.
In that a ++EXEC element would be created (target library SISPEXEC) with
an ALIAS of ONLY copied from SISPSAMP.

However, here's the problem. The shipped IBM element ++SAMP(ISRONLY) has
no updates associated with it.
This is telling me, and I could be wrong, that IBM could ship a PTF to
ISRONLY, and then my ++EXEC is
out-of-sync because IBM knows nothing of a ++EXEC(ISRONLY). Uh Oh

It seems to me that a complete solution to this problem requires that
the ++SAMP(ISRONLY) must have the RMID updated.
That way, if there is an IBM PTF, then SMP/E will detect a MODID error.

--
Jeff


Mark Zelden said the following on 7/1/2009 12:58 PM:

Paul Gilmartin

I believe (but I'm uncertain) the following:

o You should apply the USERMOD to SAMP(ISRONLY). This
sets the RMID of ISRONLY to UMISPMZ so the MODID
check will happen because the IBM PTF presumably does
not acknowledge UMISPMZ.

o On a subsequent PTF to ISRONLY, SMP/E will ask that
the USERMOD be RESTORED, then re-APPLYed.

o I don't know how effectively to change the SYSLIB.

-- gil

Skip Robinson

unread,
Jul 3, 2009, 10:28:55 AM
to
I agree with Gil that by far the most important effect of a usermod based
on an IBM-supplied element to force a 'modid error' in case the original
element is ever hit by a PTF. There may be multiple ways to get the user
element installed as desired in a single step. Whatever. Here's an example
of how we implement a sample source into production. The key is to set the
RMID via UCLIN. The rest is fluff.
//SYSIN DD *
SET BDY(GLOBAL) .
RECEIVE SYSMODS S(CONS001) .
SET BDY(MVST100) .
APPLY S(CONS001) REDO .
UCLIN .
REP SAMP(IEECMDPF) RMID(CONS001) .
ENDUCL .
//SMPPTFIN DD DATA,DLM=$$
++USERMOD(CONS001) REWORK(2007197)
/* This usermod assembles and links SAMPLIB member
IEECMDPF, which allows one to direct console
commands via SYSID prefix rather than ROUTE.
No changes are made to the sample, but UCLIN
sets the RMID in case a future PTF requires the
member to be reassembled.
*/ .
++VER(Z038) FMID(HBB7740) /* ZOS R19 */ .
++ JCLIN .
//ASM EXEC PGM=IEV90,PARM='DECK,NOOBJ,XREF(SHORT)'
//SYSIN DD DDNAME=SAMPLIB
//SAMPLIB DD DSN=SYS1.SAMPLIB(IEECMDPF),DISP=SHR
//SYSPUNCH DD DSN=SYS1.SYSPUNCH(IEECMDPF),DISP=SHR
//LINKEDIT EXEC PGM=IEWL,PARM='XREF,LIST,LET,NCAL,AC=1'
//SYSLMOD DD DSN=SYS1.LINKLIB,DISP=SHR
//SYSPUNCH DD DSN=SYS1.SYSPUNCH,DISP=SHR
//SYSLIN DD *
INCLUDE SYSPUNCH(IEECMDPF)
NAME IEECMDPF(R)
++SRC(IEECMDPF) DISTLIB(ASLIB01) TXLIB(SAMPLIB) .
$$

.
.
JO.Skip Robinson
Southern California Edison Company
Electric Dragon Team Paddler
SHARE MVS Program Co-Manager
626-302-7535 Office
323-715-0595 Mobile
JO.Skip....@sce.com




You are correct. But that isn't part of the USERMOD MCS in this case, it
would be done with UCLIN via SMPCNTL input. See the archives for past
examples of doing this when assembling sample source.

But for completeness in this thread, here is what it would look like (leaving
out the JCLIN per Kurt):


//SMPPTFIN DD DATA,DLM=$$

++USERMOD (UMISPMZ) .
++VER (Z038) FMID(HIF5H02) .
++EXEC(ISRONLY) DISTLIB(AISPEXEC) ALIAS(ONLY)
SYSLIB(SISPEXEC) TXLIB(SISPSAMP).

$$
//SMPCNTL DD *
SET BOUNDARY (tgt_zone) .
APPLY
SELECT (UMISPMZ).
UCLIN .
REP SAMP(ISRONLY) RMID(UMISPMZ).
ENDUCL.
/*


--
Mark Zelden

Schwarz, Barry A

to
Whenever I have to use an IBM module in a library other than where IBM
put it (++SAMP is just one example), I copy it to a private TXLIB,
modify it if necessary, and then create a USERMOD with both the original
data element type (e.g., ++SAMP) and the desired element type (e.g.,
++EXEC), both using the original name of the module and both referencing
the TXLIB. The desired element type also references the correct SYSLIB
where I want the module to end up. If the original element type is
correct but doesn't support the ++MOVE statement, then I use ++USER1.
The end result is both the original IBM element and my usable copy are
both flagged with the USERMOD which generates the appropriate SMPE
diagnostic if I ever attempt to apply an IBM update.

-----Original Message-----
From: Jeffery Swagger
Sent: Thursday, July 02, 2009 5:48 PM
To: IBM-...@bama.ua.edu
Subject: Re: SMPE usermod sample

Yes, but this strikes me as incomplete.

I did try an APPLY CHECK of the proposed USERMOD (minus the JCLIN) and
it appeared to produce the desired result.
In that a ++EXEC element would be created (target library SISPEXEC) with
an ALIAS of ONLY copied from SISPSAMP.

However, here's the problem. The shipped IBM element ++SAMP(ISRONLY) has
no updates associated with it.
This is telling me, and I could be wrong, that IBM could ship a PTF to
ISRONLY, and then my ++EXEC is
out-of-sync because IBM knows nothing of a ++EXEC(ISRONLY). Uh Oh

It seems to me that a complete solution to this problem requires that
the ++SAMP(ISRONLY) must have the RMID updated.
That way, if there is an IBM PTF, then SMP/E will detect a MODID error.

----------------------------------------------------------------------

tl...@uchicago.edu's profile photo
tl...@uchicago.edu
unread,
Jul 8, 2009, 7:32:50 PM
to
I have a similar SMPE usermod question... I need to add an alias to
FTP (called Z062016). In the past I have relinked the module outside
of SMPE and then updated SMPE using a usermod. It isn't very clean
and it causes modid problems when I apply new TCPIP maintenance. I'm
wondering if someone can show me the correct way. This is what I
have done in the past...
//LINK EXEC PGM=IEWBLINK,PARM=('OPTIONS(GENOPTS)')
//STEPLIB DD DSN=ZOS10.SYS1.MIGLIB,DISP=SHR
//GENOPTS DD *
RENT,REUS,AC=1,AMODE=31,RMODE=ANY,CASE(MIXED)
DYNAM(DLL),CALL
//INPUT DD DSN=ZOS10.SYS1.TCPIP.SEZALOAD,DISP=SHR
//SYSLMOD DD DSN=ZOS10.SYS1.TCPIP.SEZALOAD,DISP=SHR
//SYSLIB DD DSN=ZOS10.SYS1.CEE.SCEEOBJ,DISP=SHR
// DD DSN=ZOS10.SYS1.CEE.SCEELKEX,DISP=SHR
// DD DSN=ZOS10.SYS1.CEE.SCEELKED,DISP=SHR
// DD DSN=ZOS10.SYS1.CSSLIB,DISP=SHR
// DD DSN=ZOS10.SYS1.EUVF.SEUVFLIB,DISP=SHR
//SIEASID DD DSN=ZOS10.SYS1.SIEASID,DISP=SHR
//AEZAMODS DD DSN=ZOS10.SYS1.TCPIP.AEZAMODS,DISP=SHR
//SGSKHFS DD PATH='/Service/usr/lpp/gskssl/IBM/'
//SYSPRINT DD SYSOUT=*
//SYSLIN DD *
ORDER EZBOECPR
ORDER EZAFTPMG
ENTRY CEESTART
ALIAS FTP(CEESTART)
INCLUDE SIEASID(EUVFKDLL) TYPE=UTIN
INCLUDE SIEASID(EUVFKDLP) TYPE=UTIN
INCLUDE AEZAMODS(EZAAE061) FMID=HIP61A0
.....
INCLUDE AEZAMODS(EZBWTODM) FMID=HIP61A0
INCLUDE SGSKHFS(GSKAH011) TYPE=UTIN
INCLUDE SGSKHFS(GSKAH041) TYPE=UTIN
ALIAS Z062016,FTP
NAME EZAFTPLC(R)


//SMPE EXEC PGM=GIMSMP,REGION=0M
//STEPLIB DD DSN=ZOS10.SYS1.MIGLIB,DISP=SHR
//SMPCSI DD DSN=ZOS10.SMPE.GLOBAL.CSI,DISP=SHR
//SMPHOLD DD DUMMY
//SMPPTFIN DD DATA,DLM=@@
++USERMOD (TCPMD01).
++VER (Z038) FMID (HIP61A0).
++JCLIN.
//LINK0039 EXEC PGM=IEWBLINK,PARM=('OPTIONS(GENOPTS)')
//GENOPTS DD *
RENT,REUS,AMODE=31,RMODE=ANY,CASE(MIXED)
DYNAM(DLL),CALL
//SYSLMOD DD DSN=SEZALOAD
//SYSLIB DD DSN=SCEEOBJ
// DD DSN=SCEELKEX
// DD DSN=SCEELKED
// DD DSN=CSSLIB
// DD DSN=SEUVFLIB
//SYSLIN DD *
ORDER EZBOECPR
ORDER EZAFTPMG
ENTRY CEESTART
ALIAS FTP(CEESTART)
INCLUDE SIEASID(EUVFKDLL) TYPE=UTIN
INCLUDE SIEASID(EUVFKDLP) TYPE=UTIN
INCLUDE AEZAMODS(EZAAE061) FMID=HIP61A0
...
INCLUDE AEZAMODS(EZBWTODM) FMID=HIP61A0
INCLUDE SGSKHFS(GSKAH011) TYPE=UTIN
INCLUDE SGSKHFS(GSKAH041) TYPE=UTIN
ALIAS Z062016,FTP
NAME EZAFTPLC(R)
@@
//SMPCNTL DD *
SET BDY(GLOBAL).
RECEIVE S(TCPMD01) LIST .
SET BDY(MVST100).
APPLY S(
TCPMD01
).

Thanks,

Todd Last
MVS Systems Programmer
University of Chicago
tl...@uchicago.edu

Todd Last's profile photo
Todd Last
unread,
Jul 8, 2009, 8:06:46 PM
to

Thanks,

----------------------------------------------------------------------

Jousma, David's profile photo
Jousma, David
unread,
Jul 8, 2009, 8:20:50 PM
to
We do something similar for IEBCOPY. We add FTBIEBC as an alias. Not
sure it is the most efficient or best way, but it works:

//STEP005 EXEC SMPE,CSI=SMPE.ZOS110.GLOBAL.CSI
//SMPOUT DD SYSOUT=*
//SYSIN DD *
SET BDY (GLOBAL).
REJECT S(MSYS012) BYPASS(APPLYCHECK).
RECEIVE SYSMODS.
SET BDY (MVSTZN).
RESTORE S(MSYS012) .
APPLY SELECT(MSYS012).
/*
//SMPPTFIN DD DATA,DLM=ZZ
++USERMOD (MSYS012)
/* ADD ALIAS FTBIEBC TO IEBCOPY
*/.
++VER (Z038) FMID(HDZ1A10) .
++MOD(IEBCOPY) LKLIB(LINKLIB).
++ JCLIN.
//S1 EXEC LINKS,PARM='LET,LIST,MAP,NCAL',NAME=LINKLIB
//SYSLIN DD *
INCLUDE LINKLIB(IEBCOPY)
ORDER IEBCOMCA(P),IEBCOMCB(P) COMMON AREA
ORDER IEBDSCPY(P)
ORDER IEBESTIN
ORDER IEBESTAB
ORDER SNAPDCB,IEBDSCP2
ORDER IEBDSBAM,IEBDSPRM,IEBDSCLK
ORDER IEBCFAMS,IEBCFIOX
ORDER IEBCPMOD
ORDER IEBCRDC
ORDER IEBDRB
ORDER IEBDRD
ORDER IEBDSU
ORDER IEBDSWCP
ORDER IEBDV0,IEBDVD$C,IEBDVSQ
ORDER IEBDWR
ORDER IEBMCM
ORDER IEBRSAM
ORDER IEBSCN
ORDER IEBVCT
ORDER IEBVDM
ORDER IEBVTM
ORDER IEBVTT
ORDER IEBWSAM
ORDER IEBWSU
ORDER IEBIOE
ORDER IEBCMSG,IEBCMSG1
ORDER IEBCNVT
ORDER IEBPRINT
ORDER IGG019S9(P)
ORDER IGG019C9(P)
SETCODE AC(1)
MODE AMODE(24),RMODE(24)
ENTRY IEBDSCPY
ALIAS IEBDSCPY
ALIAS FTBIEBC
NAME IEBCOPY(R)
/*
ZZ
//

_________________________________________________________________
Dave Jousma
Assistant Vice President, Mainframe Services
david....@53.com
1830 East Paris, Grand Rapids, MI 49546 MD RSCB1G
p 616.653.8429
f 616.653.8497


-----Original Message-----
From: IBM Mainframe Discussion List [mailto:IBM-...@bama.ua.edu] On

Behalf Of Todd Last
Sent: Wednesday, July 08, 2009 10:36 AM
To: IBM-...@bama.ua.edu
Subject: Re: SMPE usermod sample

I have a similar SMPE usermod question... I need to add an alias to
FTP (called Z062016). In the past I have relinked the module outside
of SMPE and then updated SMPE using a usermod. It isn't very clean
and it causes modid problems when I apply new TCPIP maintenance. I'm
wondering if someone can show me the correct way. This is what I
have done in the past...

This e-mail transmission contains information that is confidential and may be privileged. It is intended only for the addressee(s) named above. If you receive this e-mail in error, please do not read, copy or disseminate it in any manner. If you are not the intended recipient, any disclosure, copying, distribution or use of the contents of this information is prohibited. Please reply to the message immediately by informing the sender that the message was misdirected. After replying, please erase it from your computer system. Your assistance in correcting this error is appreciated.

----------------------------------------------------------------------

Todd Last's profile photo
Todd Last
unread,
Jul 8, 2009, 10:56:54 PM
to
Based on David's reply, it looks like I forgot a ++MOD entry in my usermod. In
the next couple of days, I'll try redoing this usermod and not reassemble the
module outside of SMPE. Thanks Dave!
Todd

Todd Last's profile photo
Todd Last
unread,
Jul 10, 2009, 12:58:38 AM
to
I'm stumped... I've been working on this for hours and I'm not coding
something correctly. As I mentioned previously, I just need to create an alias
for EZAFTPLC...
//SMPPTFIN DD DATA,DLM=@@
++USERMOD (TCPMD01).
++VER (Z038) FMID (HIP61A0).

++MOD(EZAFTPLC) LKLIB(SEZALOAD) DISTLIB(AEZAMODS).


++JCLIN.
//LINK0039 EXEC PGM=IEWBLINK,PARM=('OPTIONS(GENOPTS)')
//GENOPTS DD *

RENT,REUS,AC=1,AMODE=31,RMODE=ANY,CASE(MIXED)
DYNAM(DLL),CALL
//SYSLMOD DD DSN=SEZALOAD
//SYSDEFSD DD DSN=SMPDUMMY


//SYSLIB DD DSN=SCEEOBJ
// DD DSN=SCEELKEX
// DD DSN=SCEELKED
// DD DSN=CSSLIB
// DD DSN=SEUVFLIB
//SYSLIN DD *
ORDER EZBOECPR
ORDER EZAFTPMG
ENTRY CEESTART
ALIAS FTP(CEESTART)
INCLUDE SIEASID(EUVFKDLL) TYPE=UTIN
INCLUDE SIEASID(EUVFKDLP) TYPE=UTIN

INCLUDE SGSKHFS(GSKAH011) TYPE=UTIN
INCLUDE SGSKHFS(GSKAH041) TYPE=UTIN

INCLUDE AEZAMODS(EZAAE061) FMID=HIP61A0
...
INCLUDE AEZAMODS(EZBWTODM) FMID=HIP61A0

ALIAS Z062016,FTP
NAME EZAFTPLC(R)
@@
//SMPCNTL DD *
SET BDY(GLOBAL).
RECEIVE S(TCPMD01) LIST .
SET BDY(MVST100).
APPLY S(
TCPMD01
)

CHECK.
//

I get this weird message when I run the above to create my alias:
GIM43401W MODULE EZAFTPLC IN SYSMOD TCPMD01 WAS NOT INSTALLED
IN ANY TARGET LIBRARY.

Does anyone have a clue on what I'm coding wrong?

Jousma, David's profile photo
Jousma, David
unread,
Jul 10, 2009, 1:09:47 AM
to
Not sure it matters, but separate your two aliases into separate lines.
_________________________________________________________________
Dave Jousma
Assistant Vice President, Mainframe Services
david....@53.com
1830 East Paris, Grand Rapids, MI 49546 MD RSCB1G
p 616.653.8429
f 616.653.8497


-----Original Message-----
From: IBM Mainframe Discussion List [mailto:IBM-...@bama.ua.edu] On
Behalf Of Todd Last
Sent: Thursday, July 09, 2009 3:28 PM
To: IBM-...@bama.ua.edu
Subject: Re: SMPE usermod sample

This e-mail transmission contains information that is confidential and may be privileged. It is intended only for the addressee(s) named above. If you receive this e-mail in error, please do not read, copy or disseminate it in any manner. If you are not the intended recipient, any disclosure, copying, distribution or use of the contents of this information is prohibited. Please reply to the message immediately by informing the sender that the message was misdirected. After replying, please erase it from your computer system. Your assistance in correcting this error is appreciated.

----------------------------------------------------------------------

jeff...@gmail.com's profile photo
jeff...@gmail.com
unread,
Jul 10, 2009, 6:11:41 AM
to
Yes, this is essentially what I do too.
The problem I have with changing the RMID via UCLIN approach is that you
have to (I believe) undo it via UCLIN at RESTORE time. I prefer not to
have to that.

As an aside, the thing I do in cases like this is to replace the SAMP
with something like this:

++ SAMP(ISRONLY)
*******************************************
* See USERMOD xxxxxxx *
*******************************************

This both updates the RMID so I get MODID error if IBM updates the SAMP
and provides some doc if somebody is looking at the SAMP library.

And it's not my idea. It's something, like so many things I do, that got
posted on this list ???? years ago. I have no shame when it come to
using the ideas of the more knowledgeable people on this list. :-)

--
Jeff


Schwarz, Barry A said the following on 7/6/2009 3:37 PM:

Binyamin Dissen's profile photo
Binyamin Dissen
unread,
Jul 10, 2009, 12:14:09 PM
to
On Thu, 9 Jul 2009 20:40:11 -0400 Jeffery Swagger <jef...@COMCAST.NET> wrote:
:>Yes, this is essentially what I do too.

:>The problem I have with changing the RMID via UCLIN approach is that you
:>have to (I believe) undo it via UCLIN at RESTORE time. I prefer not to
:>have to that.

You prefer a RESTORE over a UCLIN? Why?

Also, you can BYPASS(ID) to avoid the need for either.

--
Binyamin Dissen <bdi...@dissensoftware.com>
http://www.dissensoftware.com

Director, Dissen Software, Bar & Grill - Israel


Should you use the mailblocks package and expect a response from me,
you should preauthorize the dissensoftware.com domain.

I very rarely bother responding to challenge/response systems,
especially those from irresponsible companies.

Kurt Quackenbush's profile photo
Kurt Quackenbush
unread,
Jul 10, 2009, 8:06:35 PM
to
Yup. Your ++MOD is for EZAFTPLC, yet a module by that name is not
included in any load module... you need an INCLUDE statement for that
module in your JCLIN.

Kurt Quackenbush -- IBM, SMP/E Development

----------------------------------------------------------------------

Todd Last's profile photo
Todd Last
unread,
Jul 11, 2009, 1:16:32 AM
to
That worked. Thank you Kurt. I really appreciate it!
//SMPE EXEC,PGM=GIMSMP,REGION=0M,


//STEPLIB DD DSN=ZOS10.SYS1.MIGLIB,DISP=SHR
//SMPCSI DD DSN=ZOS10.SMPE.GLOBAL.CSI,DISP=SHR
//SMPHOLD DD DUMMY

//SMPPTFIN DD DATA,DLM=@@
++USERMOD (TCPMD01).
++VER (Z038) FMID (HIP61A0).

++MOD(EZAFTPLC) LKLIB(SEZALOAD).
++JCLIN.
//LINK0039 EXEC PGM=IEWBLINK,PARM=('OPTIONS
(GENOPTS)'),NAME=SEZALOAD


//GENOPTS DD *
RENT,REUS,AC=1,AMODE=31,RMODE=ANY,CASE(MIXED)
DYNAM(DLL),CALL
//SYSLMOD DD DSN=SEZALOAD
//SYSDEFSD DD DSN=SMPDUMMY
//SYSLIB DD DSN=SCEEOBJ
// DD DSN=SCEELKEX
// DD DSN=SCEELKED
// DD DSN=CSSLIB
// DD DSN=SEUVFLIB
//SYSLIN DD *

INCLUDE SIEASID(EUVFKDLL) TYPE=UTIN
INCLUDE SIEASID(EUVFKDLP) TYPE=UTIN
INCLUDE SGSKHFS(GSKAH011) TYPE=UTIN
INCLUDE SGSKHFS(GSKAH041) TYPE=UTIN

INCLUDE SEZALOAD(EZAFTPLC)


ORDER EZBOECPR
ORDER EZAFTPMG
ENTRY CEESTART
ALIAS FTP(CEESTART)

ALIAS Z062016


NAME EZAFTPLC(R)
@@
//SMPCNTL DD *
SET BDY(GLOBAL).
RECEIVE S(TCPMD01) LIST .
SET BDY(MVST100).
APPLY S(
TCPMD01

).
//

Todd Last
MVS Systems Programmer
University of Chicago
tl...@uchicago.edu

----------------------------------------------------------------------

Skip Robinson's profile photo
Skip Robinson
unread,
Jul 11, 2009, 3:45:57 AM
to
Someone else commented on the RESTORE question, but I'd like to expand on
it. In general, I see little reason ever to RESTORE a usermod. Yes, I know
the book says to do it, but it strikes me as extra work to arrive at the
same (intermediate) spot: code returned to its original, unmodified state.
With the right combination of REWORK and PRE values, you should seldom
(never?) need to REJECT or RESTORE a usermod.
For example, we maintain a ZAP usermod to an RMM table in order to mimic
behavior of a previous product around which countless production processes
have been built over the years. (Thanks to Monsignor Wood, that cross will
be lifted from our shoulders in R11 according to a new Health Check.)
Unfortunately the table moves around not only in new releases, but also
rather frequently by PTF. The same ZAP replacements work every time, but
almost always at a different offset. This usermod automatically gets its
name inserted as UMID in order to trigger a regression message whenever
that CSECT gets hit by a PTF. Hence no UCLIN is required. A few of points.

1. One 'unnatural' step is necessary at the start of each iteration: APPLY
SELECT the colliding PTF with BYPASS(ID). That's about the only time I ever
do such a thing.

2. In order to determine the new offset, we pretty much have to install the
PTF anyway before reworking the usermod.

3. By updating the REWORK value with the date of update, we don't need to
REJECT the usermod. As long as the new REWORK is higher (EBCDIC collating
sequence) than the old one, the usermod is re-received.

4. By updating the PRE values with the latest PTF, SMPE understands where
the usermod fits in the hierarchy, i.e. on top of all other sysmods.

Here's what the current usermod wrapper looks like.


//SMPCNTL DD *
SET BDY(GLOBAL) .
RECEIVE SYSMODS BYPASS(APPLYCHECK) .
SET BDY(MVST100) .
APPLY S(RMM0004) REDO .
//SMPPTFIN DD DATA
++USERMOD(RMM0004) REWORK(2009174 ) .
++VER (Z038)
FMID(HDZ1190)
PRE(
UA34754
UA39850
UA43733
UA90496
UA47393
) .
++ZAP(EDGVRECM) .
[rest of zap code goes here]

.
.
JO.Skip Robinson
Southern California Edison Company
Electric Dragon Team Paddler
SHARE MVS Program Co-Manager
626-302-7535 Office
323-715-0595 Mobile
JO.Skip....@sce.com



Jeffery Swagger
<jeffos2@COMCAST.
NET> To

Sent by: IBM IBM-...@bama.ua.edu
Mainframe cc
Discussion List
<IBM-...@bama.ua Subject
.edu> Re: SMPE usermod sample



07/09/2009 05:40

PM


Please respond to
IBM Mainframe
Discussion List
<IBM-...@bama.ua
.edu>


Yes, this is essentially what I do too.

The problem I have with changing the RMID via UCLIN approach is that you
have to (I believe) undo it via UCLIN at RESTORE time. I prefer not to
have to that.

As an aside, the thing I do in cases like this is to replace the SAMP
with something like this:

++ SAMP(ISRONLY)
*******************************************
* See USERMOD xxxxxxx *
*******************************************

This both updates the RMID so I get MODID error if IBM updates the SAMP
and provides some doc if somebody is looking at the SAMP library.

And it's not my idea. It's something, like so many things I do, that got
posted on this list ???? years ago. I have no shame when it come to
using the ideas of the more knowledgeable people on this list. :-)

--
Jeff
```
