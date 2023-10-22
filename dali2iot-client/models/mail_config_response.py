from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.smtp_security import SmtpSecurity
from ..types import UNSET, Unset

T = TypeVar("T", bound="MailConfigResponse")


@_attrs_define
class MailConfigResponse:
    """
    Attributes:
        server (Union[Unset, str]):
        port (Union[Unset, int]):
        security (Union[Unset, SmtpSecurity]): An enumeration.
        password (Union[Unset, bool]): Whether a password is currently stored (``True``) or not (``False``).
        username (Union[Unset, str]):
        sender_name (Union[Unset, str]):
        sender_email (Union[Unset, str]):
    """

    server: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    security: Union[Unset, SmtpSecurity] = UNSET
    password: Union[Unset, bool] = False
    username: Union[Unset, str] = UNSET
    sender_name: Union[Unset, str] = UNSET
    sender_email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server = self.server
        port = self.port
        security: Union[Unset, str] = UNSET
        if not isinstance(self.security, Unset):
            security = self.security.value

        password = self.password
        username = self.username
        sender_name = self.sender_name
        sender_email = self.sender_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server is not UNSET:
            field_dict["server"] = server
        if port is not UNSET:
            field_dict["port"] = port
        if security is not UNSET:
            field_dict["security"] = security
        if password is not UNSET:
            field_dict["password"] = password
        if username is not UNSET:
            field_dict["username"] = username
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name
        if sender_email is not UNSET:
            field_dict["senderEmail"] = sender_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server = d.pop("server", UNSET)

        port = d.pop("port", UNSET)

        _security = d.pop("security", UNSET)
        security: Union[Unset, SmtpSecurity]
        if isinstance(_security, Unset):
            security = UNSET
        else:
            security = SmtpSecurity(_security)

        password = d.pop("password", UNSET)

        username = d.pop("username", UNSET)

        sender_name = d.pop("senderName", UNSET)

        sender_email = d.pop("senderEmail", UNSET)

        mail_config_response = cls(
            server=server,
            port=port,
            security=security,
            password=password,
            username=username,
            sender_name=sender_name,
            sender_email=sender_email,
        )

        mail_config_response.additional_properties = d
        return mail_config_response

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
