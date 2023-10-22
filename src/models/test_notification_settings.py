from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestNotificationSettings")


@_attrs_define
class TestNotificationSettings:
    """Configure whether to notify test success or failure, by mail.

    Attributes:
        send_on_success (Union[Unset, bool]):
        send_on_failure (Union[Unset, bool]):
    """

    send_on_success: Union[Unset, bool] = UNSET
    send_on_failure: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        send_on_success = self.send_on_success
        send_on_failure = self.send_on_failure

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if send_on_success is not UNSET:
            field_dict["sendOnSuccess"] = send_on_success
        if send_on_failure is not UNSET:
            field_dict["sendOnFailure"] = send_on_failure

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        send_on_success = d.pop("sendOnSuccess", UNSET)

        send_on_failure = d.pop("sendOnFailure", UNSET)

        test_notification_settings = cls(
            send_on_success=send_on_success,
            send_on_failure=send_on_failure,
        )

        test_notification_settings.additional_properties = d
        return test_notification_settings

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
