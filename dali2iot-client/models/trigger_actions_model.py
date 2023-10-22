from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.trigger_action_model import TriggerActionModel


T = TypeVar("T", bound="TriggerActionsModel")


@_attrs_define
class TriggerActionsModel:
    """
    Attributes:
        trigger_actions (List['TriggerActionModel']):
    """

    trigger_actions: List["TriggerActionModel"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trigger_actions = []
        for trigger_actions_item_data in self.trigger_actions:
            trigger_actions_item = trigger_actions_item_data.to_dict()

            trigger_actions.append(trigger_actions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "triggerActions": trigger_actions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.trigger_action_model import TriggerActionModel

        d = src_dict.copy()
        trigger_actions = []
        _trigger_actions = d.pop("triggerActions")
        for trigger_actions_item_data in _trigger_actions:
            trigger_actions_item = TriggerActionModel.from_dict(trigger_actions_item_data)

            trigger_actions.append(trigger_actions_item)

        trigger_actions_model = cls(
            trigger_actions=trigger_actions,
        )

        trigger_actions_model.additional_properties = d
        return trigger_actions_model

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
