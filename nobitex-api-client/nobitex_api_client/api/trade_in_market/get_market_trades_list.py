from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_market_trades_list_response_200 import GetMarketTradesListResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    src_currency: Union[Unset, str] = UNSET,
    dst_currency: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["srcCurrency"] = src_currency

    params["dstCurrency"] = dst_currency

    params["page"] = page

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/market/trades/list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetMarketTradesListResponse200]:
    if response.status_code == 200:
        response_200 = GetMarketTradesListResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetMarketTradesListResponse200]:
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
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[GetMarketTradesListResponse200]:
    """Trades list

     ## لیست معاملات

    برای دریافت فهرست معاملات خود، از این درخواست استفاده نمایید.

    رمزارزهای مبدا پشتیبانی شده:
    {{crypto_currencies}}

    ارزهای مقصد پشتیبانی شده:
    rls, usdt

    ارز مبدا و مقصد باید هر دو با هم پر یا خالی باشند.

    در پاسخ حداکثر معاملات ۳ روز گذشته بازگردانده می‌شود.

    محدودیت فراخوانی: ۲۰ درخواست در هر دقیقه

    Args:
        src_currency (Union[Unset, str]):
        dst_currency (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMarketTradesListResponse200]
    """

    kwargs = _get_kwargs(
        src_currency=src_currency,
        dst_currency=dst_currency,
        page=page,
        page_size=page_size,
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
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[GetMarketTradesListResponse200]:
    """Trades list

     ## لیست معاملات

    برای دریافت فهرست معاملات خود، از این درخواست استفاده نمایید.

    رمزارزهای مبدا پشتیبانی شده:
    {{crypto_currencies}}

    ارزهای مقصد پشتیبانی شده:
    rls, usdt

    ارز مبدا و مقصد باید هر دو با هم پر یا خالی باشند.

    در پاسخ حداکثر معاملات ۳ روز گذشته بازگردانده می‌شود.

    محدودیت فراخوانی: ۲۰ درخواست در هر دقیقه

    Args:
        src_currency (Union[Unset, str]):
        dst_currency (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMarketTradesListResponse200
    """

    return sync_detailed(
        client=client,
        src_currency=src_currency,
        dst_currency=dst_currency,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    src_currency: Union[Unset, str] = UNSET,
    dst_currency: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[GetMarketTradesListResponse200]:
    """Trades list

     ## لیست معاملات

    برای دریافت فهرست معاملات خود، از این درخواست استفاده نمایید.

    رمزارزهای مبدا پشتیبانی شده:
    {{crypto_currencies}}

    ارزهای مقصد پشتیبانی شده:
    rls, usdt

    ارز مبدا و مقصد باید هر دو با هم پر یا خالی باشند.

    در پاسخ حداکثر معاملات ۳ روز گذشته بازگردانده می‌شود.

    محدودیت فراخوانی: ۲۰ درخواست در هر دقیقه

    Args:
        src_currency (Union[Unset, str]):
        dst_currency (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMarketTradesListResponse200]
    """

    kwargs = _get_kwargs(
        src_currency=src_currency,
        dst_currency=dst_currency,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    src_currency: Union[Unset, str] = UNSET,
    dst_currency: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[GetMarketTradesListResponse200]:
    """Trades list

     ## لیست معاملات

    برای دریافت فهرست معاملات خود، از این درخواست استفاده نمایید.

    رمزارزهای مبدا پشتیبانی شده:
    {{crypto_currencies}}

    ارزهای مقصد پشتیبانی شده:
    rls, usdt

    ارز مبدا و مقصد باید هر دو با هم پر یا خالی باشند.

    در پاسخ حداکثر معاملات ۳ روز گذشته بازگردانده می‌شود.

    محدودیت فراخوانی: ۲۰ درخواست در هر دقیقه

    Args:
        src_currency (Union[Unset, str]):
        dst_currency (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMarketTradesListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            src_currency=src_currency,
            dst_currency=dst_currency,
            page=page,
            page_size=page_size,
        )
    ).parsed
