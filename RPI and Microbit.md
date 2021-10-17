# Oct 2021

1. headinstall using rpi imager

64GB SDXC Config <https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html>

2. create an empty file ssh at the root of the filesystem for headless ssh access to rpi.
3. Create file wpa_supplicant.conf
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
```
sudo apt-get -y install build-essential checkinstall git zlib1g-dev
git clone --depth 1 --branch OpenSSL_1_1_1g https://github.com/openssl/openssl.git
cd openssl
./config zlib '-Wl,-rpath,$(LIBRPATH)'
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
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

```
# August 2021 

# Raspberry Pi Integration with Microbit over Bluetooth Low Enery - Send Messages to ubit over BLE from RPI

## Hardware

1. Raspberry pi 4 with Raspberry pi OS 32 bit .. https://www.raspberrypi.org/software/
2. Microbit v2 https://microbit.org/  https://makecode.microbit.org/

## Software

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

```
[bluetooth]# pair C2:DB:C7:80:B7:14
Attempting to pair with C2:DB:C7:80:B7:14
[CHG] Device C2:DB:C7:80:B7:14 Connected: yes
[CHG] Device C2:DB:C7:80:B7:14 UUIDs: 00001800-0000-1000-8000-00805f9b34fb
[CHG] Device C2:DB:C7:80:B7:14 UUIDs: 00001801-0000-1000-8000-00805f9b34fb
[CHG] Device C2:DB:C7:80:B7:14 UUIDs: 0000180a-0000-1000-8000-00805f9b34fb
[CHG] Device C2:DB:C7:80:B7:14 UUIDs: 0000fe59-0000-1000-8000-00805f9b34fb
[CHG] Device C2:DB:C7:80:B7:14 UUIDs: e95d93af-251d-470a-a062-fa1922dfa9a8
[CHG] Device C2:DB:C7:80:B7:14 UUIDs: e97dd91d-251d-470a-a062-fa1922dfa9a8
[CHG] Device C2:DB:C7:80:B7:14 ServicesResolved: yes
[CHG] Device C2:DB:C7:80:B7:14 Paired: yes
[NEW] Primary Service
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service000a
	00001801-0000-1000-8000-00805f9b34fb
	Generic Attribute Profile
[NEW] Characteristic
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service000a/char000b
	00002a05-0000-1000-8000-00805f9b34fb
	Service Changed
[NEW] Descriptor
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service000a/char000b/desc000d
	00002902-0000-1000-8000-00805f9b34fb
	Client Characteristic Configuration
[NEW] Primary Service
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service000e
	0000fe59-0000-1000-8000-00805f9b34fb
	Nordic Semiconductor ASA
[NEW] Characteristic
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service000e/char000f
	8ec90004-f315-4f60-9fb8-838830daea50
	Vendor specific
[NEW] Descriptor
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service000e/char000f/desc0011
	00002902-0000-1000-8000-00805f9b34fb
	Client Characteristic Configuration
[NEW] Primary Service
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service0012
	e97dd91d-251d-470a-a062-fa1922dfa9a8
	Vendor specific
[NEW] Characteristic
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service0012/char0013
	e97d3b10-251d-470a-a062-fa1922dfa9a8
	Vendor specific
[NEW] Descriptor
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service0012/char0013/desc0015
	00002902-0000-1000-8000-00805f9b34fb
	Client Characteristic Configuration
[NEW] Primary Service
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service0016
	0000180a-0000-1000-8000-00805f9b34fb
	Device Information
[NEW] Characteristic
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service0016/char0017
	00002a24-0000-1000-8000-00805f9b34fb
	Model Number String
[NEW] Characteristic
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service0016/char0019
	00002a25-0000-1000-8000-00805f9b34fb
	Serial Number String
[NEW] Characteristic
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service0016/char001b
	00002a26-0000-1000-8000-00805f9b34fb
	Firmware Revision String
[NEW] Primary Service
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service001d
	e95d93af-251d-470a-a062-fa1922dfa9a8
	MicroBit Event Service
[NEW] Characteristic
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service001d/char001e
	e95d9775-251d-470a-a062-fa1922dfa9a8
	MicroBit Event Data
[NEW] Descriptor
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service001d/char001e/desc0020
	00002902-0000-1000-8000-00805f9b34fb
	Client Characteristic Configuration
[NEW] Characteristic
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service001d/char0021
	e95d5404-251d-470a-a062-fa1922dfa9a8
	MicroBit Client Events
[NEW] Characteristic
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service001d/char0023
	e95d23c4-251d-470a-a062-fa1922dfa9a8
	MicroBit Client Requirements
[NEW] Characteristic
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service001d/char0025
	e95db84c-251d-470a-a062-fa1922dfa9a8
	MicroBit Requirements
[NEW] Descriptor
	/org/bluez/hci0/dev_C2_DB_C7_80_B7_14/service001d/char0025/desc0027
	00002902-0000-1000-8000-00805f9b34fb
	Client Characteristic Configuration
Pairing successful

[bluetooth]# devices
Device C2:DB:C7:80:B7:14 BBC micro:bit [puzot]
[bluetooth]# 

```


