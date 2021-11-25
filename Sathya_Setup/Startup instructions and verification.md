# Startup instructions of softwares
---

1. Start zOS
2. Start linux on vm
3. start **node-red** on command prompt on windows (http://127.0.0.1:1880/)
4. once linux started, gitlab starts automatically and you can verify using http://192.168.1.24
5. start rundeck on linux **sudo service rundeckd start** using root it and verify ( http://192.168.1.24:4440/user/login)

## Start microk8s and awx access
---
1. Start zOS
2. Start mk8s ubuntu image on vm
3. Start microk8s start
4. Verify microk8s status --wait-ready
5. kubectl get --all-namespaces pods
6. kubectl get svc
7. On Windows Powershell ->  ssh -L 30551:localhost:30551 sathya@192.168.1.25
8. logon to awx http://localhost:30551/#/login
use sathya and gitlab
