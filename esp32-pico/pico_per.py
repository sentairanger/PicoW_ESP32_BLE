import aioble
import bluetooth
import asyncio
import struct  
import json
from machine import Pin

led = Pin("LED", Pin.OUT)

connected = False

with open("uuids.json", mode="r", encoding="utf-8") as read_file:
    uuids_data = json.load(read_file) 

IAM = "Peripheral"
BLE_NAME = f"{IAM}"
BLE_SVC_UUID = bluetooth.UUID(uuids_data["service"])
BLE_CHARACTERISTIC_UUID = bluetooth.UUID(uuids_data["characteristic"])
BLE_APPEARANCE = 0x0300
BLE_ADVERTISING_INTERVAL = 2000
BLE_SCAN_LENGTH = 5000
BLE_INTERVAL = 30000
BLE_WINDOW = 30000

# state variables
message_count = 0

def encode_message(message):
    """ Encode a message to bytes """
    return message.encode('utf-8')

def decode_message(message):
    """ Decode a message from bytes """
    return message.decode('utf-8')

async def blink_led_task():
    global connected
    toggle = True
    while True:
        led.value(toggle)
        toggle = not toggle
        blink = 1000 if connected else 250
        await asyncio.sleep_ms(blink)

async def send_data_task(connection, characteristic):
    """Send data to the central device."""
    global message_count
    while True:
        message = f"{MESSAGE} {message_count}"
        message_count += 1
        print(f"Sending: {message}")

        try:
            msg = encode_message(message)
            characteristic.write(msg)  # Peripheral writes data here
            await asyncio.sleep(1)
        except Exception as e:
            print(f"Error while sending data: {e}")
            continue

async def run_peripheral_mode():
    global connected
    """ Run the peripheral mode """

    # Set up the Bluetooth service and characteristic
    ble_service = aioble.Service(BLE_SVC_UUID)
    characteristic = aioble.Characteristic(
        ble_service,
        BLE_CHARACTERISTIC_UUID,
        read=True,
        notify=True,
        write=True,
        capture=True,
    )
    aioble.register_services(ble_service)

    print(f"{BLE_NAME} starting to advertise")

    while True:
        async with await aioble.advertise(
            BLE_ADVERTISING_INTERVAL,
            name=BLE_NAME,
            services=[BLE_SVC_UUID],
            appearance=BLE_APPEARANCE) as connection:
            connected = True
            print(f"{BLE_NAME} connected to another device: {connection.device}")

            tasks = [
                asyncio.create_task(send_data_task(connection, characteristic)),
                asyncio.create_task(blink_led_task())
            ]
            await asyncio.gather(*tasks)
            print(f"{IAM} disconnected")
            connected = False 
            break

asyncio.run(run_peripheral_mode)