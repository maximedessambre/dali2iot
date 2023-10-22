from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sequence_step import SequenceStep


T = TypeVar("T", bound="SequenceResponse")


@_attrs_define
class SequenceResponse:
    """
    Attributes:
        id (int):
        active (bool):
        steps (List['SequenceStep']):
        is_macro (bool):
        name (Union[Unset, str]):  Default: ''.
        enabled (Union[Unset, bool]):  Default: True.
        loop (Union[Unset, bool]):
        repeat (Union[Unset, int]):
    """

    id: int
    active: bool
    steps: List["SequenceStep"]
    is_macro: bool
    name: Union[Unset, str] = ""
    enabled: Union[Unset, bool] = True
    loop: Union[Unset, bool] = False
    repeat: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        active = self.active
        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()

            steps.append(steps_item)

        is_macro = self.is_macro
        name = self.name
        enabled = self.enabled
        loop = self.loop
        repeat = self.repeat

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "active": active,
                "steps": steps,
                "isMacro": is_macro,
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sequence_step import SequenceStep

        d = src_dict.copy()
        id = d.pop("id")

        active = d.pop("active")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = SequenceStep.from_dict(steps_item_data)

            steps.append(steps_item)

        is_macro = d.pop("isMacro")

        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        loop = d.pop("loop", UNSET)

        repeat = d.pop("repeat", UNSET)

        sequence_response = cls(
            id=id,
            active=active,
            steps=steps,
            is_macro=is_macro,
            name=name,
            enabled=enabled,
            loop=loop,
            repeat=repeat,
        )

        sequence_response.additional_properties = d
        return sequence_response

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
