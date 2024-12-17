from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostMarketOrdersUpdateStatusBody")


@_attrs_define
class PostMarketOrdersUpdateStatusBody:
    """
    Attributes:
        order (Union[Unset, str]): شناسه سفارش

            الزامی
        status (Union[Unset, str]): وضعیت سفارش

            الزامی
    """

    order: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order = self.order

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        order = self.order if isinstance(self.order, Unset) else (None, str(self.order).encode(), "text/plain")

        status = self.status if isinstance(self.status, Unset) else (None, str(self.status).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        order = d.pop("order", UNSET)

        status = d.pop("status", UNSET)

        post_market_orders_update_status_body = cls(
            order=order,
            status=status,
        )

        post_market_orders_update_status_body.additional_properties = d
        return post_market_orders_update_status_body

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
