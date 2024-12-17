from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostUsersReferralSetReferrerBody")


@_attrs_define
class PostUsersReferralSetReferrerBody:
    """
    Attributes:
        referrer_code (Union[Unset, str]): کد دعوت کاربر دعوت کننده

            الزامی
    """

    referrer_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        referrer_code = self.referrer_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if referrer_code is not UNSET:
            field_dict["referrerCode"] = referrer_code

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        referrer_code = (
            self.referrer_code
            if isinstance(self.referrer_code, Unset)
            else (None, str(self.referrer_code).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if referrer_code is not UNSET:
            field_dict["referrerCode"] = referrer_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        referrer_code = d.pop("referrerCode", UNSET)

        post_users_referral_set_referrer_body = cls(
            referrer_code=referrer_code,
        )

        post_users_referral_set_referrer_body.additional_properties = d
        return post_users_referral_set_referrer_body

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
