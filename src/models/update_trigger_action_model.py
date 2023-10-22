from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_model import DeviceModel
    from ..models.trigger_action_source import TriggerActionSource


T = TypeVar("T", bound="UpdateTriggerActionModel")


@_attrs_define
class UpdateTriggerActionModel:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        name (Union[Unset, str]):
        sources (Union[Unset, List['TriggerActionSource']]):
        targets (Union[Unset, List['DeviceModel']]):
    """

    enabled: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    sources: Union[Unset, List["TriggerActionSource"]] = UNSET
    targets: Union[Unset, List["DeviceModel"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        name = self.name
        sources: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()

                sources.append(sources_item)

        targets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()

                targets.append(targets_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if name is not UNSET:
            field_dict["name"] = name
        if sources is not UNSET:
            field_dict["sources"] = sources
        if targets is not UNSET:
            field_dict["targets"] = targets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_model import DeviceModel
        from ..models.trigger_action_source import TriggerActionSource

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        name = d.pop("name", UNSET)

        sources = []
        _sources = d.pop("sources", UNSET)
        for sources_item_data in _sources or []:
            sources_item = TriggerActionSource.from_dict(sources_item_data)

            sources.append(sources_item)

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = DeviceModel.from_dict(targets_item_data)

            targets.append(targets_item)

        update_trigger_action_model = cls(
            enabled=enabled,
            name=name,
            sources=sources,
            targets=targets,
        )

        update_trigger_action_model.additional_properties = d
        return update_trigger_action_model

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
