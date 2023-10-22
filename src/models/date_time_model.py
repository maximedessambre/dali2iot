from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DateTimeModel")


@_attrs_define
class DateTimeModel:
    """
    Attributes:
        timezone (Union[Unset, str]):
        automatic_time (Union[Unset, bool]):
        date (Union[Unset, str]):
        time (Union[Unset, str]):
    """

    timezone: Union[Unset, str] = UNSET
    automatic_time: Union[Unset, bool] = UNSET
    date: Union[Unset, str] = UNSET
    time: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timezone = self.timezone
        automatic_time = self.automatic_time
        date = self.date
        time = self.time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if automatic_time is not UNSET:
            field_dict["automatic_time"] = automatic_time
        if date is not UNSET:
            field_dict["date"] = date
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timezone = d.pop("timezone", UNSET)

        automatic_time = d.pop("automatic_time", UNSET)

        date = d.pop("date", UNSET)

        time = d.pop("time", UNSET)

        date_time_model = cls(
            timezone=timezone,
            automatic_time=automatic_time,
            date=date,
            time=time,
        )

        date_time_model.additional_properties = d
        return date_time_model

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
