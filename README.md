# PicoW_ESP32_BLE
Last time I showed you how to use BLE to facilitate communication between a Pico W and ESP32. In that case the Pico was the central and ESP32 the peripheral. This time, this project does the reverse. So the ESP32 is now the central and the Pico the peripheral. A Medium article will accompany this project.

Inside the `esp32-pico` directory are these files:

* `esp32_central.py`: This is for the ESP32 to act as a central device.
* `pico_per.py`: This is for the Pico to act as a peripheral.
* `uuids.json`: This is the JSON file for the UUIDs

![image](https://github.com/sentairanger/PicoW_ESP32_BLE/blob/main/esp32-pico_bb.jpg)
