from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sequence_step import SequenceStep


T = TypeVar("T", bound="SequenceUpdate")


@_attrs_define
class SequenceUpdate:
    """
    Attributes:
        name (Union[Unset, str]):
        loop (Union[Unset, bool]):
        repeat (Union[Unset, int]):
        enabled (Union[Unset, bool]):
        active (Union[Unset, bool]):
        steps (Union[Unset, List['SequenceStep']]):
    """

    name: Union[Unset, str] = UNSET
    loop: Union[Unset, bool] = UNSET
    repeat: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    active: Union[Unset, bool] = UNSET
    steps: Union[Unset, List["SequenceStep"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        loop = self.loop
        repeat = self.repeat
        enabled = self.enabled
        active = self.active
        steps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()

                steps.append(steps_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if loop is not UNSET:
            field_dict["loop"] = loop
        if repeat is not UNSET:
            field_dict["repeat"] = repeat
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if active is not UNSET:
            field_dict["active"] = active
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sequence_step import SequenceStep

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        loop = d.pop("loop", UNSET)

        repeat = d.pop("repeat", UNSET)

        enabled = d.pop("enabled", UNSET)

        active = d.pop("active", UNSET)

        steps = []
        _steps = d.pop("steps", UNSET)
        for steps_item_data in _steps or []:
            steps_item = SequenceStep.from_dict(steps_item_data)

            steps.append(steps_item)

        sequence_update = cls(
            name=name,
            loop=loop,
            repeat=repeat,
            enabled=enabled,
            active=active,
            steps=steps,
        )

        sequence_update.additional_properties = d
        return sequence_update

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
