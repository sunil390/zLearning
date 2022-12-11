## Registry 

## quay.io 

```
sudo dnf install podman-docker

[sunil390@sunil390 ~]$ docker login quay.io
Emulate Docker CLI using podman. Create /etc/containers/nodocker to quiet msg.
Username: sunil390
Password:
Login Succeeded!

[sunil390@sunil390 ~]$ docker run busybox echo "fun" > newfile
Emulate Docker CLI using podman. Create /etc/containers/nodocker to quiet msg.
Resolved "busybox" as an alias (/etc/containers/registries.conf.d/000-shortnames.conf)
Trying to pull docker.io/library/busybox:latest...
Getting image source signatures
Copying blob 45a0cdc5c8d3 done
Copying config 334e4a014c done
Writing manifest to image destination
Storing signatures


[sunil390@sunil390 ~]$ docker ps -l
Emulate Docker CLI using podman. Create /etc/containers/nodocker to quiet msg.
CONTAINER ID  IMAGE                             COMMAND     CREATED             STATUS                         PORTS       NAMES
e7b9f1162b43  docker.io/library/busybox:latest  echo fun    About a minute ago  Exited (0) About a minute ago              gallant_mahavira

[sunil390@sunil390 ~]$ docker commit e7b9f1162b43 quay.io/sunil390/myfirstrepo
Emulate Docker CLI using podman. Create /etc/containers/nodocker to quiet msg.
Getting image source signatures
Copying blob 98004ed6104b skipped: already exists
Copying blob 137731b1663c done
Copying config 7164a0b4b7 done
Writing manifest to image destination
Storing signatures
7164a0b4b798dc4a13f39459e2fea695f786c3e6442f79bffe09134b267566a0

[sunil390@sunil390 ~]$ docker push quay.io/sunil390/myfirstrepo
Emulate Docker CLI using podman. Create /etc/containers/nodocker to quiet msg.
Getting image source signatures
Copying blob 98004ed6104b done
Copying blob 137731b1663c done
Copying config 7164a0b4b7 done
Writing manifest to image destination
Storing signatures
```
