from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sequence_response import SequenceResponse


T = TypeVar("T", bound="AllSequenceResponse")


@_attrs_define
class AllSequenceResponse:
    """
    Attributes:
        sequences (List['SequenceResponse']):
    """

    sequences: List["SequenceResponse"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sequences = []
        for sequences_item_data in self.sequences:
            sequences_item = sequences_item_data.to_dict()

            sequences.append(sequences_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sequences": sequences,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sequence_response import SequenceResponse

        d = src_dict.copy()
        sequences = []
        _sequences = d.pop("sequences")
        for sequences_item_data in _sequences:
            sequences_item = SequenceResponse.from_dict(sequences_item_data)

            sequences.append(sequences_item)

        all_sequence_response = cls(
            sequences=sequences,
        )

        all_sequence_response.additional_properties = d
        return all_sequence_response

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
