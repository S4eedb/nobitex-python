from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_wallets_withdraws_list_response_200 import GetUsersWalletsWithdrawsListResponse200
from ...models.get_users_wallets_withdraws_list_response_404 import GetUsersWalletsWithdrawsListResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    wallet: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["wallet"] = wallet

    params["from"] = from_

    params["to"] = to

    params["page"] = page

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/wallets/withdraws/list",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetUsersWalletsWithdrawsListResponse200, GetUsersWalletsWithdrawsListResponse404]]:
    if response.status_code == 200:
        response_200 = GetUsersWalletsWithdrawsListResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = GetUsersWalletsWithdrawsListResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetUsersWalletsWithdrawsListResponse200, GetUsersWalletsWithdrawsListResponse404]]:
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
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[Union[GetUsersWalletsWithdrawsListResponse200, GetUsersWalletsWithdrawsListResponse404]]:
    """Withdraws list

     ## فهرست برداشت‌ها

    برای دریافت لیست آخرین برداشت‌ها از این نوع درخواست استفاده نمایید. درخواست برداشت‌های تایید نشده در
    اینجا نمایش داده نخواهند شد.

    محدودیت فراخوانی: ۶۰ درخواست در ۲ دقیقه

    Args:
        wallet (Union[Unset, str]):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetUsersWalletsWithdrawsListResponse200, GetUsersWalletsWithdrawsListResponse404]]
    """

    kwargs = _get_kwargs(
        wallet=wallet,
        from_=from_,
        to=to,
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
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[Union[GetUsersWalletsWithdrawsListResponse200, GetUsersWalletsWithdrawsListResponse404]]:
    """Withdraws list

     ## فهرست برداشت‌ها

    برای دریافت لیست آخرین برداشت‌ها از این نوع درخواست استفاده نمایید. درخواست برداشت‌های تایید نشده در
    اینجا نمایش داده نخواهند شد.

    محدودیت فراخوانی: ۶۰ درخواست در ۲ دقیقه

    Args:
        wallet (Union[Unset, str]):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetUsersWalletsWithdrawsListResponse200, GetUsersWalletsWithdrawsListResponse404]
    """

    return sync_detailed(
        client=client,
        wallet=wallet,
        from_=from_,
        to=to,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    wallet: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Response[Union[GetUsersWalletsWithdrawsListResponse200, GetUsersWalletsWithdrawsListResponse404]]:
    """Withdraws list

     ## فهرست برداشت‌ها

    برای دریافت لیست آخرین برداشت‌ها از این نوع درخواست استفاده نمایید. درخواست برداشت‌های تایید نشده در
    اینجا نمایش داده نخواهند شد.

    محدودیت فراخوانی: ۶۰ درخواست در ۲ دقیقه

    Args:
        wallet (Union[Unset, str]):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetUsersWalletsWithdrawsListResponse200, GetUsersWalletsWithdrawsListResponse404]]
    """

    kwargs = _get_kwargs(
        wallet=wallet,
        from_=from_,
        to=to,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    wallet: Union[Unset, str] = UNSET,
    from_: Union[Unset, str] = UNSET,
    to: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
) -> Optional[Union[GetUsersWalletsWithdrawsListResponse200, GetUsersWalletsWithdrawsListResponse404]]:
    """Withdraws list

     ## فهرست برداشت‌ها

    برای دریافت لیست آخرین برداشت‌ها از این نوع درخواست استفاده نمایید. درخواست برداشت‌های تایید نشده در
    اینجا نمایش داده نخواهند شد.

    محدودیت فراخوانی: ۶۰ درخواست در ۲ دقیقه

    Args:
        wallet (Union[Unset, str]):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetUsersWalletsWithdrawsListResponse200, GetUsersWalletsWithdrawsListResponse404]
    """

    return (
        await asyncio_detailed(
            client=client,
            wallet=wallet,
            from_=from_,
            to=to,
            page=page,
            page_size=page_size,
        )
    ).parsed