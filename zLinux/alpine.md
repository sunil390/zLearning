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
9. Not required ( sudo apk add bash coreutils grep lsof less curl binutils dialog attr )
10. Not required ( sudo apk add git git-lfs gnupg sqlite sqlite openssl )
11. sudo apk add gitea
12. sudo service gitea start
13. sudo service gitea status
14. http://192.168.2.153:3000
