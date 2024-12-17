from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_market_orders_update_status_body import PostMarketOrdersUpdateStatusBody
from ...models.post_market_orders_update_status_response_200 import PostMarketOrdersUpdateStatusResponse200
from ...models.post_market_orders_update_status_response_404 import PostMarketOrdersUpdateStatusResponse404
from ...types import Response


def _get_kwargs(
    *,
    body: PostMarketOrdersUpdateStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/market/orders/update-status",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[PostMarketOrdersUpdateStatusResponse200, PostMarketOrdersUpdateStatusResponse404]]:
    if response.status_code == 200:
        response_200 = PostMarketOrdersUpdateStatusResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = PostMarketOrdersUpdateStatusResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[PostMarketOrdersUpdateStatusResponse200, PostMarketOrdersUpdateStatusResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMarketOrdersUpdateStatusBody,
) -> Response[Union[PostMarketOrdersUpdateStatusResponse200, PostMarketOrdersUpdateStatusResponse404]]:
    """Update status

     ## به روزرسانی سفارش

    برای سفارش گذاری از این نوع درخواست استفاده نمایید:

    گذارهای مجاز وضعیت:

    *   `active`:
        *   `canceled`
    *   `inactive`:
        *   `canceled`

    در صورتی که سفارش درخواست شده جزئی از یک سفارش OCO انجام نشده باشد، هر دو سفارش مرتبط لغو خواهند شد.

    محدودیت فراخوانی : ۱۰۰ درخواست در ۱۰ دقیقه

    Args:
        body (PostMarketOrdersUpdateStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostMarketOrdersUpdateStatusResponse200, PostMarketOrdersUpdateStatusResponse404]]
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
    body: PostMarketOrdersUpdateStatusBody,
) -> Optional[Union[PostMarketOrdersUpdateStatusResponse200, PostMarketOrdersUpdateStatusResponse404]]:
    """Update status

     ## به روزرسانی سفارش

    برای سفارش گذاری از این نوع درخواست استفاده نمایید:

    گذارهای مجاز وضعیت:

    *   `active`:
        *   `canceled`
    *   `inactive`:
        *   `canceled`

    در صورتی که سفارش درخواست شده جزئی از یک سفارش OCO انجام نشده باشد، هر دو سفارش مرتبط لغو خواهند شد.

    محدودیت فراخوانی : ۱۰۰ درخواست در ۱۰ دقیقه

    Args:
        body (PostMarketOrdersUpdateStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostMarketOrdersUpdateStatusResponse200, PostMarketOrdersUpdateStatusResponse404]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMarketOrdersUpdateStatusBody,
) -> Response[Union[PostMarketOrdersUpdateStatusResponse200, PostMarketOrdersUpdateStatusResponse404]]:
    """Update status

     ## به روزرسانی سفارش

    برای سفارش گذاری از این نوع درخواست استفاده نمایید:

    گذارهای مجاز وضعیت:

    *   `active`:
        *   `canceled`
    *   `inactive`:
        *   `canceled`

    در صورتی که سفارش درخواست شده جزئی از یک سفارش OCO انجام نشده باشد، هر دو سفارش مرتبط لغو خواهند شد.

    محدودیت فراخوانی : ۱۰۰ درخواست در ۱۰ دقیقه

    Args:
        body (PostMarketOrdersUpdateStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostMarketOrdersUpdateStatusResponse200, PostMarketOrdersUpdateStatusResponse404]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMarketOrdersUpdateStatusBody,
) -> Optional[Union[PostMarketOrdersUpdateStatusResponse200, PostMarketOrdersUpdateStatusResponse404]]:
    """Update status

     ## به روزرسانی سفارش

    برای سفارش گذاری از این نوع درخواست استفاده نمایید:

    گذارهای مجاز وضعیت:

    *   `active`:
        *   `canceled`
    *   `inactive`:
        *   `canceled`

    در صورتی که سفارش درخواست شده جزئی از یک سفارش OCO انجام نشده باشد، هر دو سفارش مرتبط لغو خواهند شد.

    محدودیت فراخوانی : ۱۰۰ درخواست در ۱۰ دقیقه

    Args:
        body (PostMarketOrdersUpdateStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostMarketOrdersUpdateStatusResponse200, PostMarketOrdersUpdateStatusResponse404]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
