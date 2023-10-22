from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="YnDescriptorModel")


@_attrs_define
class YnDescriptorModel:
    """
    Attributes:
        lines (int): Number of implemented bus lines.
        buffer_size (int): Maximum number of TX buffer entries.
        tick_resolution (int): Resolution of tick values in µs (typically 2 ms).
        max_yn_frame_size (int): Maximum number of data bytes in one Yn Frame.
        device_list_specifier (bool): Whether the device keeps device list. Refer to `Read Device List` Yn command.
    """

    lines: int
    buffer_size: int
    tick_resolution: int
    max_yn_frame_size: int
    device_list_specifier: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lines = self.lines
        buffer_size = self.buffer_size
        tick_resolution = self.tick_resolution
        max_yn_frame_size = self.max_yn_frame_size
        device_list_specifier = self.device_list_specifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lines": lines,
                "bufferSize": buffer_size,
                "tickResolution": tick_resolution,
                "maxYnFrameSize": max_yn_frame_size,
                "deviceListSpecifier": device_list_specifier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lines = d.pop("lines")

        buffer_size = d.pop("bufferSize")

        tick_resolution = d.pop("tickResolution")

        max_yn_frame_size = d.pop("maxYnFrameSize")

        device_list_specifier = d.pop("deviceListSpecifier")

        yn_descriptor_model = cls(
            lines=lines,
            buffer_size=buffer_size,
            tick_resolution=tick_resolution,
            max_yn_frame_size=max_yn_frame_size,
            device_list_specifier=device_list_specifier,
        )

        yn_descriptor_model.additional_properties = d
        return yn_descriptor_model

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
