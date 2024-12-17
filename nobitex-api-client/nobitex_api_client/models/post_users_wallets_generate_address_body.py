from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostUsersWalletsGenerateAddressBody")


@_attrs_define
class PostUsersWalletsGenerateAddressBody:
    """
    Attributes:
        currency (Union[Unset, str]): رمزارز کیف پول

            الزامی
        network (Union[Unset, str]): شبکه کیف پول

            اختیاری
        address_type (Union[Unset, str]): نوع پروتکل مورد استفاده

            اختیاری Example: default.
    """

    currency: Union[Unset, str] = UNSET
    network: Union[Unset, str] = UNSET
    address_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        network = self.network

        address_type = self.address_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if network is not UNSET:
            field_dict["network"] = network
        if address_type is not UNSET:
            field_dict["addressType"] = address_type

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        currency = (
            self.currency if isinstance(self.currency, Unset) else (None, str(self.currency).encode(), "text/plain")
        )

        network = self.network if isinstance(self.network, Unset) else (None, str(self.network).encode(), "text/plain")

        address_type = (
            self.address_type
            if isinstance(self.address_type, Unset)
            else (None, str(self.address_type).encode(), "text/plain")
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if network is not UNSET:
            field_dict["network"] = network
        if address_type is not UNSET:
            field_dict["addressType"] = address_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        currency = d.pop("currency", UNSET)

        network = d.pop("network", UNSET)

        address_type = d.pop("addressType", UNSET)

        post_users_wallets_generate_address_body = cls(
            currency=currency,
            network=network,
            address_type=address_type,
        )

        post_users_wallets_generate_address_body.additional_properties = d
        return post_users_wallets_generate_address_body

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
