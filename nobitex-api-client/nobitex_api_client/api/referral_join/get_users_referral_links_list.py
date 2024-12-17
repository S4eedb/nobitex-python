from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_referral_links_list_response_200 import GetUsersReferralLinksListResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/referral/links-list",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetUsersReferralLinksListResponse200]:
    if response.status_code == 200:
        response_200 = GetUsersReferralLinksListResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetUsersReferralLinksListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetUsersReferralLinksListResponse200]:
    """Referral codes list

     ## فهرست کدهای دعوت

    با استفاده از این درخواست می‌توانید فهرستی از کدهای دعوت فعلی خود را به همراه میزان سود شما و برخی
    دیگر از آمار مربوط به کاربران ثبت‌نامی با آن کد دعوت دریافت نمایید.

    مقادیر آماری عبارتند از:

    *   statsRegisters: کاربران ثبت‌نام کرده با این کد
    *   statsTrades: مجموع تعداد معاملات کاربران ثبت‌نام کرده با این کد
    *   statsProfit: مجموع ریالی درآمد کاربر از این کد


    محدودیت فراخوانی: ۵۰ درخواست در ۱۰ دقیقه

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersReferralLinksListResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetUsersReferralLinksListResponse200]:
    """Referral codes list

     ## فهرست کدهای دعوت

    با استفاده از این درخواست می‌توانید فهرستی از کدهای دعوت فعلی خود را به همراه میزان سود شما و برخی
    دیگر از آمار مربوط به کاربران ثبت‌نامی با آن کد دعوت دریافت نمایید.

    مقادیر آماری عبارتند از:

    *   statsRegisters: کاربران ثبت‌نام کرده با این کد
    *   statsTrades: مجموع تعداد معاملات کاربران ثبت‌نام کرده با این کد
    *   statsProfit: مجموع ریالی درآمد کاربر از این کد


    محدودیت فراخوانی: ۵۰ درخواست در ۱۰ دقیقه

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersReferralLinksListResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetUsersReferralLinksListResponse200]:
    """Referral codes list

     ## فهرست کدهای دعوت

    با استفاده از این درخواست می‌توانید فهرستی از کدهای دعوت فعلی خود را به همراه میزان سود شما و برخی
    دیگر از آمار مربوط به کاربران ثبت‌نامی با آن کد دعوت دریافت نمایید.

    مقادیر آماری عبارتند از:

    *   statsRegisters: کاربران ثبت‌نام کرده با این کد
    *   statsTrades: مجموع تعداد معاملات کاربران ثبت‌نام کرده با این کد
    *   statsProfit: مجموع ریالی درآمد کاربر از این کد


    محدودیت فراخوانی: ۵۰ درخواست در ۱۰ دقیقه

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersReferralLinksListResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetUsersReferralLinksListResponse200]:
    """Referral codes list

     ## فهرست کدهای دعوت

    با استفاده از این درخواست می‌توانید فهرستی از کدهای دعوت فعلی خود را به همراه میزان سود شما و برخی
    دیگر از آمار مربوط به کاربران ثبت‌نامی با آن کد دعوت دریافت نمایید.

    مقادیر آماری عبارتند از:

    *   statsRegisters: کاربران ثبت‌نام کرده با این کد
    *   statsTrades: مجموع تعداد معاملات کاربران ثبت‌نام کرده با این کد
    *   statsProfit: مجموع ریالی درآمد کاربر از این کد


    محدودیت فراخوانی: ۵۰ درخواست در ۱۰ دقیقه

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersReferralLinksListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
