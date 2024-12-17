from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostUsersReferralLinksAddBody")


@_attrs_define
class PostUsersReferralLinksAddBody:
    """
    Attributes:
        friend_share (Union[Unset, int]): سهم کارمزد اهدایی به دوست دعوت شده با این کد

            اختیاری Example: 0.
    """

    friend_share: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        friend_share = self.friend_share

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if friend_share is not UNSET:
            field_dict["friendShare"] = friend_share

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        friend_share = (
            self.friend_share
            if isinstance(self.friend_share, Unset)
            else (None, str(self.friend_share).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if friend_share is not UNSET:
            field_dict["friendShare"] = friend_share

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        friend_share = d.pop("friendShare", UNSET)

        post_users_referral_links_add_body = cls(
            friend_share=friend_share,
        )

        post_users_referral_links_add_body.additional_properties = d
        return post_users_referral_links_add_body

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
