# Alma Linux 10

## Almalinux 9.6 to 10.x upgrade

1. cat /etc/os-release
2. sudo curl -o /etc/yum.repos.d/elevate-ng.repo https://repo.almalinux.org/elevate/testing/elevate-ng-el$(rpm -E %rhel).repo
3. sudo rpm --import https://repo.almalinux.org/elevate/RPM-GPG-KEY-ELevate
4. sudo yum install -y leapp-upgrade leapp-data-almalinux
5. sudo leapp preupgrade
6. sudo sh -c "ln -snf var/lib/snapd/snap /snap"
7. sudo leapp preupgrade
8. sudo leapp upgrade
