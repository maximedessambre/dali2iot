from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mail_config import MailConfig
    from ..models.notification_settings import NotificationSettings


T = TypeVar("T", bound="MailSettings")


@_attrs_define
class MailSettings:
    """A complete set of mail settings, made of sender configuration and notifications.

    Attributes:
        mail_config (Union[Unset, MailConfig]): Mail sending configuration.

            All values are optional. Only provided settings are updated. Explicitly setting a value to
            ``null`` is required to clear it.
        notifications (Union[Unset, NotificationSettings]): Configure which tests should notify whom, by mail.
    """

    mail_config: Union[Unset, "MailConfig"] = UNSET
    notifications: Union[Unset, "NotificationSettings"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mail_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mail_config, Unset):
            mail_config = self.mail_config.to_dict()

        notifications: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = self.notifications.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mail_config is not UNSET:
            field_dict["mailConfig"] = mail_config
        if notifications is not UNSET:
            field_dict["notifications"] = notifications

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.mail_config import MailConfig
        from ..models.notification_settings import NotificationSettings

        d = src_dict.copy()
        _mail_config = d.pop("mailConfig", UNSET)
        mail_config: Union[Unset, MailConfig]
        if isinstance(_mail_config, Unset):
            mail_config = UNSET
        else:
            mail_config = MailConfig.from_dict(_mail_config)

        _notifications = d.pop("notifications", UNSET)
        notifications: Union[Unset, NotificationSettings]
        if isinstance(_notifications, Unset):
            notifications = UNSET
        else:
            notifications = NotificationSettings.from_dict(_notifications)

        mail_settings = cls(
            mail_config=mail_config,
            notifications=notifications,
        )

        mail_settings.additional_properties = d
        return mail_settings

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
