# Alpine Linux


## Alpine Linux Install

1. Download extended x64 iso and boot in vm image
2. setup-alpine
3. vi /etc/apk/repositories and uncomment community
```
http://dl-cdn.alpinelinux.org/alpine/v3.17/main
http://dl-cdn.alpinelinux.org/alpine/v3.17/community
#http://dl-cdn.alpinelinux.org/alpine/edge/main
#http://dl-cdn.alpinelinux.org/alpine/edge/community
#http://dl-cdn.alpinelinux.org/alpine/edge/testing

http://dl-cdn.alpinelinux.org/alpine/edge/main
http://dl-cdn.alpinelinux.org/alpine/edge/community
#http://dl-cdn.alpinelinux.org/alpine/edge/testing
```
4. apk update
5. apk add sudo
6. echo '%wheel ALL=(ALL) ALL' > /etc/sudoers.d/wheel
7. adduser sunil390 wheel
8. sudo -lU sunil390
