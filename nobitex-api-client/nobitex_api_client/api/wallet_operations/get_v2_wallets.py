from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v2_wallets_response_200 import GetV2WalletsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    currencies: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["currencies"] = currencies

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/wallets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetV2WalletsResponse200]:
    if response.status_code == 200:
        response_200 = GetV2WalletsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetV2WalletsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    currencies: Union[Unset, str] = UNSET,
) -> Response[GetV2WalletsResponse200]:
    """Wallets lists

     ## لیست کیف پول‌ها

    به کمک این درخواست شناسه، موجودی و موجودی بلوکه هر رمزارز دلخواه خود را بیابید.

    در صورتی که ارز مشخصی انتخاب نکرده باشید، همه کیف پول‌هایی که برای شما به واسطه ایجاد آدرس کیف پول
    یا ثبت سفارش در آن بازار ایجاد شده باشد، بازگردانده می‌شود.

    رمزارزهای مورد پشتیبانی عبارتند از:
    {{currencies}}

    برای درخواست همزمان چند کیف پول از ترکیب رمزارزها با ویرگول (,) استفاده کنید.

    Args:
        currencies (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV2WalletsResponse200]
    """

    kwargs = _get_kwargs(
        currencies=currencies,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    currencies: Union[Unset, str] = UNSET,
) -> Optional[GetV2WalletsResponse200]:
    """Wallets lists

     ## لیست کیف پول‌ها

    به کمک این درخواست شناسه، موجودی و موجودی بلوکه هر رمزارز دلخواه خود را بیابید.

    در صورتی که ارز مشخصی انتخاب نکرده باشید، همه کیف پول‌هایی که برای شما به واسطه ایجاد آدرس کیف پول
    یا ثبت سفارش در آن بازار ایجاد شده باشد، بازگردانده می‌شود.

    رمزارزهای مورد پشتیبانی عبارتند از:
    {{currencies}}

    برای درخواست همزمان چند کیف پول از ترکیب رمزارزها با ویرگول (,) استفاده کنید.

    Args:
        currencies (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV2WalletsResponse200
    """

    return sync_detailed(
        client=client,
        currencies=currencies,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    currencies: Union[Unset, str] = UNSET,
) -> Response[GetV2WalletsResponse200]:
    """Wallets lists

     ## لیست کیف پول‌ها

    به کمک این درخواست شناسه، موجودی و موجودی بلوکه هر رمزارز دلخواه خود را بیابید.

    در صورتی که ارز مشخصی انتخاب نکرده باشید، همه کیف پول‌هایی که برای شما به واسطه ایجاد آدرس کیف پول
    یا ثبت سفارش در آن بازار ایجاد شده باشد، بازگردانده می‌شود.

    رمزارزهای مورد پشتیبانی عبارتند از:
    {{currencies}}

    برای درخواست همزمان چند کیف پول از ترکیب رمزارزها با ویرگول (,) استفاده کنید.

    Args:
        currencies (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV2WalletsResponse200]
    """

    kwargs = _get_kwargs(
        currencies=currencies,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    currencies: Union[Unset, str] = UNSET,
) -> Optional[GetV2WalletsResponse200]:
    """Wallets lists

     ## لیست کیف پول‌ها

    به کمک این درخواست شناسه، موجودی و موجودی بلوکه هر رمزارز دلخواه خود را بیابید.

    در صورتی که ارز مشخصی انتخاب نکرده باشید، همه کیف پول‌هایی که برای شما به واسطه ایجاد آدرس کیف پول
    یا ثبت سفارش در آن بازار ایجاد شده باشد، بازگردانده می‌شود.

    رمزارزهای مورد پشتیبانی عبارتند از:
    {{currencies}}

    برای درخواست همزمان چند کیف پول از ترکیب رمزارزها با ویرگول (,) استفاده کنید.

    Args:
        currencies (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV2WalletsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            currencies=currencies,
        )
    ).parsed
