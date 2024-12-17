from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostUsersAccountsAddBody")


@_attrs_define
class PostUsersAccountsAddBody:
    """
    Attributes:
        shaba (Union[Unset, str]): شماره شبا

            الزامی
        number (Union[Unset, str]): شماره حساب

            اختیاری
    """

    shaba: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shaba = self.shaba

        number = self.number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shaba is not UNSET:
            field_dict["shaba"] = shaba
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        shaba = self.shaba if isinstance(self.shaba, Unset) else (None, str(self.shaba).encode(), "text/plain")

        number = self.number if isinstance(self.number, Unset) else (None, str(self.number).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if shaba is not UNSET:
            field_dict["shaba"] = shaba
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        shaba = d.pop("shaba", UNSET)

        number = d.pop("number", UNSET)

        post_users_accounts_add_body = cls(
            shaba=shaba,
            number=number,
        )

        post_users_accounts_add_body.additional_properties = d
        return post_users_accounts_add_body

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
