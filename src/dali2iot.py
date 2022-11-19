import json
import asyncio
import aiohttp

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

    def __init__(self, host: str, ssl: bool = False):
        self._host = host
        self._ssl = ssl
        self._version = "0.0"
        self._devices: list[DaliDevice] = []
        self._status = DALI_INIT
        self._error = ""
        self._scanner = {"id": "-1", "progress": 0, "found": 0, "status": "not started"}

        logger.debug(f"Init new DALI2IoT with host {host}")

    @property
    def host(self) -> str:
        return self._host

    @property
    def version(self) -> str:
        return self._version

    @property
    def devices(self) -> list[DaliDevice]:
        return self._devices

    @property
    def status(self) -> int:
        return self._status

    @property
    def error(self) -> str:
        return self._error

    @error.setter
    def error(self, error_msg: str):
        self._status = DALI_ERROR
        self._error = error_msg

    async def _get(self, uri):
        scheme = "http"
        if self._ssl:
            scheme = "http"

        async with aiohttp.ClientSession() as session:
            async with session.get(f"{scheme}://{self._host}{uri}") as resp:
                return resp.ok, await resp.json()

    async def _post(self, uri, data=None):

        if data is None:
            data = {}

        scheme = "http"
        if self.ssl:
            scheme = "https"

        async with aiohttp.ClientSession() as session:
            async with session.post(f"{scheme}://{self._host}{uri}", json=data) as resp:
                return resp.ok, await resp.json()

    @staticmethod
    async def is_dali(host: str, ssl: bool = False) -> tuple:
        """
        Verify if the host is a DALI2IoT gateway
        :return:
        """
        scheme = "http"
        if ssl:
            scheme = "https"

        async with aiohttp.ClientSession() as session:
            async with session.get(f"{scheme}://{host}/info") as resp:
                try:

                    logger.debug(f"is_dali status code {resp.status}")

                    if not resp.ok:
                        return (
                            False,
                            f"Error code {resp.status} — Not recognized DALI2IoT gateway",
                        )

                    payload = await resp.json()

                    if "name" in payload and payload["name"] == "dali-iot":
                        logger.debug(payload)
                        return True, payload["version"]
                    else:
                        return (
                            False,
                            f"Not recognized DALI2IoT gateway — dali-iot key not found",
                        )

                except aiohttp.ClientConnectorError as client_conn_err:
                    logger.error(
                        f"Connection to dali gateway error ({client_conn_err})"
                    )
                    return (
                        False,
                        f"Connection to dali gateway error ({client_conn_err})",
                    )

    async def connect(self):
        """
        Simulate connection to the gateway
        Todo: verified supported version
        """
        is_dali, response = await self.is_dali(host=self.host, ssl=self._ssl)

        if is_dali:
            self._status = DALI_CONNECTED
            self._version = response
        else:
            self.error = response

    async def scan(self):
        """
        Start gateway bus scan.
        :return:
        """

        if self.status != DALI_CONNECTED:
            logger.info("Not connected to DALI. Scan aborted")

        elif self.status != DALI_SCANNING:

            logger.info("Scan started")
            self._status = DALI_SCANNING

            try:
                data = {"newInstallation": False, "noAddressing": False}
                ok, response = self._post("/dali/scan", data=data)

                if ok:
                    self._scanner = response
                else:
                    self.error = response

            except aiohttp.ClientConnectorError as client_conn_err:
                self.error = f"Error while starting BUS scan ({client_conn_err})"

    async def cancel_scan(self):
        """
        Cancel the  running scan
        :return:
        """

        if self.status == DALI_SCANNING:

            self._scanner = {
                "id": "-1",
                "progress": 0,
                "found": 0,
                "status": "cancelled",
            }

            try:
                ok, response = await self._post(f"/dali/scan/cancel")

                if not ok:
                    self.error = f"Error while cancelling scan {response}"

            except aiohttp.ClientConnectorError as client_conn_err:
                self.error = f"Error while cancelling BUS scan ({client_conn_err})"

    def get_scan_status(self) -> None:
        """
        Run in thread - pool the scan status each DALI_SCAN_INTERVAL sec
        :return:
        """

        try:
            ok, response = await self._get("/dali/scan")

            if ok:
                self._status = DALI_SCANNING
                self._scanner = response

                if "progress" in response:
                    logger.info("Scan progress {}".format(self._scanner["progress"]))
                    if response["progress"] == "100":
                        self.status = DALI_READY
            else:
                self.error = response

        except aiohttp.ClientConnectorError as client_conn_err:
            self.error = f"Error while getting BUS scan status ({client_conn_err})"

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

    def monitor(self):
        """
        Start websocket listening thread
        Stores the ws in self._ws and the loop thead in self._scanner
        @return:
        """
        logger.debug(f"Subscribing to websocket ws://{self._host}")
        logger.debug("Opening subscribe thread")

    async def get_devices(self):
        """
        Fetch the available devices on the DALI BUS
        :return:
        """

        try:
            ok, response = await self._get("/devices")

            if ok:
                for device in response["devices"]:
                    if "switchable" in device["features"]:
                        self._devices.append(DaliLight(**device))
                    else:
                        self._devices.append(DaliDevice(**device))
        except aiohttp.ClientConnectorError as client_conn_err:
            self.error = f"Error while retrieving devices lists ({client_conn_err})"

    async def update_device(self, device: DaliDevice, features):
        """
        @param device: DaliDevice
        @param features: features dict to be updated; allowed key: name, switchable, dimmable
        """
        logger.info(
            f"Update device {device.id} features from {device.features} to {features}"
        )

        try:
            ok, response = await self._post(
                f"/device/{device.id}/control", data=features
            )

            if not ok:
                logger.warning(f"Error while updating device {response}")

        except aiohttp.ClientConnectorError as client_conn_err:
            self.error = f"Error while updating device {device} ({client_conn_err})"

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
