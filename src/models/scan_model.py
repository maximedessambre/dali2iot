from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scan_state import ScanState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScanModel")


@_attrs_define
class ScanModel:
    """
    Attributes:
        id (Union[Unset, str]):  Default: ''.
        progress (Union[Unset, float]):
        found (Union[Unset, int]):
        found_sensors (Union[Unset, int]):
        status (Union[Unset, ScanState]): An enumeration. Default: ScanState.NOT_STARTED.
    """

    id: Union[Unset, str] = ""
    progress: Union[Unset, float] = UNSET
    found: Union[Unset, int] = UNSET
    found_sensors: Union[Unset, int] = UNSET
    status: Union[Unset, ScanState] = ScanState.NOT_STARTED
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        progress = self.progress
        found = self.found
        found_sensors = self.found_sensors
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if progress is not UNSET:
            field_dict["progress"] = progress
        if found is not UNSET:
            field_dict["found"] = found
        if found_sensors is not UNSET:
            field_dict["foundSensors"] = found_sensors
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        progress = d.pop("progress", UNSET)

        found = d.pop("found", UNSET)

        found_sensors = d.pop("foundSensors", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ScanState]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ScanState(_status)

        scan_model = cls(
            id=id,
            progress=progress,
            found=found,
            found_sensors=found_sensors,
            status=status,
        )

        scan_model.additional_properties = d
        return scan_model

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
