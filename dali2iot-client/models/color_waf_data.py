from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ColorWAFData")


@_attrs_define
class ColorWAFData:
    """Data model for the ``colorWAF`` feature.

    Attributes:
        w (Union[Unset, float]): Relative white value in the [0, 1] interval.
        a (Union[Unset, float]): Relative amber value in the [0, 1] interval. Example: 0.5.
        f (Union[Unset, float]): Relative free color value in the [0, 1] interval. Example: 1.0.
    """

    w: Union[Unset, float] = UNSET
    a: Union[Unset, float] = UNSET
    f: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        w = self.w
        a = self.a
        f = self.f

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if w is not UNSET:
            field_dict["w"] = w
        if a is not UNSET:
            field_dict["a"] = a
        if f is not UNSET:
            field_dict["f"] = f

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        w = d.pop("w", UNSET)

        a = d.pop("a", UNSET)

        f = d.pop("f", UNSET)

        color_waf_data = cls(
            w=w,
            a=a,
            f=f,
        )

        color_waf_data.additional_properties = d
        return color_waf_data

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
