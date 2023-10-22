from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CircadianStep")


@_attrs_define
class CircadianStep:
    """
    Attributes:
        hour (int):
        dimmable (Union[Unset, float]):  Example: 50.0.
        color_kelvin (Union[Unset, float]):  Example: 4000.0.
    """

    hour: int
    dimmable: Union[Unset, float] = UNSET
    color_kelvin: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hour = self.hour
        dimmable = self.dimmable
        color_kelvin = self.color_kelvin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hour": hour,
            }
        )
        if dimmable is not UNSET:
            field_dict["dimmable"] = dimmable
        if color_kelvin is not UNSET:
            field_dict["colorKelvin"] = color_kelvin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hour = d.pop("hour")

        dimmable = d.pop("dimmable", UNSET)

        color_kelvin = d.pop("colorKelvin", UNSET)

        circadian_step = cls(
            hour=hour,
            dimmable=dimmable,
            color_kelvin=color_kelvin,
        )

        circadian_step.additional_properties = d
        return circadian_step

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
