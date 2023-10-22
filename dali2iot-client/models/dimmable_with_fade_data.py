from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DimmableWithFadeData")


@_attrs_define
class DimmableWithFadeData:
    """
    Attributes:
        fade_time (float):
        dim_value (float):
    """

    fade_time: float
    dim_value: float
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fade_time = self.fade_time
        dim_value = self.dim_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fadeTime": fade_time,
                "dimValue": dim_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fade_time = d.pop("fadeTime")

        dim_value = d.pop("dimValue")

        dimmable_with_fade_data = cls(
            fade_time=fade_time,
            dim_value=dim_value,
        )

        dimmable_with_fade_data.additional_properties = d
        return dimmable_with_fade_data

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
