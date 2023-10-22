from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_notification_settings import TestNotificationSettings


T = TypeVar("T", bound="NotificationSettings")


@_attrs_define
class NotificationSettings:
    """Configure which tests should notify whom, by mail.

    Attributes:
        function_test (Union[Unset, TestNotificationSettings]): Configure whether to notify test success or failure, by
            mail.
        duration_test (Union[Unset, TestNotificationSettings]): Configure whether to notify test success or failure, by
            mail.
        communication_test (Union[Unset, TestNotificationSettings]): Configure whether to notify test success or
            failure, by mail.
        mail_receivers (Union[Unset, List[str]]):
    """

    function_test: Union[Unset, "TestNotificationSettings"] = UNSET
    duration_test: Union[Unset, "TestNotificationSettings"] = UNSET
    communication_test: Union[Unset, "TestNotificationSettings"] = UNSET
    mail_receivers: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        function_test: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.function_test, Unset):
            function_test = self.function_test.to_dict()

        duration_test: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.duration_test, Unset):
            duration_test = self.duration_test.to_dict()

        communication_test: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.communication_test, Unset):
            communication_test = self.communication_test.to_dict()

        mail_receivers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.mail_receivers, Unset):
            mail_receivers = self.mail_receivers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if function_test is not UNSET:
            field_dict["functionTest"] = function_test
        if duration_test is not UNSET:
            field_dict["durationTest"] = duration_test
        if communication_test is not UNSET:
            field_dict["communicationTest"] = communication_test
        if mail_receivers is not UNSET:
            field_dict["mailReceivers"] = mail_receivers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.test_notification_settings import TestNotificationSettings

        d = src_dict.copy()
        _function_test = d.pop("functionTest", UNSET)
        function_test: Union[Unset, TestNotificationSettings]
        if isinstance(_function_test, Unset):
            function_test = UNSET
        else:
            function_test = TestNotificationSettings.from_dict(_function_test)

        _duration_test = d.pop("durationTest", UNSET)
        duration_test: Union[Unset, TestNotificationSettings]
        if isinstance(_duration_test, Unset):
            duration_test = UNSET
        else:
            duration_test = TestNotificationSettings.from_dict(_duration_test)

        _communication_test = d.pop("communicationTest", UNSET)
        communication_test: Union[Unset, TestNotificationSettings]
        if isinstance(_communication_test, Unset):
            communication_test = UNSET
        else:
            communication_test = TestNotificationSettings.from_dict(_communication_test)

        mail_receivers = cast(List[str], d.pop("mailReceivers", UNSET))

        notification_settings = cls(
            function_test=function_test,
            duration_test=duration_test,
            communication_test=communication_test,
            mail_receivers=mail_receivers,
        )

        notification_settings.additional_properties = d
        return notification_settings

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
