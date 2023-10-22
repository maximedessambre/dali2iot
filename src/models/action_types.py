from enum import Enum


class ActionTypes(str, Enum):
    FEATURES = "features"

    def __str__(self) -> str:
        return str(self.value)
