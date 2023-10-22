from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mail_config_response import MailConfigResponse
    from ..models.notification_settings import NotificationSettings


T = TypeVar("T", bound="MailSettingsResponse")


@_attrs_define
class MailSettingsResponse:
    """
    Attributes:
        mail_config (MailConfigResponse):
        notifications (NotificationSettings): Configure which tests should notify whom, by mail.
    """

    mail_config: "MailConfigResponse"
    notifications: "NotificationSettings"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mail_config = self.mail_config.to_dict()

        notifications = self.notifications.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mailConfig": mail_config,
                "notifications": notifications,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.mail_config_response import MailConfigResponse
        from ..models.notification_settings import NotificationSettings

        d = src_dict.copy()
        mail_config = MailConfigResponse.from_dict(d.pop("mailConfig"))

        notifications = NotificationSettings.from_dict(d.pop("notifications"))

        mail_settings_response = cls(
            mail_config=mail_config,
            notifications=notifications,
        )

        mail_settings_response.additional_properties = d
        return mail_settings_response

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
