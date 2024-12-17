from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_market_udf_history_response_200 import GetMarketUdfHistoryResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    symbol: Union[Unset, str] = UNSET,
    resolution: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["symbol"] = symbol

    params["resolution"] = resolution

    params["from"] = from_

    params["to"] = to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/market/udf/history",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetMarketUdfHistoryResponse200]:
    if response.status_code == 200:
        response_200 = GetMarketUdfHistoryResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetMarketUdfHistoryResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    symbol: Union[Unset, str] = UNSET,
    resolution: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
) -> Response[GetMarketUdfHistoryResponse200]:
    """OHLC

     ## آمار OHLC بازار نوبیتکس

    نوبیتکس از این نوع درخواست استفاده نمایید OHLCبرای دریافت آمار
    بازه زمانی کندل‌های خروجی می‌تواند یکی از مقادیر زیر باشد:

    *   یک ساعت :60
    *   یک روز :D


    ###### مقادیر پاسخ

    *   t (time): زمان شروع بازه
    *   o (open): قیمت شروع بازه
    *   c (close): قیمت پایان بازه
    *   l (low): پایین‌ترین قیمت بازه
    *   h(high): بالاترین قیمت بازه
    *   v (volume): حجم بازه


    که برای هر کندل در بازه زمانی گزارش یک عدد در لیست قرار می‌گیرد.

    Args:
        symbol (Union[Unset, str]):
        resolution (Union[Unset, str]):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMarketUdfHistoryResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        resolution=resolution,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    symbol: Union[Unset, str] = UNSET,
    resolution: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
) -> Optional[GetMarketUdfHistoryResponse200]:
    """OHLC

     ## آمار OHLC بازار نوبیتکس

    نوبیتکس از این نوع درخواست استفاده نمایید OHLCبرای دریافت آمار
    بازه زمانی کندل‌های خروجی می‌تواند یکی از مقادیر زیر باشد:

    *   یک ساعت :60
    *   یک روز :D


    ###### مقادیر پاسخ

    *   t (time): زمان شروع بازه
    *   o (open): قیمت شروع بازه
    *   c (close): قیمت پایان بازه
    *   l (low): پایین‌ترین قیمت بازه
    *   h(high): بالاترین قیمت بازه
    *   v (volume): حجم بازه


    که برای هر کندل در بازه زمانی گزارش یک عدد در لیست قرار می‌گیرد.

    Args:
        symbol (Union[Unset, str]):
        resolution (Union[Unset, str]):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMarketUdfHistoryResponse200
    """

    return sync_detailed(
        client=client,
        symbol=symbol,
        resolution=resolution,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    symbol: Union[Unset, str] = UNSET,
    resolution: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
) -> Response[GetMarketUdfHistoryResponse200]:
    """OHLC

     ## آمار OHLC بازار نوبیتکس

    نوبیتکس از این نوع درخواست استفاده نمایید OHLCبرای دریافت آمار
    بازه زمانی کندل‌های خروجی می‌تواند یکی از مقادیر زیر باشد:

    *   یک ساعت :60
    *   یک روز :D


    ###### مقادیر پاسخ

    *   t (time): زمان شروع بازه
    *   o (open): قیمت شروع بازه
    *   c (close): قیمت پایان بازه
    *   l (low): پایین‌ترین قیمت بازه
    *   h(high): بالاترین قیمت بازه
    *   v (volume): حجم بازه


    که برای هر کندل در بازه زمانی گزارش یک عدد در لیست قرار می‌گیرد.

    Args:
        symbol (Union[Unset, str]):
        resolution (Union[Unset, str]):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMarketUdfHistoryResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        resolution=resolution,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    symbol: Union[Unset, str] = UNSET,
    resolution: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
) -> Optional[GetMarketUdfHistoryResponse200]:
    """OHLC

     ## آمار OHLC بازار نوبیتکس

    نوبیتکس از این نوع درخواست استفاده نمایید OHLCبرای دریافت آمار
    بازه زمانی کندل‌های خروجی می‌تواند یکی از مقادیر زیر باشد:

    *   یک ساعت :60
    *   یک روز :D


    ###### مقادیر پاسخ

    *   t (time): زمان شروع بازه
    *   o (open): قیمت شروع بازه
    *   c (close): قیمت پایان بازه
    *   l (low): پایین‌ترین قیمت بازه
    *   h(high): بالاترین قیمت بازه
    *   v (volume): حجم بازه


    که برای هر کندل در بازه زمانی گزارش یک عدد در لیست قرار می‌گیرد.

    Args:
        symbol (Union[Unset, str]):
        resolution (Union[Unset, str]):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMarketUdfHistoryResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            symbol=symbol,
            resolution=resolution,
            from_=from_,
            to=to,
        )
    ).parsed
