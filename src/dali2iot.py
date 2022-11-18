import websocket
import requests
import threading
import time
import json

from .logger import logger
from src.dali_device import DaliDevice
from src.dali_light import DaliLight


DALI_INIT = 0
DALI_CONNECTED = 1
DALI_SCANNING = 2
DALI_SCANNING_STOP = 3
DALI_READY = 4
DALI_ERROR = -1

DALI_SCAN_INTERVAL = 2



class DALI2IoT:
    """
    DALI2IoT API, allow to communicate with Lunatone DALI2IOT gateway device
    Product link: https://www.lunatone.com/en/product/dali-2-iot-gateway/
    API reference: https://www.lunatone.com/wp-content/uploads/2021/08/89453886_DALI2_IOT_API_Dokumentation_EN_M0023.pdf
    """

    def __init__(self, host: str, scheme: str = "http") -> None:
        self._host = host
        self._scheme = scheme
        self._url = f"{scheme}://{host}"
        self._version = "0.0"
        self._devices: list[DaliDevice] = []
        self._status = {"status": DALI_INIT, "error": ""}
        self._ws: websocket.WebSocketApp = None
        self._scanner: threading.Thread = None

        logger.debug(f"Init new DALI2IoT with host {host}")

    @property
    def host(self):
        return self._host

    @property
    def scheme(self):
        return self._scheme

    @property
    def version(self):
        return self._version

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
        return self._status["status"]

    def _set_status(self, status, msg=None):

        prev = self._status

        if status == DALI_ERROR:
            self._status = {"status": DALI_ERROR, "error": msg}
        elif status == DALI_SCANNING:
            self._status = {"status": DALI_SCANNING, "error": "", "scan": msg}
        else:
            self._status = {"status": status, "error": "", "message": msg}

        logger.debug(f"Status changes from {prev} to {self._status}")

    async def connect(self):
        """
        Simulate connection to the gateway
        Todo: verified supported version
        """
        is_dali, ret = await self.is_dali(host=self.host, scheme=self.scheme)
        self._set_status(ret["status"], ret["error"])

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

            logger.debug(f"is_dali status code {req.status_code}")

            if "name" in payload and payload["name"] == "dali-iot":
                # self._info = payload
                gw = {
                    "status": DALI_CONNECTED,
                    "error": "",
                    "version": payload["version"],
                }
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
            logger.info("Not connected to DALI. Scan aborted")
        elif self.status != DALI_SCANNING:
            logger.info("Scan started")

            scan = {"id": "-1", "progress": 0, "found": 0, "status": "not started"}

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

        self._set_status(
            DALI_SCANNING_STOP,
            {"id": "-1", "progress": 0, "found": 0, "status": "cancelled"},
        )

        try:
            req = requests.post(f"{self._url}/dali/scan/cancel")
        except requests.RequestException:
            self._set_status(DALI_ERROR, "Error while cancelling scan")

    def _refresh_scan_status(self) -> None:
        """
        Run in thread - pool the scan status each DALI_SCAN_INTERVAL sec
        :return:
        """
        while self.status == DALI_SCANNING and self._status["scan"]["progress"] != 100:

            try:
                scan_status = requests.get(
                    f"{self._host}/dali/scan",
                )

                if scan_status.status_code == 200:
                    self._set_status(DALI_SCANNING, scan_status.json())
                    logger.info(
                        "Scan progress {}".format(self._status["scan"]["progress"])
                    )
                    time.sleep(DALI_SCAN_INTERVAL)
                    # await asyncio.sleep(DALI_SCAN_INTERVAL)
                else:
                    self._set_status(DALI_ERROR, scan_status.text)

            except requests.RequestException:
                self._set_status(DALI_ERROR, "Error while scanning")

        if self.status == DALI_SCANNING and self._status["scan"]["progress"] != 100:
            self._set_status(DALI_READY)

    def _ws_on_open(self, ws):
        logger.info("Websocket open")
        pass

    def _ws_on_message(self, ws, message):
        """
        # {"type": "devices", "data": {"devices": [{"id": 6, "features": {"switchable": {"status": false},
        "dimmable": {"status": 0.0}}}]}, "timeSignature": {"timestamp": 1668027883.3452175, "counter": 5840}}

        :param ws:
        :param message:
        :return:
        """
        logger.debug(f"Received {message}")

        try:
            message = json.loads(message)

            if "type" in message and message["type"] == "devices":
                for device in message["data"]["devices"]:
                    logger.info(f"Devices update receive for device {device['id']}")

                    for d in self._devices:
                        if d.id == device["id"]:
                            d.update(device["features"])
                            break

        except Exception as e:
            logger.critical(f"Error while parsing websocket message ({e})")

    def _ws_on_error(self, ws, error):
        logger.error(f"Websocket error {error}")

    def _ws_on_close(self, ws, close_status_code, close_msg):
        logger.info(f"Websocket closed (status={close_status_code},msg={close_msg})")
        self._ws = None

    def subscribe(self):

        logger.debug(f"Subscribing to websocket ws://{self._host}")

        def thread():
            # websocket.enableTrace(True)
            self._ws = websocket.WebSocketApp(
                f"ws://{self._host}",
                on_open=self._ws_on_open,
                on_message=self._ws_on_message,
                on_error=self._ws_on_error,
                on_close=self._ws_on_close,
            )

            self._ws.run_forever(
                reconnect=5
            )  # Set dispatcher to automatic reconnection, 5-second reconnect delay if connection
            # closed unexpectedly
            logger.debug("Closing subscribe thread")

        self._scanner = threading.Thread(target=thread)

        logger.debug("Opening subscribe thread")
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

            for device in payload["devices"]:
                if "switchable" in device["features"]:
                    self._devices.append(DaliLight(**device))
                else:
                    self._devices.append(DaliDevice(**device))

        except requests.RequestException:
            self._status = {
                "status": DALI_ERROR,
                "error": "Error while retrieving devices lists",
            }

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
        logger.info(
            f"Changing device {device.id} features from {device.features} to {features}"
        )

        try:
            req = requests.post(
                f"{self._url}/device/{device.id}/control", json=features
            )

            if not req.ok:
                logger.warning(
                    f"Error while updating device {req.status_code} {req.text}"
                )

        except requests.RequestException as e:
            logger.error(f"Error while updating device: {e}")

    async def turn_on(self, device: DaliDevice):
        await self.update_device(device=device, features={"switchable": True})

    async def turn_off(self, device: DaliDevice):
        await self.update_device(device=device, features={"switchable": False})

    def bye(self):
        logger.debug("Bye")
        if self._ws is not None:
            logger.debug("Closing websocket")
            self._ws.close()
