from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_market_orders_status_response_200 import GetMarketOrdersStatusResponse200
from ...models.get_market_orders_status_response_404 import GetMarketOrdersStatusResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: Union[Unset, int] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["id"] = id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/market/orders/status",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetMarketOrdersStatusResponse200, GetMarketOrdersStatusResponse404]]:
    if response.status_code == 200:
        response_200 = GetMarketOrdersStatusResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = GetMarketOrdersStatusResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetMarketOrdersStatusResponse200, GetMarketOrdersStatusResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, int] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[GetMarketOrdersStatusResponse200, GetMarketOrdersStatusResponse404]]:
    """Orders status

     ## مشاهده وضعیت سفارش

    برای دریافت وضعیت سفارش از این نوع درخواست استفاده نمایید.

    مقادیر وضعیت:

    *   `Active`: سفارش مقدار پر نشده برای شرکت در معاملات دارد و در بازار فعال است.
    *   `Done`: سفارش تماما معامله شده است.
    *   `Inactive`: سفارش حد ضرر هنوز به محدوده قیمت توقف تعیین شده نرسیده و غیرفعال است.
    *   `Canceled`: سفارش پیش از پر شدن کامل توسط کاربر یا سامانه لغو شده است. سفارش به چند دلیل
    می‌تواند توسط سامانه لغو شود:
        *   مقدار سفارش کافی در بازار در بازه ۱٪ قیمت تعیین شده برای پر کردن سفارش وجود نداشته است.
        *   موجودی کیف پول کاربر از طریق سایر تراکنش‌ها کاهش یافته است و از موجودی لازم برای پر شدن
    معامله کمتر شده است.
        *   زوج سفارش oco انجام گرفته است.

    Args:
        id (Union[Unset, int]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetMarketOrdersStatusResponse200, GetMarketOrdersStatusResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, int] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[GetMarketOrdersStatusResponse200, GetMarketOrdersStatusResponse404]]:
    """Orders status

     ## مشاهده وضعیت سفارش

    برای دریافت وضعیت سفارش از این نوع درخواست استفاده نمایید.

    مقادیر وضعیت:

    *   `Active`: سفارش مقدار پر نشده برای شرکت در معاملات دارد و در بازار فعال است.
    *   `Done`: سفارش تماما معامله شده است.
    *   `Inactive`: سفارش حد ضرر هنوز به محدوده قیمت توقف تعیین شده نرسیده و غیرفعال است.
    *   `Canceled`: سفارش پیش از پر شدن کامل توسط کاربر یا سامانه لغو شده است. سفارش به چند دلیل
    می‌تواند توسط سامانه لغو شود:
        *   مقدار سفارش کافی در بازار در بازه ۱٪ قیمت تعیین شده برای پر کردن سفارش وجود نداشته است.
        *   موجودی کیف پول کاربر از طریق سایر تراکنش‌ها کاهش یافته است و از موجودی لازم برای پر شدن
    معامله کمتر شده است.
        *   زوج سفارش oco انجام گرفته است.

    Args:
        id (Union[Unset, int]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetMarketOrdersStatusResponse200, GetMarketOrdersStatusResponse404]
    """

    return sync_detailed(
        client=client,
        id=id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, int] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[GetMarketOrdersStatusResponse200, GetMarketOrdersStatusResponse404]]:
    """Orders status

     ## مشاهده وضعیت سفارش

    برای دریافت وضعیت سفارش از این نوع درخواست استفاده نمایید.

    مقادیر وضعیت:

    *   `Active`: سفارش مقدار پر نشده برای شرکت در معاملات دارد و در بازار فعال است.
    *   `Done`: سفارش تماما معامله شده است.
    *   `Inactive`: سفارش حد ضرر هنوز به محدوده قیمت توقف تعیین شده نرسیده و غیرفعال است.
    *   `Canceled`: سفارش پیش از پر شدن کامل توسط کاربر یا سامانه لغو شده است. سفارش به چند دلیل
    می‌تواند توسط سامانه لغو شود:
        *   مقدار سفارش کافی در بازار در بازه ۱٪ قیمت تعیین شده برای پر کردن سفارش وجود نداشته است.
        *   موجودی کیف پول کاربر از طریق سایر تراکنش‌ها کاهش یافته است و از موجودی لازم برای پر شدن
    معامله کمتر شده است.
        *   زوج سفارش oco انجام گرفته است.

    Args:
        id (Union[Unset, int]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetMarketOrdersStatusResponse200, GetMarketOrdersStatusResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    id: Union[Unset, int] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[GetMarketOrdersStatusResponse200, GetMarketOrdersStatusResponse404]]:
    """Orders status

     ## مشاهده وضعیت سفارش

    برای دریافت وضعیت سفارش از این نوع درخواست استفاده نمایید.

    مقادیر وضعیت:

    *   `Active`: سفارش مقدار پر نشده برای شرکت در معاملات دارد و در بازار فعال است.
    *   `Done`: سفارش تماما معامله شده است.
    *   `Inactive`: سفارش حد ضرر هنوز به محدوده قیمت توقف تعیین شده نرسیده و غیرفعال است.
    *   `Canceled`: سفارش پیش از پر شدن کامل توسط کاربر یا سامانه لغو شده است. سفارش به چند دلیل
    می‌تواند توسط سامانه لغو شود:
        *   مقدار سفارش کافی در بازار در بازه ۱٪ قیمت تعیین شده برای پر کردن سفارش وجود نداشته است.
        *   موجودی کیف پول کاربر از طریق سایر تراکنش‌ها کاهش یافته است و از موجودی لازم برای پر شدن
    معامله کمتر شده است.
        *   زوج سفارش oco انجام گرفته است.

    Args:
        id (Union[Unset, int]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetMarketOrdersStatusResponse200, GetMarketOrdersStatusResponse404]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            authorization=authorization,
        )
    ).parsed
