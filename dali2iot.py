import asyncio
import requests
import threading
import logging
import sys
import time

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
    def __init__(self, id: int, name: str, info: str, type: int = DALI_DEVICE_DEFAULT, features=None, scenes=None,
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
    def __init__(self, id: int, name: str, info: str):
        super().__init__(id, name, info, type=DALI_DEVICE_LIGHT)


class DALI2IoT:
    """
    DALI2IoT API, allow to communicate with Lunatone DALI2IOT gateway device
    Product link: https://www.lunatone.com/en/product/dali-2-iot-gateway/
    API reference: https://www.lunatone.com/wp-content/uploads/2021/08/89453886_DALI2_IOT_API_Dokumentation_EN_M0023.pdf
    """

    def __init__(self, host: str) -> None:
        self._host = host
        self._version = "0.0"
        self._devices: list[DaliDevice] = []
        self._status = {"status": DALI_INIT, "error": ""}
        # self._scanner: threading.Thread = None

        logging.debug(f"Init new DALI2IoT with host {host}")

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

    async def connect(self):
        """
        Simulate connection to the gateway
        Todo: verified supported version
        """
        try:
            await self.is_dali()
        except requests.RequestException:
            self._status = {"status": DALI_ERROR, "error": "Connection issue"}

    async def is_dali(self) -> bool:
        """
        Verify if the endpoint is a DALI2IoT gateway
        :return:
        """
        req = requests.get(f"{self._host}/info")
        payload = req.json()

        if "name" in payload and payload["name"] == "dali-iot":
            # self._info = payload
            self._version = payload["version"]
            logging.info("Gateway info {}".format(payload))

            self._status = {"status": DALI_CONNECTED, "error": ""}
            return True
        else:
            self._status = {"status": DALI_ERROR, "error": "Not recognized DALI2IoT gateway"}
            return False

    # Can be async
    async def scan(self) -> None:
        """
        Start gateway scan. Once the scan is started; a thread is ran to monitor the scan progress
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

            self._status = {"status": DALI_SCANNING, "error": "", "scan": scan}

            try:
                data = {"newInstallation": False, "noAddressing": False}
                scan_status = requests.post(f"{self._host}/dali/scan", json=data)

                if scan_status.status_code == 200:
                    self._status = {"status": DALI_SCANNING, "error": "", "scan": scan_status.json()}
                else:
                    self._status = {"status": DALI_ERROR, "error": scan_status.text}

                self._scanner = threading.Thread(target=self._refresh_scan_status)
                self._scanner.start()

            except requests.RequestException:
                self._status = {"status": DALI_ERROR, "error": "Error while scanning"}

    async def cancel_scan(self):

        """
        Cancel the  running scan
        :return:
        """

        self._status = {"status": DALI_SCANNING_STOP, "error": "", "scan": {
            "id": "-1",
            "progress": 0,
            "found": 0,
            "status": "cancelled"
        }}

        try:
            req = requests.post(f"{self._host}/dali/scan/cancel")
        except requests.RequestException:
            self._status = {"status": DALI_ERROR, "error": "Error while cancelling scan"}

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

    async def get_devices(self) -> list[DaliDevice]:
        """
        Fetch the available devices on the DALI BUS
        :return:
        """
        # if not self._is_scanned:
        #    await self.scan()

        try:
            req = requests.get(f"{self._host}/devices")
            payload = req.json()
            logging.debug(payload)
            self._devices = [DaliDevice(**device) for device in payload["devices"]]

        except requests.RequestException:
            self._status = {"status": DALI_ERROR, "error": "Error while retreiving devices lists"}

    async def update_device(self, device: DaliDevice, features) -> DaliDevice:
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
        req = requests.post(f"{self._host}/device/{device.id}/control", json=features)

        device.features.update(features)
        return device

    async def turn_on(self, device: DaliDevice) -> DaliDevice:
        device = await self.update_device(device=device, features={"switchable": True})
        return device

    async def turn_off(self, device: DaliDevice) -> DaliDevice:
        device = await self.update_device(device=device, features={"switchable": False})
        return device
