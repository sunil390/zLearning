# TK5 MVS 3.8J Experiment - 22nd Feb 2026 
https://www.prince-webdesign.nl/images/downloads/TK5-Introduction-and-User-Manual.pdf

## Setup TK5 and MVSMF
1. Download TK5 Update 5 from https://www.prince-webdesign.nl/index.php/software/mvs-3-8j-turnkey-5
2. Unzip the folder and double click on mvs.bat
3. connect to console http://localhost:8038/
4. Start HTTPD by /S HTTPD
5. Loging using 3270 emulator connecting to 127.0.0.1 port 3270
6. user HERC01 password CUL8TR
7. download mvsmf.load.xmit from https://github.com/mvslovers/mvsmf/releases/download/current/mvsmf.load.xmit
8. From ISPF option 6 upload to HERC01.MVSMF.LOAD (Change Binary option to F and 80 and Save)
9. RECEIVE INDA('HERC01.MVSMF.LOAD(MVSMF)')
10. Using Option 3.3 copy MVSMF to HTTPD.LINKLIB
11. edit SYS2.SYSINLIB(HTTPCONF) to add cgi.MVSMF="/zosmf/*"
12. From Console P HTTPD and S HTTPD
13. Install zowe explorer extention in VSCode
14. Install nodejs
15. install zowe CLI, npm install -g @zowe/cli@zowe-v3-lts
16. Init Config, zowe config init --global-config
17. Update zosmfprofile to add protocol http and rejectUnauthorized parameters
```json
        "zosmf": {
            "type": "zosmf",
            "properties": {
                "port": 8080,
                "protocol": "http",
                "rejectUnauthorized": false
            },
            "secure": []
        },
```
18. Now List datasets and jobs from zowe panel in VSCode!
19. /f bsppilot,shutnow to shutdown TK5 or issue SHUTDOWN from READY Prompt.

## Enable IBM Z Open Editor MCP and Chat from VSCode Github Copilot.

1. Install IBM Z Open Editor Extention
2. Install IBM Semeru JDK 21 LTS if not already installed.
3. Open Settings Ctrl + ,
4. Search for zopeneditor.mcp.enabled - Enable it
5. Add .vscode/mcp.json in the repo
```json
{
  "servers": {
    "zopeneditor-sample": { "url": "http://localhost:3005/mcp" }
  }
}
```
5. Start the mcp server from Extentions - MCP SERVERS - INSTALLED section.
6. Open VSCode Chat and ask about Datasets and Jobs !

