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
