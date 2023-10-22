from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivePeriod")


@_attrs_define
class ActivePeriod:
    """
    Attributes:
        start_month (Union[Unset, int]):
        end_month (Union[Unset, int]):
        start_day (Union[Unset, int]):
        end_day (Union[Unset, int]):
    """

    start_month: Union[Unset, int] = UNSET
    end_month: Union[Unset, int] = UNSET
    start_day: Union[Unset, int] = UNSET
    end_day: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start_month = self.start_month
        end_month = self.end_month
        start_day = self.start_day
        end_day = self.end_day

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_month is not UNSET:
            field_dict["startMonth"] = start_month
        if end_month is not UNSET:
            field_dict["endMonth"] = end_month
        if start_day is not UNSET:
            field_dict["startDay"] = start_day
        if end_day is not UNSET:
            field_dict["endDay"] = end_day

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start_month = d.pop("startMonth", UNSET)

        end_month = d.pop("endMonth", UNSET)

        start_day = d.pop("startDay", UNSET)

        end_day = d.pop("endDay", UNSET)

        active_period = cls(
            start_month=start_month,
            end_month=end_month,
            start_day=start_day,
            end_day=end_day,
        )

        active_period.additional_properties = d
        return active_period

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
