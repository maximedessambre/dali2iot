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

    def __init__(self, host: str, ssl: bool = False) -> None:
        self._host = host
        self._ssl = ssl

        if ssl:
            self._scheme = "https"
        else:
            self._scheme = "http"

        self._version = "0.0"
        self._devices: list[DaliDevice] = []
        self._status = {"status": DALI_INIT, "error": ""}
        self._ws: websocket.WebSocketApp = None
        self._scanner: threading.Thread = None

        logger.debug(f"Init new DALI2IoT with host {host}")

    @property
    def host(self):
        """
        @return: gateway IP or hostname (without url scheme)
        """
        return self._host

    @property
    def uri(self):
        """
        @return: gateway uri
        """
        return f"{self._scheme}://{self._host}"

    @property
    def version(self):
        """
        @return: gateway version
        """
        return self._version

    @property
    def devices(self) -> list[DaliDevice]:
        """
        Return list of known DaliDevices
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
        """
        Set gateway FSM status
        @param status:
        @param msg: status related message
        @return:
        """

        prev = self._status

        if status == DALI_ERROR:
            self._status = {"status": DALI_ERROR, "error": msg}
        elif status == DALI_SCANNING:
            self._status = {"status": DALI_SCANNING, "error": "", "scan": msg}
            logger.error(msg)
        else:
            self._status = {"status": status, "error": "", "message": msg}

        logger.debug(f"Status changes from {prev} to {self._status}")

    async def connect(self):
        """
        Simulate connection to the gateway
        Todo: verified supported version
        """
        is_dali, ret = await self.is_dali(host=self.host, ssl=self._ssl)
        self._set_status(ret["status"], ret["error"])

        if is_dali:
            self._version = ret["version"]

    @staticmethod
    async def is_dali(host: str, ssl: bool = False) -> tuple:
        """
        Verify if the host is a DALI2IoT gateway
        :return:
        """
        gw = {}
        scheme = "http"
        if ssl:
            scheme = "https"

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

        except requests.RequestException as e:
            logger.debug(e)
            gw = {"status": DALI_ERROR, "error": "Connection issue"}

        return False, gw

    async def scan(self):
        """
        Start gateway bus scan.
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
                scan_status = requests.post(f"{self.uri}/dali/scan", json=data)

                if scan_status.status_code == 200:
                    self._set_status(DALI_SCANNING, scan_status.json())
                else:
                    self._set_status(DALI_ERROR, scan_status.text)

                # self._scanner = threading.Thread(target=self._refresh_scan_status)
                # self._scanner.start()

            except requests.RequestException as e:
                logger.debug(e)
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
            req = requests.post(f"{self.uri}/dali/scan/cancel")
        except requests.RequestException:
            self._set_status(DALI_ERROR, "Error while cancelling scan")

    def get_scan_status(self) -> None:
        """
        Run in thread - pool the scan status each DALI_SCAN_INTERVAL sec
        :return:
        """

        try:
            scan_status = requests.get(
                f"{self._host}/dali/scan",
            )

            if scan_status.status_code == 200:
                self._set_status(DALI_SCANNING, scan_status.json())
                logger.info("Scan progress {}".format(self._status["scan"]["progress"]))
            else:
                self._set_status(DALI_ERROR, scan_status.text)

        except requests.RequestException as e:
            logger.debug(e)
            self._set_status(DALI_ERROR, "Error while scanning")
        finally:
            if self.status == DALI_SCANNING and self._status["scan"]["progress"] == 100:
                self._set_status(DALI_READY)

    def _ws_on_open(self, ws):
        logger.info("Websocket open")
        pass

    def _ws_on_message(self, ws, message: str):
        """

        # {"type": "devices", "data": {"devices": [{"id": 6, "features": {"switchable": {"status": false},
        "dimmable": {"status": 0.0}}}]}, "timeSignature": {"timestamp": 1668027883.3452175, "counter": 5840}}

        :param ws:
        :param message: websocket message
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

    def monitor(self):
        """
        Start websocket listening thread
        Stores the ws in self._ws and the loop thead in self._scanner
        @return:
        """

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

        try:
            req = requests.get(f"{self.uri}/devices")
            payload = req.json()

            for device in payload["devices"]:
                if "switchable" in device["features"]:
                    self._devices.append(DaliLight(**device))
                else:
                    self._devices.append(DaliDevice(**device))

        except requests.RequestException as e:
            logger.debug(e)
            self._set_status(DALI_ERROR, "Error while retrieving devices lists")

    async def update_device(self, device: DaliDevice, features):
        """
        @param device: DaliDevice
        @param features: features dict to be updated; allowed key: name, switchable, dimmable
        """
        logger.info(
            f"Changing device {device.id} features from {device.features} to {features}"
        )

        try:
            req = requests.post(f"{self.uri}/device/{device.id}/control", json=features)

            if not req.ok:
                logger.warning(
                    f"Error while updating device {req.status_code} {req.text}"
                )

        except requests.RequestException as e:
            logger.error(f"Error while updating device: {e}")

    async def turn_on(self, device: DaliDevice):
        """
        Turn on a DaliDevice by setting `switchable` state to True
        @param device: DaliDevice
        @return:
        """

        await self.update_device(device=device, features={"switchable": True})

    async def turn_off(self, device: DaliDevice):
        """
        Turn on a DaliDevice by setting `switchable` state to False
        @param device: DaliDevice
        @return:
        """
        await self.update_device(device=device, features={"switchable": False})

    def bye(self):
        """
        Stop the websocket and ends the monitoring thread
        @return:
        """
        logger.debug("Bye")
        if self._ws is not None:
            logger.debug("Closing websocket")
            self._ws.close()
