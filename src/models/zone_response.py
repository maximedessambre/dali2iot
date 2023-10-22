from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_model import DeviceModel
    from ..models.signature_model import SignatureModel
    from ..models.zone_response_features import ZoneResponseFeatures


T = TypeVar("T", bound="ZoneResponse")


@_attrs_define
class ZoneResponse:
    """Represent a zone: a collection of devices (targets).

    Attributes:
        id (int): The unique identifier of the zone.
        targets (List['DeviceModel']): The effective range of the zone.
        features (ZoneResponseFeatures):
        time_signature (SignatureModel):
        name (Union[Unset, str]): A user defined, human readable name for the zone.
    """

    id: int
    targets: List["DeviceModel"]
    features: "ZoneResponseFeatures"
    time_signature: "SignatureModel"
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()

            targets.append(targets_item)

        features = self.features.to_dict()

        time_signature = self.time_signature.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "targets": targets,
                "features": features,
                "timeSignature": time_signature,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_model import DeviceModel
        from ..models.signature_model import SignatureModel
        from ..models.zone_response_features import ZoneResponseFeatures

        d = src_dict.copy()
        id = d.pop("id")

        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = DeviceModel.from_dict(targets_item_data)

            targets.append(targets_item)

        features = ZoneResponseFeatures.from_dict(d.pop("features"))

        time_signature = SignatureModel.from_dict(d.pop("timeSignature"))

        name = d.pop("name", UNSET)

        zone_response = cls(
            id=id,
            targets=targets,
            features=features,
            time_signature=time_signature,
            name=name,
        )

        zone_response.additional_properties = d
        return zone_response

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
