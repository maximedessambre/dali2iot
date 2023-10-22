from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActiveWeekDays")


@_attrs_define
class ActiveWeekDays:
    """
    Attributes:
        monday (Union[Unset, bool]):  Default: True.
        tuesday (Union[Unset, bool]):  Default: True.
        wednesday (Union[Unset, bool]):  Default: True.
        thursday (Union[Unset, bool]):  Default: True.
        friday (Union[Unset, bool]):  Default: True.
        saturday (Union[Unset, bool]):  Default: True.
        sunday (Union[Unset, bool]):  Default: True.
    """

    monday: Union[Unset, bool] = True
    tuesday: Union[Unset, bool] = True
    wednesday: Union[Unset, bool] = True
    thursday: Union[Unset, bool] = True
    friday: Union[Unset, bool] = True
    saturday: Union[Unset, bool] = True
    sunday: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        monday = self.monday
        tuesday = self.tuesday
        wednesday = self.wednesday
        thursday = self.thursday
        friday = self.friday
        saturday = self.saturday
        sunday = self.sunday

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monday is not UNSET:
            field_dict["monday"] = monday
        if tuesday is not UNSET:
            field_dict["tuesday"] = tuesday
        if wednesday is not UNSET:
            field_dict["wednesday"] = wednesday
        if thursday is not UNSET:
            field_dict["thursday"] = thursday
        if friday is not UNSET:
            field_dict["friday"] = friday
        if saturday is not UNSET:
            field_dict["saturday"] = saturday
        if sunday is not UNSET:
            field_dict["sunday"] = sunday

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        monday = d.pop("monday", UNSET)

        tuesday = d.pop("tuesday", UNSET)

        wednesday = d.pop("wednesday", UNSET)

        thursday = d.pop("thursday", UNSET)

        friday = d.pop("friday", UNSET)

        saturday = d.pop("saturday", UNSET)

        sunday = d.pop("sunday", UNSET)

        active_week_days = cls(
            monday=monday,
            tuesday=tuesday,
            wednesday=wednesday,
            thursday=thursday,
            friday=friday,
            saturday=saturday,
            sunday=sunday,
        )

        active_week_days.additional_properties = d
        return active_week_days

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
