from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trigger_action_source_type import TriggerActionSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggerActionSource")


@_attrs_define
class TriggerActionSource:
    """
    Attributes:
        type (TriggerActionSourceType): An enumeration.
        id (Union[Unset, int]): Unique identifier of a device or group. Required for ``device`` and ``group`` type,
            omitted for ``d16group`` and ``d16address``.
        address (Union[Unset, int]): Address of a DALI gear or DALI group. Required for ``d16group`` and ``d16address``
            type, omitted for ``device`` and ``group``.
        line (Union[Unset, int]): Line number of a DALI gear or DALI group. Required for ``d16group`` and ``d16address``
            type, omitted for ``device`` and ``group``.
    """

    type: TriggerActionSourceType
    id: Union[Unset, int] = UNSET
    address: Union[Unset, int] = UNSET
    line: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        id = self.id
        address = self.address
        line = self.line

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if address is not UNSET:
            field_dict["address"] = address
        if line is not UNSET:
            field_dict["line"] = line

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = TriggerActionSourceType(d.pop("type"))

        id = d.pop("id", UNSET)

        address = d.pop("address", UNSET)

        line = d.pop("line", UNSET)

        trigger_action_source = cls(
            type=type,
            id=id,
            address=address,
            line=line,
        )

        trigger_action_source.additional_properties = d
        return trigger_action_source

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
