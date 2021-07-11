# abc

C:\Users\A463336>zowe  profiles create zosmf-profile zNitro --host 192.168.2.44 --port 443 --user sysprg1 --password password --reject-unauthorized false
Profile created successfully! Path:
C:\Users\A463336\.zowe\profiles\zosmf\zNitro.yaml

host:               192.168.2.44
port:               443
user:               sysprg1
password:           password
rejectUnauthorized: false

Review the created profile and edit if necessary using the profile update command.

C:\Users\A463336>zowe  zos-jobs list jobs --zosmf-profile znitro
JOB03096 CC 0000    CFZIVP1 OUTPUT
TSU03030 ABEND S222 SYSPRG1 OUTPUT
TSU03029 ABEND S222 SYSPRG1 OUTPUT
TSU03027 ABEND S222 SYSPRG1 OUTPUT
TSU03026 JCL ERROR  SYSPRG1 OUTPUT
TSU03100            SYSPRG1 ACTIVE
TSU03099            SYSPRG1 ACTIVE
TSU03095            SYSPRG1 ACTIVE

