from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_market_orders_cancel_old_body import PostMarketOrdersCancelOldBody
from ...models.post_market_orders_cancel_old_response_200 import PostMarketOrdersCancelOldResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostMarketOrdersCancelOldBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/market/orders/cancel-old",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostMarketOrdersCancelOldResponse200]:
    if response.status_code == 200:
        response_200 = PostMarketOrdersCancelOldResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostMarketOrdersCancelOldResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMarketOrdersCancelOldBody,
) -> Response[PostMarketOrdersCancelOldResponse200]:
    """Cancel  market orders

     ## لغو جمعی سفارشات

    برای لغو دسته‌جمعی سفارشات فعال یک بازار از این نوع درخواست استفاده نمایید

    رمزارزهای مبدا پشتیبانی شده:
    {{crypto_currencies}}

    ارزهای مقصد پشتیبانی شده:
    rls, usdt

    مقادیر نحوه اجرا:

    *   `limit`: با قیمت معین
    *   `market`: با قیمت بازار
    *   `stop_market`: حد ضرر
    *   `stop_limit`: حد ضرر معین


    سفارشات غیرفعال از این طریق لغو نخواهند شد.

    Args:
        body (PostMarketOrdersCancelOldBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostMarketOrdersCancelOldResponse200]
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
    body: PostMarketOrdersCancelOldBody,
) -> Optional[PostMarketOrdersCancelOldResponse200]:
    """Cancel  market orders

     ## لغو جمعی سفارشات

    برای لغو دسته‌جمعی سفارشات فعال یک بازار از این نوع درخواست استفاده نمایید

    رمزارزهای مبدا پشتیبانی شده:
    {{crypto_currencies}}

    ارزهای مقصد پشتیبانی شده:
    rls, usdt

    مقادیر نحوه اجرا:

    *   `limit`: با قیمت معین
    *   `market`: با قیمت بازار
    *   `stop_market`: حد ضرر
    *   `stop_limit`: حد ضرر معین


    سفارشات غیرفعال از این طریق لغو نخواهند شد.

    Args:
        body (PostMarketOrdersCancelOldBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostMarketOrdersCancelOldResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMarketOrdersCancelOldBody,
) -> Response[PostMarketOrdersCancelOldResponse200]:
    """Cancel  market orders

     ## لغو جمعی سفارشات

    برای لغو دسته‌جمعی سفارشات فعال یک بازار از این نوع درخواست استفاده نمایید

    رمزارزهای مبدا پشتیبانی شده:
    {{crypto_currencies}}

    ارزهای مقصد پشتیبانی شده:
    rls, usdt

    مقادیر نحوه اجرا:

    *   `limit`: با قیمت معین
    *   `market`: با قیمت بازار
    *   `stop_market`: حد ضرر
    *   `stop_limit`: حد ضرر معین


    سفارشات غیرفعال از این طریق لغو نخواهند شد.

    Args:
        body (PostMarketOrdersCancelOldBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostMarketOrdersCancelOldResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMarketOrdersCancelOldBody,
) -> Optional[PostMarketOrdersCancelOldResponse200]:
    """Cancel  market orders

     ## لغو جمعی سفارشات

    برای لغو دسته‌جمعی سفارشات فعال یک بازار از این نوع درخواست استفاده نمایید

    رمزارزهای مبدا پشتیبانی شده:
    {{crypto_currencies}}

    ارزهای مقصد پشتیبانی شده:
    rls, usdt

    مقادیر نحوه اجرا:

    *   `limit`: با قیمت معین
    *   `market`: با قیمت بازار
    *   `stop_market`: حد ضرر
    *   `stop_limit`: حد ضرر معین


    سفارشات غیرفعال از این طریق لغو نخواهند شد.

    Args:
        body (PostMarketOrdersCancelOldBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostMarketOrdersCancelOldResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
