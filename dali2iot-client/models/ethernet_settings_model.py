from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EthernetSettingsModel")


@_attrs_define
class EthernetSettingsModel:
    """
    Attributes:
        dhcp (Union[Unset, bool]):
        ip_address (Union[Unset, str]):
        subnet_mask (Union[Unset, str]):
        gateway (Union[Unset, str]):
        nameservers (Union[Unset, List[str]]):
    """

    dhcp: Union[Unset, bool] = UNSET
    ip_address: Union[Unset, str] = UNSET
    subnet_mask: Union[Unset, str] = UNSET
    gateway: Union[Unset, str] = UNSET
    nameservers: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dhcp = self.dhcp
        ip_address = self.ip_address
        subnet_mask = self.subnet_mask
        gateway = self.gateway
        nameservers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.nameservers, Unset):
            nameservers = self.nameservers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dhcp is not UNSET:
            field_dict["dhcp"] = dhcp
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if subnet_mask is not UNSET:
            field_dict["subnet_mask"] = subnet_mask
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if nameservers is not UNSET:
            field_dict["nameservers"] = nameservers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dhcp = d.pop("dhcp", UNSET)

        ip_address = d.pop("ip_address", UNSET)

        subnet_mask = d.pop("subnet_mask", UNSET)

        gateway = d.pop("gateway", UNSET)

        nameservers = cast(List[str], d.pop("nameservers", UNSET))

        ethernet_settings_model = cls(
            dhcp=dhcp,
            ip_address=ip_address,
            subnet_mask=subnet_mask,
            gateway=gateway,
            nameservers=nameservers,
        )

        ethernet_settings_model.additional_properties = d
        return ethernet_settings_model

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
