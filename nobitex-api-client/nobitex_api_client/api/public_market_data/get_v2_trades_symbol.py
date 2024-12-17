from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v2_trades_symbol_response_200 import GetV2TradesSymbolResponse200
from ...types import Response


def _get_kwargs(
    symbol: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/trades/{symbol}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetV2TradesSymbolResponse200]:
    if response.status_code == 200:
        response_200 = GetV2TradesSymbolResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetV2TradesSymbolResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    symbol: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetV2TradesSymbolResponse200]:
    """Trades

     ## لیست معاملات

    برای دریافت لیست معاملات انجام شده در بازار از این نوع درخواست استفاده نمایید:

    لیست نمادهای بازارها عبارتند از :
    {{symbols}}

    محدودیت فراخوانی: ۱۵ درخواست در دقیقه

    Args:
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV2TradesSymbolResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    symbol: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetV2TradesSymbolResponse200]:
    """Trades

     ## لیست معاملات

    برای دریافت لیست معاملات انجام شده در بازار از این نوع درخواست استفاده نمایید:

    لیست نمادهای بازارها عبارتند از :
    {{symbols}}

    محدودیت فراخوانی: ۱۵ درخواست در دقیقه

    Args:
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV2TradesSymbolResponse200
    """

    return sync_detailed(
        symbol=symbol,
        client=client,
    ).parsed


async def asyncio_detailed(
    symbol: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetV2TradesSymbolResponse200]:
    """Trades

     ## لیست معاملات

    برای دریافت لیست معاملات انجام شده در بازار از این نوع درخواست استفاده نمایید:

    لیست نمادهای بازارها عبارتند از :
    {{symbols}}

    محدودیت فراخوانی: ۱۵ درخواست در دقیقه

    Args:
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV2TradesSymbolResponse200]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    symbol: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetV2TradesSymbolResponse200]:
    """Trades

     ## لیست معاملات

    برای دریافت لیست معاملات انجام شده در بازار از این نوع درخواست استفاده نمایید:

    لیست نمادهای بازارها عبارتند از :
    {{symbols}}

    محدودیت فراخوانی: ۱۵ درخواست در دقیقه

    Args:
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV2TradesSymbolResponse200
    """

    return (
        await asyncio_detailed(
            symbol=symbol,
            client=client,
        )
    ).parsed
