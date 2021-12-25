# Kubernetes Tips and Tricks

## Swap Disable in Linux

1. sudo swapoff -A
2. swapon -show
3. sudo nano /etc/fstab

## apt cheatsheet

1. sudo apt-mark app1 app2
2. apt search app1

## Notes...

1. Spec is declarative way of sepcifying desired object state.
2. Labels
    - to organise and select sub sets of objects
    - Match Labels - Label selector allows clients and users to identify a set of objects (core grouping primitive within k8s)
    - Quality based label - 
    - Set based label -  

3. Linux NameSpaces and Cgroups
4. Pods Can have
    - Init Containers - Run during startup and complete before any app container startup.
    - App containers
    - Ephemeral containers - debugging
5. Workload resources manages creation and management of multiple pods
6. Controller handles rollout replication and automatic healing.
7. Workload resources - Deployments , Jobs and daemon sets.
8. kubectl api-resources
9. shell access in pod kubectl exec podname -n namespace -it -- /bin/sh

