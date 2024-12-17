from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostMarketOrdersAddBody")


@_attrs_define
class PostMarketOrdersAddBody:
    """
    Attributes:
        type_ (Union[Unset, str]): نوع سفارش (خرید یا فروش)

            الزامی
        mode (Union[Unset, str]):  حالت سفارش

            اختیاری Example: default.
        execution (Union[Unset, str]): نحوه‌ی اجرای سفارش

            اختیاری Example: limit.
        src_currency (Union[Unset, str]): رمزارز مبدا

            الزامی
        dst_currency (Union[Unset, str]): ارز مقصد

            الزامی
        amount (Union[Unset, str]): مقدار رمزارز (حجم)

            الزامی
        price (Union[Unset, str]): قیمت واحد

            (الزامی در سفارش‌های قیمت معین)
        stop_price (Union[Unset, str]): قیمت توقف

            (الزامی در سفارش‌های حد ضرر و  oco)
        stop_limit_price (Union[Unset, str]): قیمت حد ضرر

            (الزامی در سفارش‌های oco)
        pro (Union[Unset, str]): حالت حرفه‌ای

            اختیاری
    """

    type_: Union[Unset, str] = UNSET
    mode: Union[Unset, str] = UNSET
    execution: Union[Unset, str] = UNSET
    src_currency: Union[Unset, str] = UNSET
    dst_currency: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    price: Union[Unset, str] = UNSET
    stop_price: Union[Unset, str] = UNSET
    stop_limit_price: Union[Unset, str] = UNSET
    pro: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        mode = self.mode

        execution = self.execution

        src_currency = self.src_currency

        dst_currency = self.dst_currency

        amount = self.amount

        price = self.price

        stop_price = self.stop_price

        stop_limit_price = self.stop_limit_price

        pro = self.pro

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mode is not UNSET:
            field_dict["mode"] = mode
        if execution is not UNSET:
            field_dict["execution"] = execution
        if src_currency is not UNSET:
            field_dict["srcCurrency"] = src_currency
        if dst_currency is not UNSET:
            field_dict["dstCurrency"] = dst_currency
        if amount is not UNSET:
            field_dict["amount"] = amount
        if price is not UNSET:
            field_dict["price"] = price
        if stop_price is not UNSET:
            field_dict["stopPrice"] = stop_price
        if stop_limit_price is not UNSET:
            field_dict["stopLimitPrice"] = stop_limit_price
        if pro is not UNSET:
            field_dict["pro"] = pro

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        type_ = self.type_ if isinstance(self.type_, Unset) else (None, str(self.type_).encode(), "text/plain")

        mode = self.mode if isinstance(self.mode, Unset) else (None, str(self.mode).encode(), "text/plain")

        execution = (
            self.execution if isinstance(self.execution, Unset) else (None, str(self.execution).encode(), "text/plain")
        )

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

        amount = self.amount if isinstance(self.amount, Unset) else (None, str(self.amount).encode(), "text/plain")

        price = self.price if isinstance(self.price, Unset) else (None, str(self.price).encode(), "text/plain")

        stop_price = (
            self.stop_price
            if isinstance(self.stop_price, Unset)
            else (None, str(self.stop_price).encode(), "text/plain")
        )

        stop_limit_price = (
            self.stop_limit_price
            if isinstance(self.stop_limit_price, Unset)
            else (None, str(self.stop_limit_price).encode(), "text/plain")
        )

        pro = self.pro if isinstance(self.pro, Unset) else (None, str(self.pro).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mode is not UNSET:
            field_dict["mode"] = mode
        if execution is not UNSET:
            field_dict["execution"] = execution
        if src_currency is not UNSET:
            field_dict["srcCurrency"] = src_currency
        if dst_currency is not UNSET:
            field_dict["dstCurrency"] = dst_currency
        if amount is not UNSET:
            field_dict["amount"] = amount
        if price is not UNSET:
            field_dict["price"] = price
        if stop_price is not UNSET:
            field_dict["stopPrice"] = stop_price
        if stop_limit_price is not UNSET:
            field_dict["stopLimitPrice"] = stop_limit_price
        if pro is not UNSET:
            field_dict["pro"] = pro

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = d.pop("type", UNSET)

        mode = d.pop("mode", UNSET)

        execution = d.pop("execution", UNSET)

        src_currency = d.pop("srcCurrency", UNSET)

        dst_currency = d.pop("dstCurrency", UNSET)

        amount = d.pop("amount", UNSET)

        price = d.pop("price", UNSET)

        stop_price = d.pop("stopPrice", UNSET)

        stop_limit_price = d.pop("stopLimitPrice", UNSET)

        pro = d.pop("pro", UNSET)

        post_market_orders_add_body = cls(
            type_=type_,
            mode=mode,
            execution=execution,
            src_currency=src_currency,
            dst_currency=dst_currency,
            amount=amount,
            price=price,
            stop_price=stop_price,
            stop_limit_price=stop_limit_price,
            pro=pro,
        )

        post_market_orders_add_body.additional_properties = d
        return post_market_orders_add_body

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
