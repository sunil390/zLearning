# RPI and Microbit

## December 2025 Fun Project

# rpi and microbit setup

1. Installed nodered using single command installer.
```bash
zpi@pi:~ $ node-red-start

Start Node-RED

Once Node-RED has started, point a browser at http://192.168.2.251:1880
On Pi Node-RED works better with the Firefox or Chrome browser

Use   node-red-stop                          to stop Node-RED
Use   node-red-start                         to start Node-RED again
Use   node-red-log                           to view the recent log output
Use   sudo systemctl enable nodered.service  to autostart Node-RED at every boot
Use   sudo systemctl disable nodered.service to disable autostart on boot

To find more nodes and example flows - go to http://flows.nodered.org

Starting as a systemd service.
Started nodered.service - Node-RED graphical event wiring tool.
30 Nov 16:59:52 - [info]
Welcome to Node-RED
===================
30 Nov 16:59:52 - [info] Node-RED version: v4.1.1
30 Nov 16:59:52 - [info] Node.js  version: v18.20.8
30 Nov 16:59:52 - [info] Linux 6.12.47+rpt-rpi-v8 arm64 LE
30 Nov 16:59:53 - [info] Loading palette nodes
30 Nov 16:59:55 - [info] Settings file  : /home/sunil390/.node-red/settings.js
30 Nov 16:59:55 - [info] Context store  : 'default' [module=memory]
30 Nov 16:59:55 - [info] User directory : /home/sunil390/.node-red
30 Nov 16:59:55 - [info] Projects directory: /home/sunil390/.node-red/projects
30 Nov 16:59:55 - [info] Server now running at http://localhost:1880/
30 Nov 16:59:55 - [info] Active project : znodered
30 Nov 16:59:55 - [info] Flows file     : /home/sunil390/.node-red/projects/znodered/flows.json
30 Nov 16:59:55 - [warn] Using unencrypted credentials
30 Nov 16:59:55 - [info] Starting flows
30 Nov 16:59:55 - [info] [ui-base:My Dashboard] Node-RED Dashboard 2.0 (v1.22.1) started at /dashboard
30 Nov 16:59:55 - [info] [ui-base:My Dashboard] Created socket.io server bound to Node-RED port at path /dashboard/socket.io
30 Nov 16:59:55 - [info] Started flows
```
2. zpi@pi:~/node-scripts $ sudo chmod o+x /home/zpi
3. zpi@pi:~/node-scripts $ sudo chmod o+rx /home/zpi/node-scripts
4. zpi@pi:~/node-scripts $ sudo chmod 755 /home/zpi/node-scripts/send_text.py
6. zpi@pi:~/node-scripts $ sudo pip3 install bleak --break-system-packages

## Microbit Code

```js
// 2. Button A: Manual Stop / Reset
input.onButtonPressed(Button.A, function () {
    // Manually resetting ensures the board is fresh for the next test
    control.reset()
})
// --- Event Handlers ---
// 1. Bluetooth Data Receiver
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    // Read the incoming data
    incoming = bluetooth.uartReadUntil(serial.delimiters(Delimiters.NewLine))
    // Check for STOP command
    // Handle new text
    if (incoming.includes("[STOP]")) {
        // MEMORY NUCLEAR OPTION:
        // Resetting the board clears 100% of RAM.
        // This prevents the "Sad Face" accumulation over time.
        control.reset()
    } else if (incoming.length > 0) {
        // Explicitly clear old variable to help Garbage Collector
        currentMessage = ""
        // Assign new message
        currentMessage = incoming
        // Reset logic
        beepCount = 0
        isScrolling = true
    }
})
let isScrolling = false
let beepCount = 0
let currentMessage = ""
let incoming = ""
// --- Setup ---
bluetooth.startUartService()
basic.showIcon(IconNames.Yes)
// --- Main Loop ---
basic.forever(function () {
    if (isScrolling) {
        // A. Beep Logic (Only twice)
        if (beepCount < 2) {
            music.playTone(523, music.beat(BeatFraction.Eighth))
            basic.pause(100)
            beepCount += 1
        }
        // B. Display Text
        if (currentMessage.length > 0) {
            basic.showString(currentMessage)
        }
        // C. Memory Pause
        // Important: Clear screen and wait to let buffers empty
        basic.clearScreen()
        basic.pause(1000)
    } else {
        // D. Idle State
        // We only draw this if not scrolling
        basic.showIcon(IconNames.Yes)
        basic.pause(500)
    }
})
```

