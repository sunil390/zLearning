# esp32 nano + rd-03d

## 12th June 2026

1. zpi
2. python -m venv .venv
3. source .venv/bin/activate
4. pip3 install esphome
5. sudo usermod -a -G dialout zpi
6. ls /dev/tty*
7. mkdir -p config
8. esphome dashboard config/
9. esphome run config/radar-node.yaml --device /dev/ttyACM0
10. esphome logs config/radar-node.yaml
11. radar-node.yml

```yml
esphome:
  name: radar-node

esp32:
  board: esp32-s3-devkitc-1
  framework:
    type: arduino

# --- WI-FI SETTINGS ---
wifi:
  ssid: "AX55"
  password: "xxxxxxxxxxxxx"

  # SoftAP fallback hotspot if your home Wi-Fi disconnects
  ap:
    ssid: "Radar-Node-Fallback"
    password: "xxxxxxxxxxx"

captive_portal:

logger:

# --- HARDWARE SERIAL CONFIGURATION ---
# Handles the high-speed 256k raw radar stream on D0/D1 pins
uart:
  - id: radar_uart
    tx_pin: GPIO44  # This is the physical D1 pad on the board
    rx_pin: GPIO43  # This is the physical D0 pad on the board
    baud_rate: 256000

# Activates the built-in RD-03D library components
rd03d:
  uart_id: radar_uart

# --- SENSOR INGESTION & COUPLING ---
binary_sensor:
  - platform: rd03d
    target:
      name: "Target Detected"

# --- SENSORS ---
sensor:
  # --- Target 1 ---
  - platform: rd03d
    target_1:
      x:
        name: "Target 1 X"
      y:
        name: "Target 1 Y"
      speed:
        name: "Target 1 Speed"

  # --- Target 2 ---
  - platform: rd03d
    target_2:
      x:
        name: "Target 2 X"
      y:
        name: "Target 2 Y"
      speed:
        name: "Target 2 Speed"

  # --- Target 3 ---
  - platform: rd03d
    target_3:
      x:
        name: "Target 3 X"
      y:
        name: "Target 3 Y"
      speed:
        name: "Target 3 Speed"

# Streams the coordinates seamlessly over the network back to Node-RED 5
mqtt:
  broker: 127.0.0.1  # Points directly back to your Pi's local broker profile
  topic_prefix: home/radar
```

12. Install logs

