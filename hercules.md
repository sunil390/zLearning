#Hecules

#Hercules helper

1. Download https://github.com/wrljet/hercules-helper-windows
2. Unzip to C:\helper-windows
3. Install ooRexx-5.0.0-12583.windows.x86_64.exe from hercules-helper\goodies
4. From adrmin terminal mode Set-ExecutionPolicy RemoteSigned ( Had to use Unrestricted)
5. cd c:\hercules-helper
6. .\hercules-buildall.ps1 -VS2017 -BuildDir c:\Z\hercules -Firewall

## Disk Compression

1. .\dasdcopy64 -r -o CCKD64 C:\Z\zOS2.5\ACS001.c C:\Z\zOS2.5\ACS001.z
