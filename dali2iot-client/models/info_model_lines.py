from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dali_bus_model import DaliBusModel


T = TypeVar("T", bound="InfoModelLines")


@_attrs_define
class InfoModelLines:
    """ """

    additional_properties: Dict[str, "DaliBusModel"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dali_bus_model import DaliBusModel

        d = src_dict.copy()
        info_model_lines = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = DaliBusModel.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        info_model_lines.additional_properties = additional_properties
        return info_model_lines

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "DaliBusModel":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "DaliBusModel") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
