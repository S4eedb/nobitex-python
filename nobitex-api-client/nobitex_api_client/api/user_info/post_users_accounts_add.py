from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_users_accounts_add_body import PostUsersAccountsAddBody
from ...models.post_users_accounts_add_response_200 import PostUsersAccountsAddResponse200
from ...models.post_users_accounts_add_response_401 import PostUsersAccountsAddResponse401
from ...types import Response


def _get_kwargs(
    *,
    body: PostUsersAccountsAddBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/accounts-add",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[PostUsersAccountsAddResponse200, PostUsersAccountsAddResponse401]]:
    if response.status_code == 200:
        response_200 = PostUsersAccountsAddResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = PostUsersAccountsAddResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[PostUsersAccountsAddResponse200, PostUsersAccountsAddResponse401]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersAccountsAddBody,
) -> Response[Union[PostUsersAccountsAddResponse200, PostUsersAccountsAddResponse401]]:
    """Accounts add

     ## افزودن حساب بانکی

    برای افزودن حساب بانکی جدید از این نوع درخواست استفاده نمایید:

    قبل از درج حساب باید نام، نام خانوادگی، کدملی و شماره همراه خود را در پروفایل نوبیتکس تکمیل کرده
    باشید.

    محدودیت فراخوانی : ۳۰ درخواست در ۳۰ دقیقه

    Args:
        body (PostUsersAccountsAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostUsersAccountsAddResponse200, PostUsersAccountsAddResponse401]]
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
    body: PostUsersAccountsAddBody,
) -> Optional[Union[PostUsersAccountsAddResponse200, PostUsersAccountsAddResponse401]]:
    """Accounts add

     ## افزودن حساب بانکی

    برای افزودن حساب بانکی جدید از این نوع درخواست استفاده نمایید:

    قبل از درج حساب باید نام، نام خانوادگی، کدملی و شماره همراه خود را در پروفایل نوبیتکس تکمیل کرده
    باشید.

    محدودیت فراخوانی : ۳۰ درخواست در ۳۰ دقیقه

    Args:
        body (PostUsersAccountsAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostUsersAccountsAddResponse200, PostUsersAccountsAddResponse401]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersAccountsAddBody,
) -> Response[Union[PostUsersAccountsAddResponse200, PostUsersAccountsAddResponse401]]:
    """Accounts add

     ## افزودن حساب بانکی

    برای افزودن حساب بانکی جدید از این نوع درخواست استفاده نمایید:

    قبل از درج حساب باید نام، نام خانوادگی، کدملی و شماره همراه خود را در پروفایل نوبیتکس تکمیل کرده
    باشید.

    محدودیت فراخوانی : ۳۰ درخواست در ۳۰ دقیقه

    Args:
        body (PostUsersAccountsAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostUsersAccountsAddResponse200, PostUsersAccountsAddResponse401]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersAccountsAddBody,
) -> Optional[Union[PostUsersAccountsAddResponse200, PostUsersAccountsAddResponse401]]:
    """Accounts add

     ## افزودن حساب بانکی

    برای افزودن حساب بانکی جدید از این نوع درخواست استفاده نمایید:

    قبل از درج حساب باید نام، نام خانوادگی، کدملی و شماره همراه خود را در پروفایل نوبیتکس تکمیل کرده
    باشید.

    محدودیت فراخوانی : ۳۰ درخواست در ۳۰ دقیقه

    Args:
        body (PostUsersAccountsAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostUsersAccountsAddResponse200, PostUsersAccountsAddResponse401]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed