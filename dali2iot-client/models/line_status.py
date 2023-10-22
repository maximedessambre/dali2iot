from enum import Enum


class LineStatus(str, Enum):
    LOWPOWER = "lowPower"
    NOPOWER = "noPower"
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
