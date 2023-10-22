from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.color_waf_data import ColorWAFData


T = TypeVar("T", bound="ColorWAFWithFadeData")


@_attrs_define
class ColorWAFWithFadeData:
    """
    Attributes:
        fade_time (float):
        color (ColorWAFData): Data model for the ``colorWAF`` feature.
    """

    fade_time: float
    color: "ColorWAFData"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fade_time = self.fade_time
        color = self.color.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fadeTime": fade_time,
                "color": color,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.color_waf_data import ColorWAFData

        d = src_dict.copy()
        fade_time = d.pop("fadeTime")

        color = ColorWAFData.from_dict(d.pop("color"))

        color_waf_with_fade_data = cls(
            fade_time=fade_time,
            color=color,
        )

        color_waf_with_fade_data.additional_properties = d
        return color_waf_with_fade_data

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
