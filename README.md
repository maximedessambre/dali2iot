# dali2iot

Async python library to control your Lunatone DALi2IoT gateway
Works with https://www.lunatone.com/en/product/dali-2-iot-gateway/ 

## Installation

To be published to PyPI. Working on it :)

## Usage

The d2i object is using an internal FSM thanks to the "status" property. Each state is defined with a constant

- `DALI_INIT = 0` : initial state
- `DALI_CONNECTED = 1` : the gateway is a recognized as a supported DALI2IoT gateway
- `DALI_SCANNING = 2` : BUS Scan in progress
- `DALI_SCANNING_STOP = 3` : BUS scan stopped
- `DALI_READY = 4` : BUS scan completed
- `DALI_ERROR = -1` : An error has occured, see the `error` property to know more

Note: scanning is mandatory only if a device is not found on the DALI BUS. The gateway will work in `DALI_CONNECTED` and `DALI_READY`state

A running example can be found under the `example.py` file

1. Validate the host is a recognized Dali2IoT gateway using static method

```python
is_dali, ret = await dali2iot.DALI2IoT.is_dali(host=host)
```

2. If the gateway is supported, you can connect to it ()
````python
asyncio.run(d2i.connect())
````

3. Scan your DALI Bus if the devices have not been discovered yet
```python
asyncio.run(d2i.scan())
```

4. Retrieve the devices known by the gateway

Note: if the device is newly added, it might not be known by the DALI BUS itself. Run a scan to have it discover and address

```python
asyncio.run(d2i.get_devices())
```

5. Start the monitoring thread

```python
d2i.monitor()
```

The monitoring thread open a websocket to the gateway and listen to incoming messages.
When a device state change is receive, the corresponding DaliDevice get their status updated to reflect the current state of the device

#### Example 
Below is a `devices` type message, indicating a change in the device status with the new device state
```json
{
  "type": "devices",
  "data": {
  "devices": [
    {
      "id": 1,
      "name": "Dali #0",
      "address": 0,
      "line": 0,
      "type": "default",
      "features": {
        "switchable": {
          "status": false
        }
      } ...
    }, ...
}
```

6. Toggle a device

```python
device_id = int(input("Device id: "))
device = next((d for d in d2i.devices if d.id == device_id), None)
if device is not None:
    if device.is_on:
        asyncio.run(d2i.turn_off(device))
    else:
        asyncio.run(d2i.turn_on(device))
```

## What's next?

### Planned

- Scan progress update using websocket

### Unplanned

- SSL support