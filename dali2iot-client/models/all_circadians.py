from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.circadian import Circadian
    from ..models.signature_model import SignatureModel


T = TypeVar("T", bound="AllCircadians")


@_attrs_define
class AllCircadians:
    """
    Attributes:
        circadians (List['Circadian']):
        time_signature (SignatureModel):
    """

    circadians: List["Circadian"]
    time_signature: "SignatureModel"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        circadians = []
        for circadians_item_data in self.circadians:
            circadians_item = circadians_item_data.to_dict()

            circadians.append(circadians_item)

        time_signature = self.time_signature.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "circadians": circadians,
                "timeSignature": time_signature,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.circadian import Circadian
        from ..models.signature_model import SignatureModel

        d = src_dict.copy()
        circadians = []
        _circadians = d.pop("circadians")
        for circadians_item_data in _circadians:
            circadians_item = Circadian.from_dict(circadians_item_data)

            circadians.append(circadians_item)

        time_signature = SignatureModel.from_dict(d.pop("timeSignature"))

        all_circadians = cls(
            circadians=circadians,
            time_signature=time_signature,
        )

        all_circadians.additional_properties = d
        return all_circadians

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