## rpi Code

zpi@pi:~/node-scripts $ cat check_props.py
```py
import asyncio
from bleak import BleakClient

ADDRESS = "C2:DB:C7:80:B7:14"

async def run():
    print(f"Connecting to {ADDRESS}...")
    async with BleakClient(ADDRESS) as client:
        print("Connected.")
        for service in client.services:
            for char in service.characteristics:
                if "6e400002" in char.uuid:
                    print(f"\nFOUND UART CHARACTERISTIC: {char.uuid}")
                    print(f"Properties: {char.properties}")

asyncio.run(run())
```
zpi@pi:~/node-scripts $ cat explore_services.py
```py
import asyncio
from bleak import BleakClient

# YOUR ADDRESS
address = "C2:DB:C7:80:B7:14"

async def run(address):
    print(f"Connecting to {address}...")
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")
        print("Listing Services...")
        for service in client.services:
            print(f"[Service] {service.uuid} ({service.description})")
            for char in service.characteristics:
                print(f"  - [Char] {char.uuid} ({char.description})")

asyncio.run(run(address))
```
zpi@pi:~/node-scripts $ cat find_write_uuid.py
```py
import asyncio
from bleak import BleakClient

ADDRESS = "C2:DB:C7:80:B7:14"
UART_SERVICE_UUID = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"

async def run():
    print(f"Connecting to {ADDRESS}...")
    async with BleakClient(ADDRESS) as client:
        print("Connected.")

        # Find the UART Service
        uart_service = None
        for s in client.services:
            if UART_SERVICE_UUID in s.uuid:
                uart_service = s
                break

        if not uart_service:
            print("Could not find UART Service!")
            return

        print("Scanning Characteristics...")
        for char in uart_service.characteristics:
            print(f"UUID: {char.uuid}, Properties: {char.properties}")
            if "write" in char.properties or "write-without-response" in char.properties:
                print(f"\n✅ CORRECT UUID TO USE: {char.uuid}")

asyncio.run(run())
```
zpi@pi:~/node-scripts $ cat scan.py
```py
import asyncio
from bleak import BleakScanner
async def main():
    print("Scanning...")
    devices = await BleakScanner.discover()
    for d in devices:
        print(f"Address: {d.address} | Name: {d.name}")
asyncio.run(main())
```
zpi@pi:~/node-scripts $ cat send_text.py
```py
import asyncio
import sys
from bleak import BleakClient

# REPLACE WITH YOUR MICROBIT ADDRESS
MICROBIT_ADDRESS = "C2:DB:C7:80:B7:14"
UART_RX_CHAR_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"

async def send_text(text):
    print(f"Connecting to {MICROBIT_ADDRESS}...")
    try:
        async with BleakClient(MICROBIT_ADDRESS) as client:
            if client.is_connected:
                print("Connected!")
                await asyncio.sleep(1.0)

                # Add the New Line character which acts as the 'End of Message' signal
                full_message = f"{text}\n"
                data = full_message.encode('utf-8')

                # --- CHUNKING LOGIC ---
                # We must split the data into 20-byte chunks because
                # generic BLE hardware cannot handle large packets at once.
                chunk_size = 20

                for i in range(0, len(data), chunk_size):
                    chunk = data[i : i + chunk_size]
                    await client.write_gatt_char(UART_RX_CHAR_UUID, chunk, response=False)
                    # Small pause to ensure the micro:bit buffer doesn't overflow
                    await asyncio.sleep(0.1)

                print("Message sent successfully")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Join arguments to form the message
        message = " ".join(sys.argv[1:])
        asyncio.run(send_text(message))
    else:
        print("No text provided")
```

## Flowforge Device Registration 20th May 2023

### PROVISIONING TOKEN ###
1. provisioningName: zraspberry
2. provisioningTeam: MXnyArYa46
3. provisioningToken: ffadp_WXm25DUkqDuSAxy8viUrHJqUkPOQq5zEAiFi7g02YFA
4. forgeURL: http://192.168.2.4:3003

