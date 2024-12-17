from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostUsersWalletsWithdrawConfirmBody")


@_attrs_define
class PostUsersWalletsWithdrawConfirmBody:
    """
    Attributes:
        withdraw (Union[Unset, str]): شناسه درخواست برداشت
        otp (Union[Unset, str]): رمز یکبارمصرف ارسال شده
    """

    withdraw: Union[Unset, str] = UNSET
    otp: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        withdraw = self.withdraw

        otp = self.otp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if withdraw is not UNSET:
            field_dict["withdraw"] = withdraw
        if otp is not UNSET:
            field_dict["otp"] = otp

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        withdraw = (
            self.withdraw if isinstance(self.withdraw, Unset) else (None, str(self.withdraw).encode(), "text/plain")
        )

        otp = self.otp if isinstance(self.otp, Unset) else (None, str(self.otp).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if withdraw is not UNSET:
            field_dict["withdraw"] = withdraw
        if otp is not UNSET:
            field_dict["otp"] = otp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        withdraw = d.pop("withdraw", UNSET)

        otp = d.pop("otp", UNSET)

        post_users_wallets_withdraw_confirm_body = cls(
            withdraw=withdraw,
            otp=otp,
        )

        post_users_wallets_withdraw_confirm_body.additional_properties = d
        return post_users_wallets_withdraw_confirm_body

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