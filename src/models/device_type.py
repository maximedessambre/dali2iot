from enum import Enum


class DeviceType(str, Enum):
    BROADCAST = "broadcast"
    DEVICE = "device"
    GROUP = "group"
    ZONE = "zone"

    def __str__(self) -> str:
        return str(self.value)
