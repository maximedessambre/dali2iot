from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartScanModel")


@_attrs_define
class StartScanModel:
    """
    Attributes:
        new_installation (Union[Unset, bool]):
        no_addressing (Union[Unset, bool]):
        use_lines (Union[Unset, List[int]]):
    """

    new_installation: Union[Unset, bool] = False
    no_addressing: Union[Unset, bool] = False
    use_lines: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new_installation = self.new_installation
        no_addressing = self.no_addressing
        use_lines: Union[Unset, List[int]] = UNSET
        if not isinstance(self.use_lines, Unset):
            use_lines = self.use_lines

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_installation is not UNSET:
            field_dict["newInstallation"] = new_installation
        if no_addressing is not UNSET:
            field_dict["noAddressing"] = no_addressing
        if use_lines is not UNSET:
            field_dict["useLines"] = use_lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_installation = d.pop("newInstallation", UNSET)

        no_addressing = d.pop("noAddressing", UNSET)

        use_lines = cast(List[int], d.pop("useLines", UNSET))

        start_scan_model = cls(
            new_installation=new_installation,
            no_addressing=no_addressing,
            use_lines=use_lines,
        )

        start_scan_model.additional_properties = d
        return start_scan_model

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
