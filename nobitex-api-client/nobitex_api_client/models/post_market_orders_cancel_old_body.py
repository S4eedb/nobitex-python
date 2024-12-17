from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostMarketOrdersCancelOldBody")


@_attrs_define
class PostMarketOrdersCancelOldBody:
    """
    Attributes:
        src_currency (Union[Unset, str]): رمزارز مبدا بازار

            الزامی
        dst_currency (Union[Unset, str]): ارز مقصد بازار

            الزامی
        execution (Union[Unset, str]): نحوه اجرای سفارش‌ها

            اختیاری
        hours (Union[Unset, str]): بازه زمانی سفارش‌ها به ساعت

            اختیاری
    """

    src_currency: Union[Unset, str] = UNSET
    dst_currency: Union[Unset, str] = UNSET
    execution: Union[Unset, str] = UNSET
    hours: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        src_currency = self.src_currency

        dst_currency = self.dst_currency

        execution = self.execution

        hours = self.hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if src_currency is not UNSET:
            field_dict["srcCurrency"] = src_currency
        if dst_currency is not UNSET:
            field_dict["dstCurrency"] = dst_currency
        if execution is not UNSET:
            field_dict["execution"] = execution
        if hours is not UNSET:
            field_dict["hours"] = hours

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        src_currency = (
            self.src_currency
            if isinstance(self.src_currency, Unset)
            else (None, str(self.src_currency).encode(), "text/plain")
        )

        dst_currency = (
            self.dst_currency
            if isinstance(self.dst_currency, Unset)
            else (None, str(self.dst_currency).encode(), "text/plain")
        )

        execution = (
            self.execution if isinstance(self.execution, Unset) else (None, str(self.execution).encode(), "text/plain")
        )

        hours = self.hours if isinstance(self.hours, Unset) else (None, str(self.hours).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if src_currency is not UNSET:
            field_dict["srcCurrency"] = src_currency
        if dst_currency is not UNSET:
            field_dict["dstCurrency"] = dst_currency
        if execution is not UNSET:
            field_dict["execution"] = execution
        if hours is not UNSET:
            field_dict["hours"] = hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        src_currency = d.pop("srcCurrency", UNSET)

        dst_currency = d.pop("dstCurrency", UNSET)

        execution = d.pop("execution", UNSET)

        hours = d.pop("hours", UNSET)

        post_market_orders_cancel_old_body = cls(
            src_currency=src_currency,
            dst_currency=dst_currency,
            execution=execution,
            hours=hours,
        )

        post_market_orders_cancel_old_body.additional_properties = d
        return post_market_orders_cancel_old_body

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