# Nov 13th 2021

1. Convert /var/lib/rundeck/id_rsa to new format  ssh-keygen -p -m PEM -f id_rsa
2. rundeck project settings -> key storage -> add upload key -> Provate Key
3. add rundeck public key to gitlab
4. rundeck -> Jobs -> Job actions -> Commit

## Oct 28 2021

### Rundeck Customization for WebHook integration with SNOW.
1. Project Settings -> Edit Configuration -> Default node executor -> Ansible ad-hoc Node executor, executable : bin/bash , ansible config file path : /home/gitlab-runner/zansible/ansible.cfg , check generate inventory,  (This is not in use)
2. Project Settings -> Add a new node source -> local
3. Jobs -> New Job -> Nodes -> Execute Locally
                   -> Workflow -> Add a Step -> script
```bash
cd /var/lib/rundeck/zansible
ansible-playbook -i inventory.yml console_command.yaml -e arg1=$1

Playbook in zansible folder

---
- hosts: zos_host
  collections:
    - ibm.ibm_zos_core
  gather_facts: no
  vars:
  environment: "{{ environment_vars }}"
  tasks:

    - name: Execute an operator command to show active jobs
      zos_operator:
            cmd: 'C U={{ arg1 }}'
            wait_time_s: 5
            wait: false
      register : result

    - name: Response for Console Command
      debug:
        msg: "{{ result }}"

```
                    -> Workflow -> Argumens : ${option.User}
4. Webhook -> Handler configuration -> run job -> select Job -> Options -> -User ${data.User}
5. Node Red -> Inject Node -> msg.payload : {"User":"IBMUSER"}
6. http-request -> POST -> webhook url

## Oct 27 2021

### Rundeck Ansible Integration
1. Created /usr/share/ansible and /usr/share/ansible/collections folders and chmod 755 
2. sudo ansible-galaxy collection install ibm-ibm_zos_core-1.4.0-beta.1.tar.gz -p /usr/share/ansible/collections
3. ansible-galaxy collection list ( ~/.ansible/collections:/usr/share/ansible/collections <- default value for COLLECTIONS_PATHS in ansible.cfg)
4. sudo usermod -aG sudo rundeck 
5. /etc/sudoers.d/ added sudoers file and made this entry-> rundeck  ALL=(ALL) NOPASSWD:ALL
6. chsh -s /bin/bash rundeck
7. Login as rundeck
13. ssh-keygen
14. ssh-copy-id sysprg1@192.168.2.44


## Oct 24 2021
### pi gpio enablement on Ubuntu
1. sudo apt-get install python3-pip python3-dev
2. sudo pip install RPi.GPIO
3. sudo addgroup gpio
4. sudo chown root:gpio /dev/gpiomem
5. sudo adduser $USER gpio
6. echo 'KERNEL=="gpiomem", NAME="%k", GROUP="gpio", MODE="0660"' | sudo tee /etc/udev/rules.d/45-gpio.rules
7. sudo udevadm control --reload-rules && sudo udevadm trigger
8. sudo apt install python3-gpiozero
9. reboot

## Oct 23 2021

### PostGresql config for rundeck
1. If not already done change password of postgres, passwd postgres
2. su postgres
3. psql
4. create database rundeck;
5. create user rundeckuser with password 'rundeckpassword';
6. grant ALL privileges on database rundeck to rundeckuser;
7. cd etc/rundeck/rundeck-config.properties
```bash
dataSource.driverClassName = org.postgresql.Driver
dataSource.dbCreate = update
dataSource.url = jdbc:postgresql://127.0.0.1:5433/rundeck
dataSource.username = rundeckuser
dataSource.password = rundeckpassword
```
8. sudo service rundeckd start
9. tail -f /var/log/rundeck/service.log
10. http://192.168.2.251:4440

## Oct 21 2021

