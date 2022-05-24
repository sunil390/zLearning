# Commands

## Microk8s Kubeconfig

1. sudo microk8s kubectl config view --raw > $HOME/.kube/config

## ssh to POD and Container

1. k get pods --all-namespaces -o wide
2. k exec --stdin --tty awx-zdino-75549ccf9b-zj76j -- /bin/bash
```
 "redis" out of: redis, awx-zdino-web, awx-zdino-task, awx-zdino-ee
```
3. k exec -i -t awx-zdino-75549ccf9b-zj76j --container awx-zdino-ee -- /bin/bash

4. [List all containers](https://kubernetes.io/docs/tasks/access-application-cluster/list-all-running-container-images/)
```
Unique...
kubectl get pods --all-namespaces -o jsonpath="{.items[*].spec.containers[*].image}" |\
tr -s '[[:space:]]' '\n' |\
sort |\
uniq -c

by Pod...
kubectl get pods --all-namespaces -o jsonpath='{range .items[*]}{"\n"}{.metadata.name}{":\t"}{range .spec.containers[*]}{.image}{", "}{end}{end}' |\
sort



```
