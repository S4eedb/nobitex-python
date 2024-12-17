from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostAuthLoginBody")


@_attrs_define
class PostAuthLoginBody:
    """
    Attributes:
        username (Union[Unset, str]): ایمیل کاربر

            الزامی
        password (Union[Unset, str]): رمز ورود

            الزامی
        remember (Union[Unset, str]): توکن طولانی مدت

            اختیاری Example: yes.
        captcha (Union[Unset, str]): الزامی Example: api.
        useragent (Union[Unset, str]): نام بات با پیشوند TraderBot/

            اختیاری
    """

    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    remember: Union[Unset, str] = UNSET
    captcha: Union[Unset, str] = UNSET
    useragent: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        remember = self.remember

        captcha = self.captcha

        useragent = self.useragent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if remember is not UNSET:
            field_dict["remember"] = remember
        if captcha is not UNSET:
            field_dict["captcha"] = captcha
        if useragent is not UNSET:
            field_dict["useragent"] = useragent

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        username = (
            self.username if isinstance(self.username, Unset) else (None, str(self.username).encode(), "text/plain")
        )

        password = (
            self.password if isinstance(self.password, Unset) else (None, str(self.password).encode(), "text/plain")
        )

        remember = (
            self.remember if isinstance(self.remember, Unset) else (None, str(self.remember).encode(), "text/plain")
        )

        captcha = self.captcha if isinstance(self.captcha, Unset) else (None, str(self.captcha).encode(), "text/plain")

        useragent = (
            self.useragent if isinstance(self.useragent, Unset) else (None, str(self.useragent).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if remember is not UNSET:
            field_dict["remember"] = remember
        if captcha is not UNSET:
            field_dict["captcha"] = captcha
        if useragent is not UNSET:
            field_dict["useragent"] = useragent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        remember = d.pop("remember", UNSET)

        captcha = d.pop("captcha", UNSET)

        useragent = d.pop("useragent", UNSET)

        post_auth_login_body = cls(
            username=username,
            password=password,
            remember=remember,
            captcha=captcha,
            useragent=useragent,
        )

        post_auth_login_body.additional_properties = d
        return post_auth_login_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
