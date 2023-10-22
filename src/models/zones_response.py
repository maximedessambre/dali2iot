from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.signature_model import SignatureModel
    from ..models.zone_model import ZoneModel


T = TypeVar("T", bound="ZonesResponse")


@_attrs_define
class ZonesResponse:
    """
    Attributes:
        zones (List['ZoneModel']):
        time_signature (SignatureModel):
    """

    zones: List["ZoneModel"]
    time_signature: "SignatureModel"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        zones = []
        for zones_item_data in self.zones:
            zones_item = zones_item_data.to_dict()

            zones.append(zones_item)

        time_signature = self.time_signature.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "zones": zones,
                "timeSignature": time_signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.signature_model import SignatureModel
        from ..models.zone_model import ZoneModel

        d = src_dict.copy()
        zones = []
        _zones = d.pop("zones")
        for zones_item_data in _zones:
            zones_item = ZoneModel.from_dict(zones_item_data)

            zones.append(zones_item)

        time_signature = SignatureModel.from_dict(d.pop("timeSignature"))

        zones_response = cls(
            zones=zones,
            time_signature=time_signature,
        )

        zones_response.additional_properties = d
        return zones_response

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
