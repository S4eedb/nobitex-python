from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_market_stats_body import PostMarketStatsBody
from ...models.post_market_stats_response_200 import PostMarketStatsResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostMarketStatsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/market/stats",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostMarketStatsResponse200]:
    if response.status_code == 200:
        response_200 = PostMarketStatsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostMarketStatsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMarketStatsBody,
) -> Response[PostMarketStatsResponse200]:
    """Stats

     ## وضعیت بازار نوبیتکس

    برای دریافت آخرین آمار بازار نوبیتکس (شامل بهترین قیمت خرید و فروش در لحظه، بالاترین و پایین‌ترین
    قیمت در ۲۴ ساعت گذشته، حجم بازار و ...) از این نوع درخواست استفاده نمایید:

    انواع ارز:
    {{currencies}}

    محدودیت فراخوانی: ۱۰۰ درخواست در ۱۰ دقیقه

    Args:
        body (PostMarketStatsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostMarketStatsResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMarketStatsBody,
) -> Optional[PostMarketStatsResponse200]:
    """Stats

     ## وضعیت بازار نوبیتکس

    برای دریافت آخرین آمار بازار نوبیتکس (شامل بهترین قیمت خرید و فروش در لحظه، بالاترین و پایین‌ترین
    قیمت در ۲۴ ساعت گذشته، حجم بازار و ...) از این نوع درخواست استفاده نمایید:

    انواع ارز:
    {{currencies}}

    محدودیت فراخوانی: ۱۰۰ درخواست در ۱۰ دقیقه

    Args:
        body (PostMarketStatsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostMarketStatsResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMarketStatsBody,
) -> Response[PostMarketStatsResponse200]:
    """Stats

     ## وضعیت بازار نوبیتکس

    برای دریافت آخرین آمار بازار نوبیتکس (شامل بهترین قیمت خرید و فروش در لحظه، بالاترین و پایین‌ترین
    قیمت در ۲۴ ساعت گذشته، حجم بازار و ...) از این نوع درخواست استفاده نمایید:

    انواع ارز:
    {{currencies}}

    محدودیت فراخوانی: ۱۰۰ درخواست در ۱۰ دقیقه

    Args:
        body (PostMarketStatsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostMarketStatsResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMarketStatsBody,
) -> Optional[PostMarketStatsResponse200]:
    """Stats

     ## وضعیت بازار نوبیتکس

    برای دریافت آخرین آمار بازار نوبیتکس (شامل بهترین قیمت خرید و فروش در لحظه، بالاترین و پایین‌ترین
    قیمت در ۲۴ ساعت گذشته، حجم بازار و ...) از این نوع درخواست استفاده نمایید:

    انواع ارز:
    {{currencies}}

    محدودیت فراخوانی: ۱۰۰ درخواست در ۱۰ دقیقه

    Args:
        body (PostMarketStatsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostMarketStatsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
