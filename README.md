# PicoW_ESP32_BLE
Last time I showed you how to use BLE to facilitate communication between a Pico W and ESP32. In that case the Pico was the central and ESP32 the peripheral. This time, this project does the reverse. So the ESP32 is now the central and the Pico the peripheral. A Medium article will accompany this project.

Inside the `esp32-pico` directory are these files:

* `esp32_central.py`: This is for the ESP32 to act as a central device.
* `pico_per.py`: This is for the Pico to act as a peripheral.
* `uuids.json`: This is the JSON file for the UUIDs

Inside the `esp32_pico_pot` directory are these files:
* `esp32_central.py`: Same file as before in the `esp32-pico` folder
* `pico_per_pot.py`: This is for the Pico to send the values of the potentiometer to the ESP32.
* `esp32_central_pwm.py`: This adjusts the brightness of the LED based on the values it gets from the Pico.
* `uuids.json`

Inside the `esp32_pico_dual` directory are these files:
* `esp32_central.py`: Same code as before
* `pico_per.py`: Also same code as before
* `uuids.json`


![image](https://github.com/sentairanger/PicoW_ESP32_BLE/blob/main/esp32-pico_bb.jpg)
![picture](https://github.com/sentairanger/PicoW_ESP32_BLE/blob/main/esp32-pico-pot_bb.jpg)
