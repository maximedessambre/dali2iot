from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_types import ActionTypes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sequencer_action import SequencerAction


T = TypeVar("T", bound="SequenceStep")


@_attrs_define
class SequenceStep:
    """
    Attributes:
        type (ActionTypes): An enumeration.
        data (SequencerAction):
        enabled (Union[Unset, bool]):  Default: True.
        delay (Union[Unset, float]): delay in seconds Example: 0.1.
    """

    type: ActionTypes
    data: "SequencerAction"
    enabled: Union[Unset, bool] = True
    delay: Union[Unset, float] = 0.0
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        data = self.data.to_dict()

        enabled = self.enabled
        delay = self.delay

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "data": data,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if delay is not UNSET:
            field_dict["delay"] = delay

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sequencer_action import SequencerAction

        d = src_dict.copy()
        type = ActionTypes(d.pop("type"))

        data = SequencerAction.from_dict(d.pop("data"))

        enabled = d.pop("enabled", UNSET)

        delay = d.pop("delay", UNSET)

        sequence_step = cls(
            type=type,
            data=data,
            enabled=enabled,
            delay=delay,
        )

        sequence_step.additional_properties = d
        return sequence_step

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
