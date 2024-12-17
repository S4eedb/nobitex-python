from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostUsersCardsAddBody")


@_attrs_define
class PostUsersCardsAddBody:
    """
    Attributes:
        number (Union[Unset, str]): شماره کارت

            الزامی
        bank (Union[Unset, str]): نام بانک

            اختیاری
    """

    number: Union[Unset, str] = UNSET
    bank: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        bank = self.bank

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if bank is not UNSET:
            field_dict["bank"] = bank

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        number = self.number if isinstance(self.number, Unset) else (None, str(self.number).encode(), "text/plain")

        bank = self.bank if isinstance(self.bank, Unset) else (None, str(self.bank).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if bank is not UNSET:
            field_dict["bank"] = bank

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        number = d.pop("number", UNSET)

        bank = d.pop("bank", UNSET)

        post_users_cards_add_body = cls(
            number=number,
            bank=bank,
        )

        post_users_cards_add_body.additional_properties = d
        return post_users_cards_add_body

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
