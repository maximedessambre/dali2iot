import websocket
import requests
import threading
import logging
import sys
import time
import json

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

DALI_INIT = 0
DALI_CONNECTED = 1
DALI_SCANNING = 2
DALI_SCANNING_STOP = 3
DALI_READY = 4
DALI_ERROR = -1

DALI_SCAN_INTERVAL = 2

DALI_DEVICE_DEFAULT = "default"
DALI_DEVICE_LIGHT = "switchable"
DALI_DEVICE_LIGHT_DIM = "dimmable"


class DaliDevice:
    """
    DaliDevice super class. Represent any dali devices
    """

    def __init__(self, id: int, name: str, info: str, type: str = DALI_DEVICE_DEFAULT, features=None, scenes=None,
                 groups=None):

        if groups is None:
            groups = []
        if scenes is None:
            scenes = []
        if features is None:
            features = {}

        self._id = id
        self._name = name
        self._info = info
        self._type = type
        self._features = features
        self._scenes = scenes
        self._groups = groups

        logging.debug(f"New device added, id:{id}, name:{name}")

    def __repr__(self):
        return f"Dali device {self.name} ({self.id})"

    def __str__(self):
        return f"{self.name} ({self.id})"

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def info(self):
        return self._info

    @property
    def type(self):
        return self._type

    @property
    def features(self):
        return self._features

    def update(self, kargs):
        self._features.update(kargs)
        # {"id": 6, "features": {"switchable": {"status": false}, "dimmable": {"status": 0.0}}}


class DaliLight(DaliDevice):
    """
    Dali Light device
    """

    def __init__(self, id: int, name: str, info: str, features=None,
                 scenes=None, groups=None):
        super().__init__(id=id, name=name, info=info, type=DALI_DEVICE_LIGHT, features=features, scenes=scenes,
                         groups=groups)

    @property
    def is_on(self) -> bool:
        return self.features['switchable']['status']


