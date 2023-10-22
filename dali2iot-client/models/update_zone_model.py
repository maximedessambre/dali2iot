from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_model import DeviceModel
    from ..models.update_zone_model_features import UpdateZoneModelFeatures


T = TypeVar("T", bound="UpdateZoneModel")


@_attrs_define
class UpdateZoneModel:
    """
    Attributes:
        name (Union[Unset, str]): A user defined, human readable name for the zone. Example: DALI broadcast on lines
            0-3.
        targets (Union[Unset, List['DeviceModel']]): The effective range of the zone. Example: [{'type': 'broadcast',
            'id': 0}, {'type': 'broadcast', 'id': 1}, {'type': 'broadcast', 'id': 2}, {'type': 'broadcast', 'id': 3}].
        features (Union[Unset, UpdateZoneModelFeatures]):
    """

    name: Union[Unset, str] = UNSET
    targets: Union[Unset, List["DeviceModel"]] = UNSET
    features: Union[Unset, "UpdateZoneModelFeatures"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        targets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()

                targets.append(targets_item)

        features: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.features, Unset):
            features = self.features.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if targets is not UNSET:
            field_dict["targets"] = targets
        if features is not UNSET:
            field_dict["features"] = features

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_model import DeviceModel
        from ..models.update_zone_model_features import UpdateZoneModelFeatures

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = DeviceModel.from_dict(targets_item_data)

            targets.append(targets_item)

        _features = d.pop("features", UNSET)
        features: Union[Unset, UpdateZoneModelFeatures]
        if isinstance(_features, Unset):
            features = UNSET
        else:
            features = UpdateZoneModelFeatures.from_dict(_features)

        update_zone_model = cls(
            name=name,
            targets=targets,
            features=features,
        )

        update_zone_model.additional_properties = d
        return update_zone_model

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
