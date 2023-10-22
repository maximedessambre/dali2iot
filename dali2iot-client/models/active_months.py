from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActiveMonths")


@_attrs_define
class ActiveMonths:
    """
    Attributes:
        january (Union[Unset, bool]):  Default: True.
        february (Union[Unset, bool]):  Default: True.
        march (Union[Unset, bool]):  Default: True.
        april (Union[Unset, bool]):  Default: True.
        may (Union[Unset, bool]):  Default: True.
        june (Union[Unset, bool]):  Default: True.
        july (Union[Unset, bool]):  Default: True.
        august (Union[Unset, bool]):  Default: True.
        september (Union[Unset, bool]):  Default: True.
        october (Union[Unset, bool]):  Default: True.
        november (Union[Unset, bool]):  Default: True.
        december (Union[Unset, bool]):  Default: True.
    """

    january: Union[Unset, bool] = True
    february: Union[Unset, bool] = True
    march: Union[Unset, bool] = True
    april: Union[Unset, bool] = True
    may: Union[Unset, bool] = True
    june: Union[Unset, bool] = True
    july: Union[Unset, bool] = True
    august: Union[Unset, bool] = True
    september: Union[Unset, bool] = True
    october: Union[Unset, bool] = True
    november: Union[Unset, bool] = True
    december: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        january = self.january
        february = self.february
        march = self.march
        april = self.april
        may = self.may
        june = self.june
        july = self.july
        august = self.august
        september = self.september
        october = self.october
        november = self.november
        december = self.december

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if january is not UNSET:
            field_dict["january"] = january
        if february is not UNSET:
            field_dict["february"] = february
        if march is not UNSET:
            field_dict["march"] = march
        if april is not UNSET:
            field_dict["april"] = april
        if may is not UNSET:
            field_dict["may"] = may
        if june is not UNSET:
            field_dict["june"] = june
        if july is not UNSET:
            field_dict["july"] = july
        if august is not UNSET:
            field_dict["august"] = august
        if september is not UNSET:
            field_dict["september"] = september
        if october is not UNSET:
            field_dict["october"] = october
        if november is not UNSET:
            field_dict["november"] = november
        if december is not UNSET:
            field_dict["december"] = december

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        january = d.pop("january", UNSET)

        february = d.pop("february", UNSET)

        march = d.pop("march", UNSET)

        april = d.pop("april", UNSET)

        may = d.pop("may", UNSET)

        june = d.pop("june", UNSET)

        july = d.pop("july", UNSET)

        august = d.pop("august", UNSET)

        september = d.pop("september", UNSET)

        october = d.pop("october", UNSET)

        november = d.pop("november", UNSET)

        december = d.pop("december", UNSET)

        active_months = cls(
            january=january,
            february=february,
            march=march,
            april=april,
            may=may,
            june=june,
            july=july,
            august=august,
            september=september,
            october=october,
            november=november,
            december=december,
        )

        active_months.additional_properties = d
        return active_months

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
