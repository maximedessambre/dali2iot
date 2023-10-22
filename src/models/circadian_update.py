from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.circadian_curve import CircadianCurve
    from ..models.device_model import DeviceModel


T = TypeVar("T", bound="CircadianUpdate")


@_attrs_define
class CircadianUpdate:
    """
    Attributes:
        name (Union[Unset, str]):
        targets (Union[Unset, List['DeviceModel']]):
        enabled (Union[Unset, bool]):  Default: True.
        longest (Union[Unset, CircadianCurve]):
        shortest (Union[Unset, CircadianCurve]):
    """

    name: Union[Unset, str] = UNSET
    targets: Union[Unset, List["DeviceModel"]] = UNSET
    enabled: Union[Unset, bool] = True
    longest: Union[Unset, "CircadianCurve"] = UNSET
    shortest: Union[Unset, "CircadianCurve"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        targets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()

                targets.append(targets_item)

        enabled = self.enabled
        longest: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.longest, Unset):
            longest = self.longest.to_dict()

        shortest: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shortest, Unset):
            shortest = self.shortest.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if targets is not UNSET:
            field_dict["targets"] = targets
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if longest is not UNSET:
            field_dict["longest"] = longest
        if shortest is not UNSET:
            field_dict["shortest"] = shortest

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.circadian_curve import CircadianCurve
        from ..models.device_model import DeviceModel

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = DeviceModel.from_dict(targets_item_data)

            targets.append(targets_item)

        enabled = d.pop("enabled", UNSET)

        _longest = d.pop("longest", UNSET)
        longest: Union[Unset, CircadianCurve]
        if isinstance(_longest, Unset):
            longest = UNSET
        else:
            longest = CircadianCurve.from_dict(_longest)

        _shortest = d.pop("shortest", UNSET)
        shortest: Union[Unset, CircadianCurve]
        if isinstance(_shortest, Unset):
            shortest = UNSET
        else:
            shortest = CircadianCurve.from_dict(_shortest)

        circadian_update = cls(
            name=name,
            targets=targets,
            enabled=enabled,
            longest=longest,
            shortest=shortest,
        )

        circadian_update.additional_properties = d
        return circadian_update

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
