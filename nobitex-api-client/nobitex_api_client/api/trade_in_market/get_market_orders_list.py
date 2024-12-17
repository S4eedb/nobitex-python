from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_market_orders_list_response_200 import GetMarketOrdersListResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    src_currency: Union[Unset, str] = UNSET,
    dst_currency: Union[Unset, str] = UNSET,
    details: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["srcCurrency"] = src_currency

    params["dstCurrency"] = dst_currency

    params["details"] = details

    params["status"] = status

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/market/orders/list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetMarketOrdersListResponse200]:
    if response.status_code == 200:
        response_200 = GetMarketOrdersListResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetMarketOrdersListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    src_currency: Union[Unset, str] = UNSET,
    dst_currency: Union[Unset, str] = UNSET,
    details: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[GetMarketOrdersListResponse200]:
    """Orders list

     ## لیست سفارشات

    برای دریافت فهرست سفارش‌های خود، از این درخواست استفاده نمایید.

    رمزارزهای مبدا پشتیبانی شده:
    {{crypto_currencies}}

    ارزهای مقصد پشتیبانی شده:
    rls, usdt

    مقادیر وضعیت سفارش:

    *   `all`: تمام سفارش‌های کاربر
    *   `open`: سفارش‌های باز، شامل سفارش‌های فعال و غیرفعال
    *   `done`: سفارش‌هایی که بخشی یا تمام آن پر شده باشد
    *   `close`: سفارش‌هایی که وضعیت آن‌ها «انجام شده» یا «لغو شده» باشد


    مقادیر نوع سفارش:

    *   `buy`: خرید
    *   `sell`: فروش


    میزان جزئیات شی سفارش در پاسخ:

    *   `1`:
        *   type
        *   execution
        *   srcCurrency
        *   dstCurrency
        *   price
        *   amount
        *   matchedAmount: مقدار پر شده از سفارش
    *   `2`: علاوه بر مقادیر قبلی، مقادیر زیر بازگردانده می‌شوند
        *   id
        *   status
        *   fee: کارمزد سفارش تاکنون
        *   created_at
        *   averagePrice: میانگین قیمت اجرا شده از سفارش

    در پاسخ حداکثر اطلاعات ۱۰۰۰ سفارش بازگردانده می‌شود.

    محدودیت فراخوانی: ۳۰ درخواست در هر دقیقه

    Args:
        src_currency (Union[Unset, str]):
        dst_currency (Union[Unset, str]):
        details (Union[Unset, int]):
        status (Union[Unset, str]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMarketOrdersListResponse200]
    """

    kwargs = _get_kwargs(
        src_currency=src_currency,
        dst_currency=dst_currency,
        details=details,
        status=status,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    src_currency: Union[Unset, str] = UNSET,
    dst_currency: Union[Unset, str] = UNSET,
    details: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Optional[GetMarketOrdersListResponse200]:
    """Orders list

     ## لیست سفارشات

    برای دریافت فهرست سفارش‌های خود، از این درخواست استفاده نمایید.

    رمزارزهای مبدا پشتیبانی شده:
    {{crypto_currencies}}

    ارزهای مقصد پشتیبانی شده:
    rls, usdt

    مقادیر وضعیت سفارش:

    *   `all`: تمام سفارش‌های کاربر
    *   `open`: سفارش‌های باز، شامل سفارش‌های فعال و غیرفعال
    *   `done`: سفارش‌هایی که بخشی یا تمام آن پر شده باشد
    *   `close`: سفارش‌هایی که وضعیت آن‌ها «انجام شده» یا «لغو شده» باشد


    مقادیر نوع سفارش:

    *   `buy`: خرید
    *   `sell`: فروش


    میزان جزئیات شی سفارش در پاسخ:

    *   `1`:
        *   type
        *   execution
        *   srcCurrency
        *   dstCurrency
        *   price
        *   amount
        *   matchedAmount: مقدار پر شده از سفارش
    *   `2`: علاوه بر مقادیر قبلی، مقادیر زیر بازگردانده می‌شوند
        *   id
        *   status
        *   fee: کارمزد سفارش تاکنون
        *   created_at
        *   averagePrice: میانگین قیمت اجرا شده از سفارش

    در پاسخ حداکثر اطلاعات ۱۰۰۰ سفارش بازگردانده می‌شود.

    محدودیت فراخوانی: ۳۰ درخواست در هر دقیقه

    Args:
        src_currency (Union[Unset, str]):
        dst_currency (Union[Unset, str]):
        details (Union[Unset, int]):
        status (Union[Unset, str]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMarketOrdersListResponse200
    """

    return sync_detailed(
        client=client,
        src_currency=src_currency,
        dst_currency=dst_currency,
        details=details,
        status=status,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    src_currency: Union[Unset, str] = UNSET,
    dst_currency: Union[Unset, str] = UNSET,
    details: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[GetMarketOrdersListResponse200]:
    """Orders list

     ## لیست سفارشات

    برای دریافت فهرست سفارش‌های خود، از این درخواست استفاده نمایید.

    رمزارزهای مبدا پشتیبانی شده:
    {{crypto_currencies}}

    ارزهای مقصد پشتیبانی شده:
    rls, usdt

    مقادیر وضعیت سفارش:

    *   `all`: تمام سفارش‌های کاربر
    *   `open`: سفارش‌های باز، شامل سفارش‌های فعال و غیرفعال
    *   `done`: سفارش‌هایی که بخشی یا تمام آن پر شده باشد
    *   `close`: سفارش‌هایی که وضعیت آن‌ها «انجام شده» یا «لغو شده» باشد


    مقادیر نوع سفارش:

    *   `buy`: خرید
    *   `sell`: فروش


    میزان جزئیات شی سفارش در پاسخ:

    *   `1`:
        *   type
        *   execution
        *   srcCurrency
        *   dstCurrency
        *   price
        *   amount
        *   matchedAmount: مقدار پر شده از سفارش
    *   `2`: علاوه بر مقادیر قبلی، مقادیر زیر بازگردانده می‌شوند
        *   id
        *   status
        *   fee: کارمزد سفارش تاکنون
        *   created_at
        *   averagePrice: میانگین قیمت اجرا شده از سفارش

    در پاسخ حداکثر اطلاعات ۱۰۰۰ سفارش بازگردانده می‌شود.

    محدودیت فراخوانی: ۳۰ درخواست در هر دقیقه

    Args:
        src_currency (Union[Unset, str]):
        dst_currency (Union[Unset, str]):
        details (Union[Unset, int]):
        status (Union[Unset, str]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMarketOrdersListResponse200]
    """

    kwargs = _get_kwargs(
        src_currency=src_currency,
        dst_currency=dst_currency,
        details=details,
        status=status,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    src_currency: Union[Unset, str] = UNSET,
    dst_currency: Union[Unset, str] = UNSET,
    details: Union[Unset, int] = UNSET,
    status: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Optional[GetMarketOrdersListResponse200]:
    """Orders list

     ## لیست سفارشات

    برای دریافت فهرست سفارش‌های خود، از این درخواست استفاده نمایید.

    رمزارزهای مبدا پشتیبانی شده:
    {{crypto_currencies}}

    ارزهای مقصد پشتیبانی شده:
    rls, usdt

    مقادیر وضعیت سفارش:

    *   `all`: تمام سفارش‌های کاربر
    *   `open`: سفارش‌های باز، شامل سفارش‌های فعال و غیرفعال
    *   `done`: سفارش‌هایی که بخشی یا تمام آن پر شده باشد
    *   `close`: سفارش‌هایی که وضعیت آن‌ها «انجام شده» یا «لغو شده» باشد


    مقادیر نوع سفارش:

    *   `buy`: خرید
    *   `sell`: فروش


    میزان جزئیات شی سفارش در پاسخ:

    *   `1`:
        *   type
        *   execution
        *   srcCurrency
        *   dstCurrency
        *   price
        *   amount
        *   matchedAmount: مقدار پر شده از سفارش
    *   `2`: علاوه بر مقادیر قبلی، مقادیر زیر بازگردانده می‌شوند
        *   id
        *   status
        *   fee: کارمزد سفارش تاکنون
        *   created_at
        *   averagePrice: میانگین قیمت اجرا شده از سفارش

    در پاسخ حداکثر اطلاعات ۱۰۰۰ سفارش بازگردانده می‌شود.

    محدودیت فراخوانی: ۳۰ درخواست در هر دقیقه

    Args:
        src_currency (Union[Unset, str]):
        dst_currency (Union[Unset, str]):
        details (Union[Unset, int]):
        status (Union[Unset, str]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMarketOrdersListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            src_currency=src_currency,
            dst_currency=dst_currency,
            details=details,
            status=status,
            type_=type_,
        )
    ).parsed