```sh
Creating ESP32-S3 image...
Successfully created ESP32-S3 image.
Linking .pioenvs/radar-node/firmware.elf
                            Memory Type Usage Summary
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Memory Type/Section ┃ Used [bytes] ┃ Used [%] ┃ Remain [bytes] ┃ Total [bytes] ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ Flash Code          │       727072 │          │                │               │
│    .text            │       727072 │          │                │               │
│ Flash Data          │       135888 │          │                │               │
│    .rodata          │       135632 │          │                │               │
│    .appdesc         │          256 │          │                │               │
│ DIRAM               │       104399 │    30.55 │         237361 │        341760 │
│    .text            │        53075 │    15.53 │                │               │
│    .bss             │        32736 │     9.58 │                │               │
│    .data            │        18588 │     5.44 │                │               │
│ IRAM                │        16384 │    100.0 │              0 │         16384 │
│    .text            │        15356 │    93.73 │                │               │
│    .vectors         │         1028 │     6.27 │                │               │
└─────────────────────┴──────────────┴──────────┴────────────────┴───────────────┘
Total image size: 951007 bytes (.bin may be padded larger)
Note: The reported total sizes may be smaller than those in the technical reference manual due to reserved memory and application configuration. The total flash size available for the application is not included by default, as it cannot be reliably determined due to the presence of other data like the bootloader, partition table, and application partition size.
RAM:   [==        ]  15.7% (used 51324 bytes from 327680 bytes)
Flash: [=====     ]  51.8% (used 950751 bytes from 1835008 bytes)
Building .pioenvs/radar-node/firmware.bin
Creating ESP32-S3 image...
Successfully created ESP32-S3 image.
Creating binary "firmware.factory.bin" with:
    Offset   | File
 -  0x0      | bootloader.bin
 -  0x8000   | partitions.bin
 -  0x9000   | boot_app0.bin
 -  0x10000  | firmware.bin
Successfully created combined binary image.
sign_firmware([".pioenvs/radar-node/firmware.bin"], [".pioenvs/radar-node/firmware.elf"])
merge_factory_bin([".pioenvs/radar-node/firmware.bin"], [".pioenvs/radar-node/firmware.elf"])
Info: bootloader.bin not found - skipping
Info: partition-table.bin not found - skipping
Info: ota_data_initial.bin not found - skipping
Info: radar-node.bin not found - skipping
Using FLASH_EXTRA_IMAGES from PlatformIO environment
Merging binaries into /home/zpi/config/.esphome/build/radar-node/.pioenvs/radar-node/firmware.factory.bin
Merging binaries with esptool
SHA digest in image updated.
Wrote 0xf8370 bytes to file '/home/zpi/config/.esphome/build/radar-node/.pioenvs/radar-node/firmware.factory.bin', ready to flash to offset 0x0.
Successfully created /home/zpi/config/.esphome/build/radar-node/.pioenvs/radar-node/firmware.factory.bin
esp32_copy_ota_bin([".pioenvs/radar-node/firmware.bin"], [".pioenvs/radar-node/firmware.elf"])
Copied firmware to /home/zpi/config/.esphome/build/radar-node/.pioenvs/radar-node/firmware.ota.bin
============================================ [SUCCESS] Took 719.52 seconds ============================================
Using Python 3.11.2 environment at: /home/zpi/.platformio/penv/.espidf-5.5.4
INFO Build Info: config_hash=0x168e5f1d build_time_str=2026-06-12 01:04:17 +0530
INFO Successfully compiled program.
esptool v5.2.0
Connected to ESP32-S3 on /dev/ttyACM0:
Chip type:          ESP32-S3 (QFN56) (revision v0.2)
Features:           Wi-Fi, BT 5 (LE), Dual Core + LP Core, 240MHz, Embedded PSRAM 8MB (AP_3v3)
Crystal frequency:  40MHz
USB mode:           USB-Serial/JTAG
MAC:                48:ca:43:2e:41:78

Stub flasher running.
Changing baud rate to 460800...
Changed.

Configuring flash size...
Auto-detected flash size: 16MB
Flash will be erased from 0x00010000 to 0x000f8fff...
Wrote 951152 bytes (635330 compressed) at 0x00010000 in 7.7 seconds (985.8 kbit/s).
Hash of data verified.
Flash parameters set to 0x024f.
SHA digest in image updated.
Flash will be erased from 0x00000000 to 0x00005fff...
Wrote 20864 bytes (13355 compressed) at 0x00000000 in 0.4 seconds (448.2 kbit/s).
Hash of data verified.
Flash will be erased from 0x00008000 to 0x00008fff...
Wrote 3072 bytes (161 compressed) at 0x00008000 in 0.0 seconds (580.6 kbit/s).
Hash of data verified.
Flash will be erased from 0x00009000 to 0x0000afff...
Wrote 8192 bytes (47 compressed) at 0x00009000 in 0.1 seconds (788.4 kbit/s).
Hash of data verified.

Hard resetting via RTS pin...
INFO Successfully uploaded program.
INFO Starting log output from /dev/ttyACM0 with baud rate 115200
[01:16:58.165][D][wifi:1458]: Found networks:
[01:16:58.167][I][wifi:1429]: - 'AX55' (F0:2F:74:EB:0A:78) ▂▄▆█ Ch: 4 -68dB P:0
[01:16:58.167][D][wifi:1852]: Retry phase: INITIAL_CONNECT → SCAN_CONNECTING
[01:16:58.169][I][wifi:1097]: Connecting to 'AX55' (F0:2F:74:EB:0A:78) (priority 0, attempt 1/2 in phase SCAN_CONNECTING)...
[01:16:59.295][I][wifi:1570]: Connected
[01:16:59.296][D][wifi:1587]: Disabling AP
[01:16:59.297][C][wifi:1237]:   IP Address: 192.168.2.221
[01:16:59.298][C][wifi:1248]:   SSID: 'AX55'
[01:16:59.298][C][wifi:1248]:   BSSID: F0:2F:74:EB:0A:78
[01:16:59.299][C][wifi:1248]:   Hostname: 'radar-node'
[01:16:59.299][C][wifi:1248]:   Signal strength: -69 dB ▂▄▆█
[01:16:59.300][C][wifi:1248]:   Channel: 4
[01:16:59.300][C][wifi:1248]:   Subnet: 255.255.255.0
[01:16:59.300][C][wifi:1248]:   Gateway: 192.168.2.1
[01:16:59.300][C][wifi:1248]:   DNS1: 192.168.2.1
[01:16:59.301][C][wifi:1248]:   DNS2: 0.0.0.0
```
