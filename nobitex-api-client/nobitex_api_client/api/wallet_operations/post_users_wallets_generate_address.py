from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_users_wallets_generate_address_body import PostUsersWalletsGenerateAddressBody
from ...models.post_users_wallets_generate_address_response_200 import PostUsersWalletsGenerateAddressResponse200
from ...models.post_users_wallets_generate_address_response_401 import PostUsersWalletsGenerateAddressResponse401
from ...types import Response


def _get_kwargs(
    *,
    body: PostUsersWalletsGenerateAddressBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/wallets/generate-address",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[PostUsersWalletsGenerateAddressResponse200, PostUsersWalletsGenerateAddressResponse401]]:
    if response.status_code == 200:
        response_200 = PostUsersWalletsGenerateAddressResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = PostUsersWalletsGenerateAddressResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[PostUsersWalletsGenerateAddressResponse200, PostUsersWalletsGenerateAddressResponse401]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersWalletsGenerateAddressBody,
) -> Response[Union[PostUsersWalletsGenerateAddressResponse200, PostUsersWalletsGenerateAddressResponse401]]:
    """Generate wallet address

     ## تولید آدرس بلاکچین

    به کمک این درخواست کیف پول برای رمزارز خود ایجاد کنید و آدرس بلاکچین جهت واریز و برداشت رمزارز به آن
    اختصاص دهید.

    رمزارزهای مورد پشتیبانی عبارتند از:
    {{crypto_currencies}}

    شبکه‌های قابل قبول عبارتند از:
    {{networks}}

    برای مشاهده شبکه‌های مورد پشتیبانی برای هر رمزارز، از ای‌پی‌آی تنظیمات سیستم استفاده نمایید.

    نوع پروتکل در حال حاضر تنها برای بیت‌کوین مورد استفاده است:

    *   legacy: روش قدیمی
    *   default: سِگویت

    Args:
        body (PostUsersWalletsGenerateAddressBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostUsersWalletsGenerateAddressResponse200, PostUsersWalletsGenerateAddressResponse401]]
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
    body: PostUsersWalletsGenerateAddressBody,
) -> Optional[Union[PostUsersWalletsGenerateAddressResponse200, PostUsersWalletsGenerateAddressResponse401]]:
    """Generate wallet address

     ## تولید آدرس بلاکچین

    به کمک این درخواست کیف پول برای رمزارز خود ایجاد کنید و آدرس بلاکچین جهت واریز و برداشت رمزارز به آن
    اختصاص دهید.

    رمزارزهای مورد پشتیبانی عبارتند از:
    {{crypto_currencies}}

    شبکه‌های قابل قبول عبارتند از:
    {{networks}}

    برای مشاهده شبکه‌های مورد پشتیبانی برای هر رمزارز، از ای‌پی‌آی تنظیمات سیستم استفاده نمایید.

    نوع پروتکل در حال حاضر تنها برای بیت‌کوین مورد استفاده است:

    *   legacy: روش قدیمی
    *   default: سِگویت

    Args:
        body (PostUsersWalletsGenerateAddressBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostUsersWalletsGenerateAddressResponse200, PostUsersWalletsGenerateAddressResponse401]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersWalletsGenerateAddressBody,
) -> Response[Union[PostUsersWalletsGenerateAddressResponse200, PostUsersWalletsGenerateAddressResponse401]]:
    """Generate wallet address

     ## تولید آدرس بلاکچین

    به کمک این درخواست کیف پول برای رمزارز خود ایجاد کنید و آدرس بلاکچین جهت واریز و برداشت رمزارز به آن
    اختصاص دهید.

    رمزارزهای مورد پشتیبانی عبارتند از:
    {{crypto_currencies}}

    شبکه‌های قابل قبول عبارتند از:
    {{networks}}

    برای مشاهده شبکه‌های مورد پشتیبانی برای هر رمزارز، از ای‌پی‌آی تنظیمات سیستم استفاده نمایید.

    نوع پروتکل در حال حاضر تنها برای بیت‌کوین مورد استفاده است:

    *   legacy: روش قدیمی
    *   default: سِگویت

    Args:
        body (PostUsersWalletsGenerateAddressBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostUsersWalletsGenerateAddressResponse200, PostUsersWalletsGenerateAddressResponse401]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersWalletsGenerateAddressBody,
) -> Optional[Union[PostUsersWalletsGenerateAddressResponse200, PostUsersWalletsGenerateAddressResponse401]]:
    """Generate wallet address

     ## تولید آدرس بلاکچین

    به کمک این درخواست کیف پول برای رمزارز خود ایجاد کنید و آدرس بلاکچین جهت واریز و برداشت رمزارز به آن
    اختصاص دهید.

    رمزارزهای مورد پشتیبانی عبارتند از:
    {{crypto_currencies}}

    شبکه‌های قابل قبول عبارتند از:
    {{networks}}

    برای مشاهده شبکه‌های مورد پشتیبانی برای هر رمزارز، از ای‌پی‌آی تنظیمات سیستم استفاده نمایید.

    نوع پروتکل در حال حاضر تنها برای بیت‌کوین مورد استفاده است:

    *   legacy: روش قدیمی
    *   default: سِگویت

    Args:
        body (PostUsersWalletsGenerateAddressBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostUsersWalletsGenerateAddressResponse200, PostUsersWalletsGenerateAddressResponse401]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
