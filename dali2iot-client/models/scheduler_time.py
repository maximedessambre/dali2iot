from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchedulerTime")


@_attrs_define
class SchedulerTime:
    """
    Attributes:
        hour (Union[Unset, int]):
        minute (Union[Unset, int]):
        second (Union[Unset, int]):
    """

    hour: Union[Unset, int] = UNSET
    minute: Union[Unset, int] = UNSET
    second: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hour = self.hour
        minute = self.minute
        second = self.second

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hour is not UNSET:
            field_dict["hour"] = hour
        if minute is not UNSET:
            field_dict["minute"] = minute
        if second is not UNSET:
            field_dict["second"] = second

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hour = d.pop("hour", UNSET)

        minute = d.pop("minute", UNSET)

        second = d.pop("second", UNSET)

        scheduler_time = cls(
            hour=hour,
            minute=minute,
            second=second,
        )

        scheduler_time.additional_properties = d
        return scheduler_time

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
