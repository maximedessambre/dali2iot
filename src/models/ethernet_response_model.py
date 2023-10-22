from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ethernet_settings_model import EthernetSettingsModel


T = TypeVar("T", bound="EthernetResponseModel")


@_attrs_define
class EthernetResponseModel:
    """
    Attributes:
        settings (EthernetSettingsModel):
        mac_address (Union[Unset, str]):  Default: 'AA:BB:CC:DD:EE:FF'.
        dhcp_lease (Union[Unset, str]):
    """

    settings: "EthernetSettingsModel"
    mac_address: Union[Unset, str] = "AA:BB:CC:DD:EE:FF"
    dhcp_lease: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        settings = self.settings.to_dict()

        mac_address = self.mac_address
        dhcp_lease = self.dhcp_lease

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "settings": settings,
            }
        )
        if mac_address is not UNSET:
            field_dict["mac_address"] = mac_address
        if dhcp_lease is not UNSET:
            field_dict["dhcp_lease"] = dhcp_lease

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ethernet_settings_model import EthernetSettingsModel

        d = src_dict.copy()
        settings = EthernetSettingsModel.from_dict(d.pop("settings"))

        mac_address = d.pop("mac_address", UNSET)

        dhcp_lease = d.pop("dhcp_lease", UNSET)

        ethernet_response_model = cls(
            settings=settings,
            mac_address=mac_address,
            dhcp_lease=dhcp_lease,
        )

        ethernet_response_model.additional_properties = d
        return ethernet_response_model

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