class DALI2IoT:
    """
    DALI2IoT API, allow to communicate with Lunatone DALI2IOT gateway device
    Product link: https://www.lunatone.com/en/product/dali-2-iot-gateway/
    API reference: https://www.lunatone.com/wp-content/uploads/2021/08/89453886_DALI2_IOT_API_Dokumentation_EN_M0023.pdf
    """

    def __init__(self, host: str, scheme: str = "http") -> None:
        self._host = host
        self._url = f"{scheme}://{host}"
        self._version = "0.0"
        self._devices: list[DaliDevice] = []
        self._status = {"status": DALI_INIT, "error": ""}
        self._ws: websocket.WebSocketApp = None
        self._scanner: threading.Thread = None

        logging.debug(f"Init new DALI2IoT with host {host}")

    def bye(self):
        logging.debug("Bye")
        if self._ws is not None:
            logging.debug("Closing websocket")
            self._ws.close()

    @property
    def devices(self):
        """
        Return list of discovered DaliDevices
        :return:
        """
        return self._devices

    @property
    def status(self):
        """
        Return the API connection status
        {
            "status": int (required)
            "error" : string - if status is set to DALI_ERROR, this fields contains the error message
            "scan": dict (optional) - Scan status
                    scan = {
                        "id": "-1",
                        "progress": 0,
                        "found": 0,
                        "status": "not started"
                    }
        }
        :return:
        """
        return self._status['status']

    def _set_status(self, status, msg=None):

        prev = self._status

        if status == DALI_ERROR:
            self._status = {"status": DALI_ERROR, "error": msg}
        elif status == DALI_SCANNING:
            self._status = {"status": DALI_SCANNING, "error": "", "scan": msg}
        else:
            self._status = {"status": status, "error": "", "messqge": msg}

        logging.debug(f"Status changes from {prev} to {self._status}")

    async def connect(self):
        """
        Simulate connection to the gateway
        Todo: verified supported version
        """
        is_dali, ret = await self.is_dali(self.host)
        self._set_status(**ret['status'])

        if is_dali:
            self._version = ret["version"]

    @staticmethod
    async def is_dali(host: str, scheme="http") -> tuple:
        """
        Verify if the endpoint is a DALI2IoT gateway
        :return:
        """
        gw = {}

        try:
            req = requests.get(f"{scheme}://{host}/info")
            payload = req.json()

            logging.debug(f"is_dali status code {req.status_code}")

            if "name" in payload and payload["name"] == "dali-iot":
                # self._info = payload
                gw = {"status": DALI_CONNECTED, "error": "", "version": payload["version"]}
                return True, gw

            gw = {"status": DALI_ERROR, "error": "Not recognized DALI2IoT gateway"}

        except requests.RequestException:
            gw = {"status": DALI_ERROR, "error": "Connection issue"}

        return False, gw

    # Can be async
    # Can be async
    async def scan(self) -> None:
        """
        Start gateway scan. Once the scan is started; a thread is running to monitor the scan progress
        :return:
        """

        if self.status != DALI_CONNECTED:
            logging.info("Not connected to DALI. Scan aborted")
        elif self.status != DALI_SCANNING:
            logging.info("Scan started")

            scan = {
                "id": "-1",
                "progress": 0,
                "found": 0,
                "status": "not started"
            }

            self._set_status(DALI_SCANNING, scan)

            try:
                data = {"newInstallation": False, "noAddressing": False}
                scan_status = requests.post(f"{self._url}/dali/scan", json=data)

                if scan_status.status_code == 200:
                    self._set_status(DALI_SCANNING, scan_status.json())
                else:
                    self._set_status(DALI_ERROR, scan_status.text)

                # self._scanner = threading.Thread(target=self._refresh_scan_status)
                # self._scanner.start()

            except requests.RequestException:
                self._set_status(DALI_ERROR, "Error while scanning")

    async def cancel_scan(self):

        """
        Cancel the  running scan
        :return:
        """

        self._set_status(DALI_SCANNING_STOP, {
            "id": "-1",
            "progress": 0,
            "found": 0,
            "status": "cancelled"
        })

        try:
            req = requests.post(f"{self._url}/dali/scan/cancel")
        except requests.RequestException:
            self._set_status(DALI_ERROR, "Error while cancelling scan")

    def _refresh_scan_status(self) -> None:
        """
        Run in thread - pool the scan status each DALI_SCAN_INTERVAL sec
        :return:
        """
        while self.status == DALI_SCANNING and self._status['scan']['progress'] != 100:

            try:
                scan_status = requests.get(f"{self._host}/dali/scan", )

                if scan_status.status_code == 200:
                    self._status = {"status": DALI_SCANNING, "error": "", "scan": scan_status.json()}
                    logging.info("Scan progress {}".format(self._status['scan']['progress']))
                    time.sleep(DALI_SCAN_INTERVAL)
                    # await asyncio.sleep(DALI_SCAN_INTERVAL)
                else:
                    self._status = {"status": DALI_ERROR, "error": scan_status.text}

            except requests.RequestException:
                self._status = {"status": DALI_ERROR, "error": "Error while scanning"}

        if self.status == DALI_SCANNING and self._status['scan']['progress'] != 100:
            self._status = {"status": DALI_READY, "error": ""}

    def _ws_on_open(self, ws):
        logging.info("Websocket open")
        pass

    def _ws_on_message(self, ws, message):
        """
        # {"type": "devices", "data": {"devices": [{"id": 6, "features": {"switchable": {"status": false}, "dimmable": {"status": 0.0}}}]}, "timeSignature": {"timestamp": 1668027883.3452175, "counter": 5840}}

        :param ws:
        :param message:
        :return:
        """
        logging.debug(f"Received {message}")

        try:
            message = json.loads(message)

            if "type" in message and message["type"] == "devices":
                for device in message["data"]["devices"]:
                    logging.info(f"Devices update recieve for device {device['id']}")

                    for d in self._devices:
                        if d.id == device["id"]:
                            d.update(device["features"])
                            break
                        else:
                            logging.debug("New device discovered")


        except Exception as e:
            logging.critical(f"Error while parsing websocket message ({e})")

    def _ws_on_error(self, ws, error):
        logging.error(f"Websocket error {error}")

    def _ws_on_close(self, ws, close_status_code, close_msg):
        logging.info(f"Websocket closed (status={close_status_code},msg={close_msg})")
        self._ws = None

    def subscribe(self):

        logging.debug(f"Subscribing to websocket ws://{self._host}")

        def thread():
            # websocket.enableTrace(True)
            self._ws = websocket.WebSocketApp(f"ws://{self._host}",
                                              on_open=self._ws_on_open,
                                              on_message=self._ws_on_message,
                                              on_error=self._ws_on_error,
                                              on_close=self._ws_on_close)

            self._ws.run_forever(
                reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
            logging.debug("Closing subscribe thread")

        self._scanner = threading.Thread(target=thread)

        logging.debug("Opening subscribe thread")
        self._scanner.start()

    async def get_devices(self):
        """
        Fetch the available devices on the DALI BUS
        :return:
        """
        # if not self._is_scanned:
        #    await self.scan()

        try:
            req = requests.get(f"{self._url}/devices")
            payload = req.json()

            for device in payload['devices']:
                if "switchable" in device['features']:
                    self._devices.append(DaliLight(**device))
                else:
                    self._devices.append(DaliDevice(**device))

        except requests.RequestException:
            self._status = {"status": DALI_ERROR, "error": "Error while retrieving devices lists"}

    async def update_device(self, device: DaliDevice, features):
        """
        Update a device state

        204 : Successful Response
        422 : Validation Error
                {
                "detail": [
                    {
                    "loc": [
                        "string"
                    ],
                    "msg": "string",
                    "type": "string"
                    }
                ]
                }
        """
        logging.info(f"Changing device {device.id} features from {device.features} to {features}")

        try:
            req = requests.post(f"{self._url}/device/{device.id}/control", json=features)

            if not req.ok:
                logging.warning(f"Error while updating device {req.status_code} {req.text}")

        except requests.RequestException as e:
            logging.error(f"Error while updating device: {e}")

    async def turn_on(self, device: DaliDevice) -> DaliDevice:
        device = await self.update_device(device=device, features={"switchable": True})
        return device

    async def turn_off(self, device: DaliDevice) -> DaliDevice:
        device = await self.update_device(device=device, features={"switchable": False})
        return device
