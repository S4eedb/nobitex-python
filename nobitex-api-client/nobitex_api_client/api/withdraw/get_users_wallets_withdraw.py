from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_wallets_withdraw_response_200 import GetUsersWalletsWithdrawResponse200
from ...models.get_users_wallets_withdraw_response_404 import GetUsersWalletsWithdrawResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    x_totp: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_totp, Unset):
        headers["X-TOTP"] = x_totp

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/wallets/withdraw",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetUsersWalletsWithdrawResponse200, GetUsersWalletsWithdrawResponse404]]:
    if response.status_code == 200:
        response_200 = GetUsersWalletsWithdrawResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = GetUsersWalletsWithdrawResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetUsersWalletsWithdrawResponse200, GetUsersWalletsWithdrawResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    x_totp: Union[Unset, str] = UNSET,
) -> Response[Union[GetUsersWalletsWithdrawResponse200, GetUsersWalletsWithdrawResponse404]]:
    """Request withdraw

     ## ثبت درخواست برداشت

    مقادیر مجاز شبکه:

    {{networks}}

    شبکه‌های دارای تگ انتقال اجباری:

    {{tag_networks}}

    #### شرایط اجازه برداشت:

    *   کاربر درخواست دهنده حداقل سطح کاربری مجاز برای برداشت و شماره تماس تایید داشته باشد.
    *   سقف برداشت مجاز روزانه و ماهانه برای کاربر بسته به [سطوح
    کاربری](https://nobitex.ir/policies/user-levels/) متفاوت است. مطابق با قوانین این سقف می‌تواند بیشتر
    یا محدودتر شود.
    *   بعضی اعمال مانند لغو اضطراری برداشت منجر به غیر فعال شدن موقت امکان برداشت برای کاربر شود.


    محدودیت فراخوانی : ۱۰ درخواست در ۳ دقیقه

    Args:
        x_totp (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetUsersWalletsWithdrawResponse200, GetUsersWalletsWithdrawResponse404]]
    """

    kwargs = _get_kwargs(
        x_totp=x_totp,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    x_totp: Union[Unset, str] = UNSET,
) -> Optional[Union[GetUsersWalletsWithdrawResponse200, GetUsersWalletsWithdrawResponse404]]:
    """Request withdraw

     ## ثبت درخواست برداشت

    مقادیر مجاز شبکه:

    {{networks}}

    شبکه‌های دارای تگ انتقال اجباری:

    {{tag_networks}}

    #### شرایط اجازه برداشت:

    *   کاربر درخواست دهنده حداقل سطح کاربری مجاز برای برداشت و شماره تماس تایید داشته باشد.
    *   سقف برداشت مجاز روزانه و ماهانه برای کاربر بسته به [سطوح
    کاربری](https://nobitex.ir/policies/user-levels/) متفاوت است. مطابق با قوانین این سقف می‌تواند بیشتر
    یا محدودتر شود.
    *   بعضی اعمال مانند لغو اضطراری برداشت منجر به غیر فعال شدن موقت امکان برداشت برای کاربر شود.


    محدودیت فراخوانی : ۱۰ درخواست در ۳ دقیقه

    Args:
        x_totp (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetUsersWalletsWithdrawResponse200, GetUsersWalletsWithdrawResponse404]
    """

    return sync_detailed(
        client=client,
        x_totp=x_totp,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    x_totp: Union[Unset, str] = UNSET,
) -> Response[Union[GetUsersWalletsWithdrawResponse200, GetUsersWalletsWithdrawResponse404]]:
    """Request withdraw

     ## ثبت درخواست برداشت

    مقادیر مجاز شبکه:

    {{networks}}

    شبکه‌های دارای تگ انتقال اجباری:

    {{tag_networks}}

    #### شرایط اجازه برداشت:

    *   کاربر درخواست دهنده حداقل سطح کاربری مجاز برای برداشت و شماره تماس تایید داشته باشد.
    *   سقف برداشت مجاز روزانه و ماهانه برای کاربر بسته به [سطوح
    کاربری](https://nobitex.ir/policies/user-levels/) متفاوت است. مطابق با قوانین این سقف می‌تواند بیشتر
    یا محدودتر شود.
    *   بعضی اعمال مانند لغو اضطراری برداشت منجر به غیر فعال شدن موقت امکان برداشت برای کاربر شود.


    محدودیت فراخوانی : ۱۰ درخواست در ۳ دقیقه

    Args:
        x_totp (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetUsersWalletsWithdrawResponse200, GetUsersWalletsWithdrawResponse404]]
    """

    kwargs = _get_kwargs(
        x_totp=x_totp,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    x_totp: Union[Unset, str] = UNSET,
) -> Optional[Union[GetUsersWalletsWithdrawResponse200, GetUsersWalletsWithdrawResponse404]]:
    """Request withdraw

     ## ثبت درخواست برداشت

    مقادیر مجاز شبکه:

    {{networks}}

    شبکه‌های دارای تگ انتقال اجباری:

    {{tag_networks}}

    #### شرایط اجازه برداشت:

    *   کاربر درخواست دهنده حداقل سطح کاربری مجاز برای برداشت و شماره تماس تایید داشته باشد.
    *   سقف برداشت مجاز روزانه و ماهانه برای کاربر بسته به [سطوح
    کاربری](https://nobitex.ir/policies/user-levels/) متفاوت است. مطابق با قوانین این سقف می‌تواند بیشتر
    یا محدودتر شود.
    *   بعضی اعمال مانند لغو اضطراری برداشت منجر به غیر فعال شدن موقت امکان برداشت برای کاربر شود.


    محدودیت فراخوانی : ۱۰ درخواست در ۳ دقیقه

    Args:
        x_totp (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetUsersWalletsWithdrawResponse200, GetUsersWalletsWithdrawResponse404]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_totp=x_totp,
        )
    ).parsed
