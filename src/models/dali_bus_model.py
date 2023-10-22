from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.line_status import LineStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DaliBusModel")


@_attrs_define
class DaliBusModel:
    """
    Attributes:
        send_blocked_initialize (Union[Unset, bool]):
        send_blocked_quiescent (Union[Unset, bool]):
        send_blocked_macro_running (Union[Unset, bool]):
        send_buffer_full (Union[Unset, bool]):
        line_status (Union[Unset, LineStatus]): An enumeration. Default: LineStatus.OK.
    """

    send_blocked_initialize: Union[Unset, bool] = False
    send_blocked_quiescent: Union[Unset, bool] = False
    send_blocked_macro_running: Union[Unset, bool] = False
    send_buffer_full: Union[Unset, bool] = False
    line_status: Union[Unset, LineStatus] = LineStatus.OK
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        send_blocked_initialize = self.send_blocked_initialize
        send_blocked_quiescent = self.send_blocked_quiescent
        send_blocked_macro_running = self.send_blocked_macro_running
        send_buffer_full = self.send_buffer_full
        line_status: Union[Unset, str] = UNSET
        if not isinstance(self.line_status, Unset):
            line_status = self.line_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if send_blocked_initialize is not UNSET:
            field_dict["sendBlockedInitialize"] = send_blocked_initialize
        if send_blocked_quiescent is not UNSET:
            field_dict["sendBlockedQuiescent"] = send_blocked_quiescent
        if send_blocked_macro_running is not UNSET:
            field_dict["sendBlockedMacroRunning"] = send_blocked_macro_running
        if send_buffer_full is not UNSET:
            field_dict["sendBufferFull"] = send_buffer_full
        if line_status is not UNSET:
            field_dict["lineStatus"] = line_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        send_blocked_initialize = d.pop("sendBlockedInitialize", UNSET)

        send_blocked_quiescent = d.pop("sendBlockedQuiescent", UNSET)

        send_blocked_macro_running = d.pop("sendBlockedMacroRunning", UNSET)

        send_buffer_full = d.pop("sendBufferFull", UNSET)

        _line_status = d.pop("lineStatus", UNSET)
        line_status: Union[Unset, LineStatus]
        if isinstance(_line_status, Unset):
            line_status = UNSET
        else:
            line_status = LineStatus(_line_status)

        dali_bus_model = cls(
            send_blocked_initialize=send_blocked_initialize,
            send_blocked_quiescent=send_blocked_quiescent,
            send_blocked_macro_running=send_blocked_macro_running,
            send_buffer_full=send_buffer_full,
            line_status=line_status,
        )

        dali_bus_model.additional_properties = d
        return dali_bus_model

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
