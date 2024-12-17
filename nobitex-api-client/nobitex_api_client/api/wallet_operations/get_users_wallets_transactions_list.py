from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_wallets_transactions_list_response_200 import GetUsersWalletsTransactionsListResponse200
from ...models.get_users_wallets_transactions_list_response_404 import GetUsersWalletsTransactionsListResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    wallet: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["wallet"] = wallet

    params["page"] = page

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/wallets/transactions/list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetUsersWalletsTransactionsListResponse200, GetUsersWalletsTransactionsListResponse404]]:
    if response.status_code == 200:
        response_200 = GetUsersWalletsTransactionsListResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = GetUsersWalletsTransactionsListResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetUsersWalletsTransactionsListResponse200, GetUsersWalletsTransactionsListResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    wallet: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[Union[GetUsersWalletsTransactionsListResponse200, GetUsersWalletsTransactionsListResponse404]]:
    """Transactions list

     ## لیست تراکنش ها

    برای دریافت لیست تراکنش‌های یک کیف پول شامل واریز، برداشت، خرید، فروش و ... از این درخواست استفاده
    نمایید:

    Args:
        wallet (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetUsersWalletsTransactionsListResponse200, GetUsersWalletsTransactionsListResponse404]]
    """

    kwargs = _get_kwargs(
        wallet=wallet,
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
    wallet: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[Union[GetUsersWalletsTransactionsListResponse200, GetUsersWalletsTransactionsListResponse404]]:
    """Transactions list

     ## لیست تراکنش ها

    برای دریافت لیست تراکنش‌های یک کیف پول شامل واریز، برداشت، خرید، فروش و ... از این درخواست استفاده
    نمایید:

    Args:
        wallet (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetUsersWalletsTransactionsListResponse200, GetUsersWalletsTransactionsListResponse404]
    """

    return sync_detailed(
        client=client,
        wallet=wallet,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    wallet: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[Union[GetUsersWalletsTransactionsListResponse200, GetUsersWalletsTransactionsListResponse404]]:
    """Transactions list

     ## لیست تراکنش ها

    برای دریافت لیست تراکنش‌های یک کیف پول شامل واریز، برداشت، خرید، فروش و ... از این درخواست استفاده
    نمایید:

    Args:
        wallet (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetUsersWalletsTransactionsListResponse200, GetUsersWalletsTransactionsListResponse404]]
    """

    kwargs = _get_kwargs(
        wallet=wallet,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    wallet: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[Union[GetUsersWalletsTransactionsListResponse200, GetUsersWalletsTransactionsListResponse404]]:
    """Transactions list

     ## لیست تراکنش ها

    برای دریافت لیست تراکنش‌های یک کیف پول شامل واریز، برداشت، خرید، فروش و ... از این درخواست استفاده
    نمایید:

    Args:
        wallet (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetUsersWalletsTransactionsListResponse200, GetUsersWalletsTransactionsListResponse404]
    """

    return (
        await asyncio_detailed(
            client=client,
            wallet=wallet,
            page=page,
            page_size=page_size,
        )
    ).parsed
