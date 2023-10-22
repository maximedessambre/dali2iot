from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.circadian_curve import CircadianCurve
    from ..models.device_model import DeviceModel
    from ..models.signature_model import SignatureModel


T = TypeVar("T", bound="CircadianResponse")


@_attrs_define
class CircadianResponse:
    """
    Attributes:
        targets (List['DeviceModel']):
        longest (CircadianCurve):
        shortest (CircadianCurve):
        id (int):
        time_signature (SignatureModel):
        name (Union[Unset, str]):  Default: ''.
        enabled (Union[Unset, bool]):  Default: True.
    """

    targets: List["DeviceModel"]
    longest: "CircadianCurve"
    shortest: "CircadianCurve"
    id: int
    time_signature: "SignatureModel"
    name: Union[Unset, str] = ""
    enabled: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()

            targets.append(targets_item)

        longest = self.longest.to_dict()

        shortest = self.shortest.to_dict()

        id = self.id
        time_signature = self.time_signature.to_dict()

        name = self.name
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targets": targets,
                "longest": longest,
                "shortest": shortest,
                "id": id,
                "timeSignature": time_signature,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.circadian_curve import CircadianCurve
        from ..models.device_model import DeviceModel
        from ..models.signature_model import SignatureModel

        d = src_dict.copy()
        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = DeviceModel.from_dict(targets_item_data)

            targets.append(targets_item)

        longest = CircadianCurve.from_dict(d.pop("longest"))

        shortest = CircadianCurve.from_dict(d.pop("shortest"))

        id = d.pop("id")

        time_signature = SignatureModel.from_dict(d.pop("timeSignature"))

        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        circadian_response = cls(
            targets=targets,
            longest=longest,
            shortest=shortest,
            id=id,
            time_signature=time_signature,
            name=name,
            enabled=enabled,
        )

        circadian_response.additional_properties = d
        return circadian_response

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
