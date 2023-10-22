from enum import Enum


class SchedulerRecallModes(str, Enum):
    AFTERSUNRISE = "afterSunrise"
    AFTERSUNSET = "afterSunset"
    BEFORESUNRISE = "beforeSunrise"
    BEFORESUNSET = "beforeSunset"
    TIMEOFDAY = "timeOfDay"

    def __str__(self) -> str:
        return str(self.value)
