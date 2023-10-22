from enum import Enum


class TriggerActionSourceType(str, Enum):
    D16GEAR = "d16gear"
    D16GROUP = "d16group"
    DEVICE = "device"
    GROUP = "group"

    def __str__(self) -> str:
        return str(self.value)
