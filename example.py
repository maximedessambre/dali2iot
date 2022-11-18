from src import dali2iot
import asyncio

CONNECT = 1
SCAN = 2
DEVICES_LIST = 3
MONITORING = 4
DEVICES_PRINT = 5
TOGGLE_LIGHT = 6
EXIT_CODE=9

def menu():
    opts = [CONNECT, SCAN, DEVICES_LIST, MONITORING, TOGGLE_LIGHT, EXIT_CODE]
    s = 0

    while s not in opts:
        print(f"{CONNECT}. Connect to DALI2IoT")
        print(f"{SCAN}. Scan DALI gateway")
        print(f"{DEVICES_LIST}. Get devices list")
        print(f"{MONITORING}. Toggle monitoring thread")
        print(f"{DEVICES_PRINT}. Print devices")
        print(f"{TOGGLE_LIGHT}. Toggle light")
        print(f"{EXIT_CODE}. Exit")

        try:
            s = int(input("Choice: "))
        except Exception as e:
            pass

    return s

if __name__ == '__main__':

    host = "10.0.30.16"

    is_dali, ret = asyncio.run(dali2iot.DALI2IoT.is_dali(host=host))

    if not is_dali:
        print(f"{host} is not a recognized DALI2IoT Gateway")
        exit(-1)

    d2i = dali2iot.DALI2IoT(host=host)

    s = 0

    while s is not EXIT_CODE:
        s = menu()

        if s == CONNECT:
            asyncio.run(d2i.connect())
        elif s == SCAN:
            asyncio.run(d2i.scan())
        elif s == DEVICES_LIST:
            asyncio.run(d2i.get_devices())
        elif s == MONITORING:
            d2i.subscribe()
        elif s == DEVICES_LIST or s == TOGGLE_LIGHT:

            for device in d2i.devices:
                print(device)

            if s == TOGGLE_LIGHT:

                try:
                    device_id = int(input("Device id: "))
                    device = next((d for d in d2i.devices if d.id == device_id), None)
                    if device is not None:
                        if device.is_on:
                            asyncio.run(d2i.turn_off(device))
                        else:
                            asyncio.run(d2i.turn_on(device))
                    else:
                        print(f"Unrecognized device id {device_id}")

                except Exception as e:
                    print(f"Error {e}")
        elif s == EXIT_CODE:
            d2i.bye()