### Postgresql
```bash
1. sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
2. wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
3. sudo apt-get update
4. sudo apt-get -y install postgresql
5. set listen_addresses = '*' and port = 5433 in /etc/postgresql/14/main/postgresql.conf ( 5432 is used by gitlab postgresql)
6. add line host    all all 0.0.0.0/0   md5 in /etc/postgresql/14/main/pg_hba.conf
7. sudo systemctl stop postgresql
8. sudo systemctl start postgresql
9. passwd postgres ( Change password - This is to access psql prompt to define rundeck database)
10. su postgres
11. psql
12. \password (Change database admin user postgres password here for administration using pgadmin GUI)
```

## Oct 18 2021
### Install Ubuntu Server in RPI
1. Headless ubuntu 64 bit server 20.04.03 LTS using pi imager.
2. sudo nano /etc/netplan/50-cloud-init.yaml
```bash
    wifis:
        wlan0:
            optional: true
            access-points:
                "AX55":
                   password: "passwd"
            dhcp4: true
```
3. sudo update followed by sudo upgrade
### Install Node-Red
4. Install Node Red -> bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
5. enable projects in ~/.node-red/settings.js
6. node-red-start / sudo systemctl enable nodered.service (For Auto Start)
7. Access node-red and clone repository https://gitlab.com/Sunil390/znodered.git 
### Install Ansible as Global
8. curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
9. sudo python3 get-pip.py
10. sudo python3 -m pip install ansible
11. ansible-galaxy collection install ibm-ibm_zos_core-1.4.0-beta.1.tar.gz
12. git clone http://192.168.2.195/mainframe/zansible.git
### ssh setup between rpi and herc
13. ssh-keygen
14. ssh-copy-id sysprg1@192.168.2.44
### Test Ansible from zansible foler
15. ansible-playbook -i inventory.yml console_command.yaml
### Install Gitlab Runner
16. curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh | sudo bash
17. sudo apt-get install gitlab-runner
18. sudo passwd gitlab-runner
19. sudo gitlab-runner register
### Install Rundeck  
20. sudo apt-get install openjdk-11-jre-headless
21. curl https://raw.githubusercontent.com/rundeck/packaging/main/scripts/deb-setup.sh 2> /dev/null | sudo bash -s rundeck
22. sudo apt-get update
23. sudo apt-get install rundeck
24. Update localhost with ip address of server in /etc/rundeck/rundeck-config.properties and /etc/rundeck/framework.properties 
25. sudo service rundeckd start
26. tail -f /var/log/rundeck/service.log  
### Bluetooth LE and Microbit
27. sudo apt install pi-bluetooth
28. sudo reboot
29. sudo pip3 install bluezero  ( This may not be required -> sudo hciattach /dev/ttyAMA0 bcm43xx)
30. bluetoothctl
31. show
32. scan on
33. scan off
34. pair mac..
35. ubitmsg.py code.
```py
import time
import sys
from bluezero import microbit
ubit = microbit.Microbit(adapter_addr='DC:A6:32:87:01:10',
                         device_addr='C2:DB:C7:80:B7:14')

my_text = sys.argv[2]+' '+sys.argv[4]+' '+sys.argv[5]+' '+sys.argv[6]

ubit.connect()

while ubit.button_a < 1:
    ubit.text = my_text
    time.sleep(10)

ubit.disconnect()
```

## Oct 17 2021

1. Headless pi OS install using rpi imager

64GB SDXC Config <https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html>

