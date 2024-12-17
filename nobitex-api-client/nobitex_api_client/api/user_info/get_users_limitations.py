from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_users_limitations_response_200 import GetUsersLimitationsResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/limitations",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetUsersLimitationsResponse200]:
    if response.status_code == 200:
        response_200 = GetUsersLimitationsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetUsersLimitationsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetUsersLimitationsResponse200]:
    """Limitations

     ## محدودیت های کاربر

    کاربران در نوبیتکس بر اساس سطح کاربری خود، محدودیت هایی در برداشت، واریز و مبادلات خود دارند. هر
    کاربر نسبت به نیاز خود و میزان مبادلاتی که دارد، می‌تواند با ارائه مدارک مورد نیاز ، سطح کاربری خود
    را پس از احراز هویت و تایید مدراک، ارتقا دهد.
    برای دریافت محدودیت های کاربر از این نوع درخواست استفاده نمایید:

    ###### features: شرایط حساب کاربری

    *   crypto_trade: امکان مبادله رمز ارزها
    *   rial_trade: امکان مبادله با ریال
    *   coin_deposit: امکان واریز رمز ارز به کیف پول نوبیتکس
    *   rial_deposit: امکان واریز ریال به کیف پول نوبیتکس
    *   coin_withdrawal: امکان برداشت رمز ارز از کیف پول نوبیتکس به کیف پول دیگر
    *   rial_withdrawal: امکان برداشت ریال از کیف پول نوبیتکس به حساب بانکی


    ###### limits: محدودیت های حساب کاربری

    *   withdrawRialDaily: مقدار مجاز برای برداشت روزانه ریال
    *   withdrawCoinDaily: مقدار مجاز برای برداشت روزانه رمز ارز
    *   withdrawTotalDaily: مقدار مجاز برای برداشت روزانه مجموع رمز ارز و ریال
    *   withdrawTotalMonthly: مقدار مجاز برای برداشت ماهیانه مجموع رمز ارز و ریال


    این مقادیر در واحد ریال هستند.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersLimitationsResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetUsersLimitationsResponse200]:
    """Limitations

     ## محدودیت های کاربر

    کاربران در نوبیتکس بر اساس سطح کاربری خود، محدودیت هایی در برداشت، واریز و مبادلات خود دارند. هر
    کاربر نسبت به نیاز خود و میزان مبادلاتی که دارد، می‌تواند با ارائه مدارک مورد نیاز ، سطح کاربری خود
    را پس از احراز هویت و تایید مدراک، ارتقا دهد.
    برای دریافت محدودیت های کاربر از این نوع درخواست استفاده نمایید:

    ###### features: شرایط حساب کاربری

    *   crypto_trade: امکان مبادله رمز ارزها
    *   rial_trade: امکان مبادله با ریال
    *   coin_deposit: امکان واریز رمز ارز به کیف پول نوبیتکس
    *   rial_deposit: امکان واریز ریال به کیف پول نوبیتکس
    *   coin_withdrawal: امکان برداشت رمز ارز از کیف پول نوبیتکس به کیف پول دیگر
    *   rial_withdrawal: امکان برداشت ریال از کیف پول نوبیتکس به حساب بانکی


    ###### limits: محدودیت های حساب کاربری

    *   withdrawRialDaily: مقدار مجاز برای برداشت روزانه ریال
    *   withdrawCoinDaily: مقدار مجاز برای برداشت روزانه رمز ارز
    *   withdrawTotalDaily: مقدار مجاز برای برداشت روزانه مجموع رمز ارز و ریال
    *   withdrawTotalMonthly: مقدار مجاز برای برداشت ماهیانه مجموع رمز ارز و ریال


    این مقادیر در واحد ریال هستند.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersLimitationsResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetUsersLimitationsResponse200]:
    """Limitations

     ## محدودیت های کاربر

    کاربران در نوبیتکس بر اساس سطح کاربری خود، محدودیت هایی در برداشت، واریز و مبادلات خود دارند. هر
    کاربر نسبت به نیاز خود و میزان مبادلاتی که دارد، می‌تواند با ارائه مدارک مورد نیاز ، سطح کاربری خود
    را پس از احراز هویت و تایید مدراک، ارتقا دهد.
    برای دریافت محدودیت های کاربر از این نوع درخواست استفاده نمایید:

    ###### features: شرایط حساب کاربری

    *   crypto_trade: امکان مبادله رمز ارزها
    *   rial_trade: امکان مبادله با ریال
    *   coin_deposit: امکان واریز رمز ارز به کیف پول نوبیتکس
    *   rial_deposit: امکان واریز ریال به کیف پول نوبیتکس
    *   coin_withdrawal: امکان برداشت رمز ارز از کیف پول نوبیتکس به کیف پول دیگر
    *   rial_withdrawal: امکان برداشت ریال از کیف پول نوبیتکس به حساب بانکی


    ###### limits: محدودیت های حساب کاربری

    *   withdrawRialDaily: مقدار مجاز برای برداشت روزانه ریال
    *   withdrawCoinDaily: مقدار مجاز برای برداشت روزانه رمز ارز
    *   withdrawTotalDaily: مقدار مجاز برای برداشت روزانه مجموع رمز ارز و ریال
    *   withdrawTotalMonthly: مقدار مجاز برای برداشت ماهیانه مجموع رمز ارز و ریال


    این مقادیر در واحد ریال هستند.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersLimitationsResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetUsersLimitationsResponse200]:
    """Limitations

     ## محدودیت های کاربر

    کاربران در نوبیتکس بر اساس سطح کاربری خود، محدودیت هایی در برداشت، واریز و مبادلات خود دارند. هر
    کاربر نسبت به نیاز خود و میزان مبادلاتی که دارد، می‌تواند با ارائه مدارک مورد نیاز ، سطح کاربری خود
    را پس از احراز هویت و تایید مدراک، ارتقا دهد.
    برای دریافت محدودیت های کاربر از این نوع درخواست استفاده نمایید:

    ###### features: شرایط حساب کاربری

    *   crypto_trade: امکان مبادله رمز ارزها
    *   rial_trade: امکان مبادله با ریال
    *   coin_deposit: امکان واریز رمز ارز به کیف پول نوبیتکس
    *   rial_deposit: امکان واریز ریال به کیف پول نوبیتکس
    *   coin_withdrawal: امکان برداشت رمز ارز از کیف پول نوبیتکس به کیف پول دیگر
    *   rial_withdrawal: امکان برداشت ریال از کیف پول نوبیتکس به حساب بانکی


    ###### limits: محدودیت های حساب کاربری

    *   withdrawRialDaily: مقدار مجاز برای برداشت روزانه ریال
    *   withdrawCoinDaily: مقدار مجاز برای برداشت روزانه رمز ارز
    *   withdrawTotalDaily: مقدار مجاز برای برداشت روزانه مجموع رمز ارز و ریال
    *   withdrawTotalMonthly: مقدار مجاز برای برداشت ماهیانه مجموع رمز ارز و ریال


    این مقادیر در واحد ریال هستند.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersLimitationsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