## Download the makecode script to ubit

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

Flow export from Node-RED

```json
[
    {
        "id": "524fe5c0.a70e5c",
        "type": "tab",
        "label": "zIOT",
        "disabled": false,
        "info": ""
    },
    {
        "id": "c7dc0a18.2c9288",
        "type": "template",
        "z": "524fe5c0.a70e5c",
        "name": "TeamsMessageBuild",
        "field": "payload",
        "fieldType": "msg",
        "format": "handlebars",
        "syntax": "mustache",
        "template": "{\n  \"@context\": \"https://schema.org/extensions\",\n  \"@type\": \"MessageCard\",\n  \"themeColor\": \"0072C6\",\n  \"title\": \"Node-RED to Teams\",\n  \"text\": \" {{payload}} \"\n}",
        "output": "str",
        "x": 640,
        "y": 300,
        "wires": [
            []
        ]
    },
    {
        "id": "bc1662fd.9545e",
        "type": "http request",
        "z": "524fe5c0.a70e5c",
        "name": "WebHook to MS Teams",
        "method": "POST",
        "ret": "txt",
        "paytoqs": "ignore",
        "url": "https://atos365.webhook.office.com/webhookb2/e6ac63b9-669b-4f26-bba5-4b0a37fa8ff3@33440fc6-b7c7-412c-bb73-0e70b0198d5a/IncomingWebhook/f3923ae196ad4bdfb2f5451a2248950a/788daa90-58da-4246-b1ab-7de9e262496d",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "x": 890,
        "y": 300,
        "wires": [
            []
        ]
    },
    {
        "id": "5b199649.a8ad08",
        "type": "http in",
        "z": "524fe5c0.a70e5c",
        "name": "zListener",
        "url": "/zEntry",
        "method": "post",
        "upload": false,
        "swaggerDoc": "",
        "x": 100,
        "y": 160,
        "wires": [
            [
                "4ef25165.b2dc2",
                "63a752a9.7bdd0c",
                "1eaccced9bc5756c"
            ]
        ]
    },
    {
        "id": "4ef25165.b2dc2",
        "type": "template",
        "z": "524fe5c0.a70e5c",
        "name": "ResponceMsg",
        "field": "payload",
        "fieldType": "msg",
        "format": "handlebars",
        "syntax": "mustache",
        "template": "Sweets from Node-RED: {{payload}} !",
        "output": "str",
        "x": 340,
        "y": 100,
        "wires": [
            [
                "795d3737.d353e8"
            ]
        ]
    },
    {
        "id": "795d3737.d353e8",
        "type": "http response",
        "z": "524fe5c0.a70e5c",
        "name": "Responce",
        "statusCode": "",
        "headers": {},
        "x": 580,
        "y": 100,
        "wires": []
    },
    {
        "id": "63a752a9.7bdd0c",
        "type": "http request",
        "z": "524fe5c0.a70e5c",
        "name": "Download mp3",
        "method": "GET",
        "ret": "bin",
        "paytoqs": "ignore",
        "url": "https://quz1yp-a.akamaihd.net/downloads/ringtones/files/dl/mp3/kannodu-kannodu-kannoram-49034-51958-53676.mp3",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "x": 340,
        "y": 160,
        "wires": [
            [
                "2539fbce.cb39a4"
            ]
        ],
        "info": "https://quz1yp-a.akamaihd.net/downloads/ringtones/files/dl/mp3/kannodu-kannodu-kannoram-49034-51958-53676.mp3\n\n"
    },
    {
        "id": "2539fbce.cb39a4",
        "type": "play audio",
        "z": "524fe5c0.a70e5c",
        "name": "",
        "voice": "21",
        "x": 610,
        "y": 160,
        "wires": []
    },
    {
        "id": "1eaccced9bc5756c",
        "type": "split",
        "z": "524fe5c0.a70e5c",
        "name": "Array to Message",
        "splt": "\\n",
        "spltType": "str",
        "arraySplt": 1,
        "arraySpltType": "len",
        "stream": false,
        "addname": "",
        "x": 350,
        "y": 220,
        "wires": [
            [
                "c7dc0a18.2c9288",
                "be15d2f960bd4334",
                "4955728690484afa"
            ]
        ]
    },
    {
        "id": "be15d2f960bd4334",
        "type": "alexa-remote-routine",
        "z": "524fe5c0.a70e5c",
        "name": "",
        "account": "2be4ecceb4fdbc89",
        "routineNode": {
            "type": "speak",
            "payload": {
                "type": "announcement",
                "text": {
                    "type": "msg",
                    "value": "payload"
                },
                "devices": [
                    "G090XG0793742RWP"
                ]
            }
        },
        "x": 620,
        "y": 220,
        "wires": [
            []
        ]
    },
    {
        "id": "90ed2c4405b2637b",
        "type": "inject",
        "z": "524fe5c0.a70e5c",
        "name": "",
        "props": [
            {
                "p": "payload"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "test",
        "payloadType": "str",
        "x": 130,
        "y": 380,
        "wires": [
            [
                "4955728690484afa"
            ]
        ]
    },
    {
        "id": "4955728690484afa",
        "type": "exec",
        "z": "524fe5c0.a70e5c",
        "command": "python3 ubitmsg.py",
        "addpay": "payload",
        "append": "",
        "useSpawn": "false",
        "timer": "",
        "winHide": false,
        "oldrc": false,
        "name": "Send Message",
        "x": 600,
        "y": 380,
        "wires": [
            [],
            [
                "37d148a93ed040e6"
            ],
            []
        ]
    },
    {
        "id": "37d148a93ed040e6",
        "type": "debug",
        "z": "524fe5c0.a70e5c",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "statusVal": "",
        "statusType": "auto",
        "x": 850,
        "y": 380,
        "wires": []
    },
    {
        "id": "2be4ecceb4fdbc89",
        "type": "alexa-remote-account",
        "name": "",
        "authMethod": "proxy",
        "proxyOwnIp": "192.168.2.252",
        "proxyPort": "3456",
        "cookieFile": "/home/pi/Alexa",
        "refreshInterval": "3",
        "alexaServiceHost": "pitangui.amazon.com",
        "amazonPage": "amazon.com",
        "acceptLanguage": "en-US",
        "userAgent": "",
        "useWsMqtt": "on",
        "autoInit": "on"
    }
]
```

### RPI in Headless Mode

prefix the command with sudo in the exec node,   sudo python3  ubitmsg.py 