2. create an empty file ssh at the root of the filesystem for headless ssh access to rpi.
3. Create file wpa_supplicant.conf
```bash
country=IN
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
scan_ssid=1
ssid="your_wifi_ssid"
psk="your_wifi_password"
key_mgmt=WPA-PSK
}
4. passwd to change pi's password and install latest updates
```
```bash
sudo apt update
sudo apt upgrade
sudo apt install git
```
5. Install Node Red -> bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
6. enable projects in ~/.node-red/settings.js
7. node-red-start
8. Access node-red and clone repository https://gitlab.com/Sunil390/znodered.git
9. Install node-red-contrib-alexa-remote2-applestrudel and node-red-dshboard from pallette 
10. added dependencies to project, committed local changes and pushed to gitlab repo.
11. Python3.9 with Openssl
<https://rolandsdev.blog/how-to-install-openssl-1-1-1/>
<https://github.com/actions/setup-python/issues/93>
```bash
sudo apt-get -y install build-essential checkinstall git zlib1g-dev libffi-dev libssl-dev python3-dev cargo
git clone --depth 1 --branch OpenSSL_1_1_1g https://github.com/openssl/openssl.git
cd openssl
./config zlib '-Wl,-rpath,$(LIBRPATH)' -Bsymbolic-functions -fPIC shared
make
make test
sudo make install
sudo ldconfig -v
openssl version

export PATH=$HOME/openssl/bin:$PATH
export LD_LIBRARY_PATH=/home/pi/openssl/lib
export LDFLAGS="-L/home/pi/openssl/lib -Wl,-rpath,/home/pi/openssl/lib"
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/home/pi/openssl/lib/

wget https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz
tar -zxvf Python-3.9.5.tgz
cd Python-3.9.5
./configure --enable-optimizations --with-openssl=/home/pi/openssl
sudo make altinstall
cd /usr/bin
sudo rm python
sudo ln -s /usr/local/bin/python3.9 python
python --version
python -m ssl
```
12. Ansible
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3 get-pip.py
pip install cryptography --no-binary cryptography
sudo python3 -m pip install ansible

```
## August 2021 

### Raspberry Pi Integration with Microbit over Bluetooth Low Enery - Send Messages to ubit over BLE from RPI

### Hardware

1. Raspberry pi 4 with Raspberry pi OS 32 bit .. https://www.raspberrypi.org/software/
2. Microbit v2 https://microbit.org/  https://makecode.microbit.org/

### Software

1. Nodered 2.0.5
2. MakeCode - to be downloaded to Microbit
```py
def on_bluetooth_connected():
    basic.show_leds("""
        . # # # .
                # . . . .
                # . . . .
                # . . . .
                . # # # .
    """)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_leds("""
        # # # . .
                # . . # .
                # . . # .
                # . . # .
                # # # . .
    """)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

basic.show_leds("""
    # . . # #
        # . . # #
        # # # . .
        # . # . .
        # # # . .
""")
bluetooth.start_accelerometer_service()
bluetooth.start_button_service()
bluetooth.start_led_service()
bluetooth.start_temperature_service()
``` 
3. Installed sudo pip3 install bluezero  https://ukbaz.github.io/howto/ubit_workshop.html  

``` shell
pi@raspberrypi:~ $ bluetoothctl
Agent registered
[bluetooth]# show
Controller DC:A6:32:87:01:10 (public)
	Name: raspberrypi
	Alias: raspberrypi
	Class: 0x000c0000
	Powered: yes
	Discoverable: no
	Pairable: yes
	UUID: Headset AG                (00001112-0000-1000-8000-00805f9b34fb)
	UUID: Generic Attribute Profile (00001801-0000-1000-8000-00805f9b34fb)
	UUID: A/V Remote Control        (0000110e-0000-1000-8000-00805f9b34fb)
	UUID: Generic Access Profile    (00001800-0000-1000-8000-00805f9b34fb)
	UUID: PnP Information           (00001200-0000-1000-8000-00805f9b34fb)
	UUID: A/V Remote Control Target (0000110c-0000-1000-8000-00805f9b34fb)
	UUID: Audio Source              (0000110a-0000-1000-8000-00805f9b34fb)
	UUID: Audio Sink                (0000110b-0000-1000-8000-00805f9b34fb)
	UUID: Headset                   (00001108-0000-1000-8000-00805f9b34fb)
	Modalias: usb:v1D6Bp0246d0532
	Discovering: no
[bluetooth]# 
[bluetooth]# scan on
Discovery started
[CHG] Controller DC:A6:32:87:01:10 Discovering: yes
[NEW] Device 5E:1D:C8:93:F8:27 5E-1D-C8-93-F8-27
[NEW] Device 4B:22:96:6F:47:C3 4B-22-96-6F-47-C3
[NEW] Device 49:C4:DD:DB:67:FB 49-C4-DD-DB-67-FB
[NEW] Device 55:C1:2B:A7:73:63 55-C1-2B-A7-73-63
[NEW] Device 70:67:7B:96:4F:B9 70-67-7B-96-4F-B9
[NEW] Device C2:DB:C7:80:B7:14 BBC micro:bit [puzot]
[CHG] Device 70:67:7B:96:4F:B9 RSSI: -76
[NEW] Device 7C:74:19:35:40:FA 7C-74-19-35-40-FA
[bluetooth]# scan off 

