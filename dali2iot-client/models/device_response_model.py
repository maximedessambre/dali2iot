from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.device_response_model_features import DeviceResponseModelFeatures
    from ..models.device_response_model_scenes_item import DeviceResponseModelScenesItem
    from ..models.signature_model import SignatureModel


T = TypeVar("T", bound="DeviceResponseModel")


@_attrs_define
class DeviceResponseModel:
    """
    Attributes:
        id (int):
        name (str):
        type (str):
        features (DeviceResponseModelFeatures):
        scenes (List['DeviceResponseModelScenesItem']):
        groups (List[int]):
        address (int):
        line (int):
        dali_types (List[int]):
        time_signature (SignatureModel):
    """

    id: int
    name: str
    type: str
    features: "DeviceResponseModelFeatures"
    scenes: List["DeviceResponseModelScenesItem"]
    groups: List[int]
    address: int
    line: int
    dali_types: List[int]
    time_signature: "SignatureModel"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        type = self.type
        features = self.features.to_dict()

        scenes = []
        for scenes_item_data in self.scenes:
            scenes_item = scenes_item_data.to_dict()

            scenes.append(scenes_item)

        groups = self.groups

        address = self.address
        line = self.line
        dali_types = self.dali_types

        time_signature = self.time_signature.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type,
                "features": features,
                "scenes": scenes,
                "groups": groups,
                "address": address,
                "line": line,
                "daliTypes": dali_types,
                "timeSignature": time_signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_response_model_features import DeviceResponseModelFeatures
        from ..models.device_response_model_scenes_item import DeviceResponseModelScenesItem
        from ..models.signature_model import SignatureModel

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        type = d.pop("type")

        features = DeviceResponseModelFeatures.from_dict(d.pop("features"))

        scenes = []
        _scenes = d.pop("scenes")
        for scenes_item_data in _scenes:
            scenes_item = DeviceResponseModelScenesItem.from_dict(scenes_item_data)

            scenes.append(scenes_item)

        groups = cast(List[int], d.pop("groups"))

        address = d.pop("address")

        line = d.pop("line")

        dali_types = cast(List[int], d.pop("daliTypes"))

        time_signature = SignatureModel.from_dict(d.pop("timeSignature"))

        device_response_model = cls(
            id=id,
            name=name,
            type=type,
            features=features,
            scenes=scenes,
            groups=groups,
            address=address,
            line=line,
            dali_types=dali_types,
            time_signature=time_signature,
        )

        device_response_model.additional_properties = d
        return device_response_model

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
