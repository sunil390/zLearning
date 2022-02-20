# Commands

## ssh to POD and Container

1. k get pods --all-namespaces -o wide
2. k exec --stdin --tty awx-zdino-75549ccf9b-zj76j -- /bin/bash
```
 "redis" out of: redis, awx-zdino-web, awx-zdino-task, awx-zdino-ee
```
3. k exec -i -t awx-zdino-75549ccf9b-zj76j --container awx-zdino-ee -- /bin/bash