```

```bash
[bluetooth]# pair C2:DB:C7:80:B7:14

Pairing successful

[bluetooth]# devices
Device C2:DB:C7:80:B7:14 BBC micro:bit [puzot]
[bluetooth]# 

```


### Download the makecode script to ubit

https://ukbaz.github.io/howto/ubit_workshop.html

### Run the Code in Python IDE in RPI


### Sending a message to the micro:bit
This first Python exercise is to send text to display on the micro:bit.

```py
from bluezero import microbit
ubit = microbit.Microbit(adapter_addr='DC:A6:32:87:01:10',
                         device_addr='C2:DB:C7:80:B7:14')
my_text = 'Hello, world'
ubit.connect()

while my_text is not '':
    ubit.text = my_text
    my_text = input('Enter message: ')

ubit.disconnect()
```

### Reading a button press
Display an image of which button needs pressing to break out of the loop

```py
import time
from bluezero import microbit
ubit = microbit.Microbit(adapter_addr='DC:A6:32:87:01:10',
                         device_addr='C2:DB:C7:80:B7:14')
ubit.connect()
while ubit.button_a < 1:
    ubit.pixels = [0b00000, 0b01000, 0b11111, 0b01000, 0b00000]
    time.sleep(0.5)
    ubit.clear_display()

while ubit.button_b < 1:
    ubit.pixels = [0b00000, 0b00010, 0b11111, 0b00010, 0b00000]
    time.sleep(0.5)
    ubit.clear_display()

ubit.disconnect()
```
    
### Reading values from the micro:bit
This last exercise uses information from the micro:bit sensors to be displayed ont he Raspberry Pi.

Pressing Button A prints if the micro:bit is face-up or face-down
Pressing Button B print the temperature from the micro:bit
Pressing Button A & B exits the code

```py
import time
from bluezero import microbit

ubit = microbit.Microbit(adapter_addr='DC:A6:32:87:01:10',
                         device_addr='C2:DB:C7:80:B7:14')
looping = True
ubit.connect()
print('Connected... Press a button to select mode')
mode = 0
while looping:
    if ubit.button_a > 0 and ubit.button_b > 0:
        mode = 3
        ubit.pixels = [0b10001, 0b01010, 0b00100, 0b01010, 0b10001]
        time.sleep(1)
    elif ubit.button_b > 0:
        mode = 2
        ubit.pixels = [0b11111, 0b00100, 0b00100, 0b00100, 0b00100]

        time.sleep(0.25)
    elif ubit.button_a > 0:
        mode = 1
        ubit.pixels = [0b11110, 0b10000, 0b11100, 0b10000, 0b10000]
        time.sleep(0.25)

    if mode == 1:
        x, y, z = ubit.accelerometer
        if z < 0:
            print('Face up')
        else:
            print('Face down')
        time.sleep(0.5)
    elif mode == 2:
        print('Temperature:', ubit.temperature)
        time.sleep(0.5)
    elif mode == 3:
        looping = False
        print('Exiting')

ubit.disconnect()
```


## Integrating with Node-RED

1. Python code to Send the message to ubit over ble
sys is used to pass argument
when button A is pressed for 5 seconds the alert message sent to ubit will stop displaying

ubitmsg.py code...
```py
import time
import sys
from bluezero import microbit
ubit = microbit.Microbit(adapter_addr='DC:A6:32:87:01:10',
                         device_addr='C2:DB:C7:80:B7:14')

my_text = sys.argv[2]+' '+sys.argv[4]+' '+sys.argv[5]+' '+sys.argv[6]

ubit.connect()

while ubit.button_a < 1:
    ubit.text = my_text
    time.sleep(10)

ubit.disconnect()
```

2. in the .profile of RPI pi user added the PYTHONPATH entry

```shell
export PYTHONPATH=".:/usr/local/lib/python3.7"
```

3. Added an exec node in Node-RED with command as python3  ubitmsg.py and enabled append msg.payload option.

prefix the command with sudo in the exec node,   sudo python3  ubitmsg.py 
