# Raspberry Pi Integration with Microbit over Bluetooth Low Enery

## Hardware

1. Raspberry pi 4
2. Microbit v2

## Software

1. Nodered 2.0.5
2. BLE https://ukbaz.github.io/howto/ubit_workshop.html 

Installed sudo pip3 install bluezero

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
