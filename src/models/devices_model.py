from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.device_base_model import DeviceBaseModel
    from ..models.signature_model import SignatureModel


T = TypeVar("T", bound="DevicesModel")


@_attrs_define
class DevicesModel:
    """
    Attributes:
        devices (List['DeviceBaseModel']):
        time_signature (SignatureModel):
    """

    devices: List["DeviceBaseModel"]
    time_signature: "SignatureModel"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        devices = []
        for devices_item_data in self.devices:
            devices_item = devices_item_data.to_dict()

            devices.append(devices_item)

        time_signature = self.time_signature.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "devices": devices,
                "timeSignature": time_signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_base_model import DeviceBaseModel
        from ..models.signature_model import SignatureModel

        d = src_dict.copy()
        devices = []
        _devices = d.pop("devices")
        for devices_item_data in _devices:
            devices_item = DeviceBaseModel.from_dict(devices_item_data)

            devices.append(devices_item)

        time_signature = SignatureModel.from_dict(d.pop("timeSignature"))

        devices_model = cls(
            devices=devices,
            time_signature=time_signature,
        )

        devices_model.additional_properties = d
        return devices_model

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
