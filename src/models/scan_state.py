from enum import Enum


class ScanState(str, Enum):
    ADDRESSING = "addressing"
    CANCELLED = "cancelled"
    DONE = "done"
    IN_PROGRESS = "in progress"
    NOT_STARTED = "not started"

    def __str__(self) -> str:
        return str(self.value)
