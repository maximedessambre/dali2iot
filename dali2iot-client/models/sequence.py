from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sequence_step import SequenceStep


T = TypeVar("T", bound="Sequence")


@_attrs_define
class Sequence:
    """
    Attributes:
        steps (List['SequenceStep']):
        name (Union[Unset, str]):  Default: ''.
        enabled (Union[Unset, bool]):  Default: True.
        loop (Union[Unset, bool]):
        repeat (Union[Unset, int]):
        is_macro (Union[Unset, bool]): Whether the sequence is a DALI macro.
    """

    steps: List["SequenceStep"]
    name: Union[Unset, str] = ""
    enabled: Union[Unset, bool] = True
    loop: Union[Unset, bool] = False
    repeat: Union[Unset, int] = UNSET
    is_macro: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()

            steps.append(steps_item)

        name = self.name
        enabled = self.enabled
        loop = self.loop
        repeat = self.repeat
        is_macro = self.is_macro

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "steps": steps,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if loop is not UNSET:
            field_dict["loop"] = loop
        if repeat is not UNSET:
            field_dict["repeat"] = repeat
        if is_macro is not UNSET:
            field_dict["isMacro"] = is_macro

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sequence_step import SequenceStep

        d = src_dict.copy()
        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = SequenceStep.from_dict(steps_item_data)

            steps.append(steps_item)

        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        loop = d.pop("loop", UNSET)

        repeat = d.pop("repeat", UNSET)

        is_macro = d.pop("isMacro", UNSET)

        sequence = cls(
            steps=steps,
            name=name,
            enabled=enabled,
            loop=loop,
            repeat=repeat,
            is_macro=is_macro,
        )

        sequence.additional_properties = d
        return sequence

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
