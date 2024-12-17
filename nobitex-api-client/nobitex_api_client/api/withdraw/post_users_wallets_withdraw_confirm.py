from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_users_wallets_withdraw_confirm_body import PostUsersWalletsWithdrawConfirmBody
from ...models.post_users_wallets_withdraw_confirm_response_200 import PostUsersWalletsWithdrawConfirmResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostUsersWalletsWithdrawConfirmBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/wallets/withdraw-confirm",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostUsersWalletsWithdrawConfirmResponse200]:
    if response.status_code == 200:
        response_200 = PostUsersWalletsWithdrawConfirmResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostUsersWalletsWithdrawConfirmResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersWalletsWithdrawConfirmBody,
) -> Response[PostUsersWalletsWithdrawConfirmResponse200]:
    """Confirm withdraw

     ## تایید درخواست برداشت

    برای تایید برداشت باید کد ارسال شده به شماره تلفن همراه یا ایمیل حساب کاربری خود را از طریق کد به
    صورت خودکار دریافت کنید و به این API ارسال نمایید.

    محدودیت فراخوانی: 30 درخواست در ساعت

    Args:
        body (PostUsersWalletsWithdrawConfirmBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUsersWalletsWithdrawConfirmResponse200]
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
    body: PostUsersWalletsWithdrawConfirmBody,
) -> Optional[PostUsersWalletsWithdrawConfirmResponse200]:
    """Confirm withdraw

     ## تایید درخواست برداشت

    برای تایید برداشت باید کد ارسال شده به شماره تلفن همراه یا ایمیل حساب کاربری خود را از طریق کد به
    صورت خودکار دریافت کنید و به این API ارسال نمایید.

    محدودیت فراخوانی: 30 درخواست در ساعت

    Args:
        body (PostUsersWalletsWithdrawConfirmBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUsersWalletsWithdrawConfirmResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersWalletsWithdrawConfirmBody,
) -> Response[PostUsersWalletsWithdrawConfirmResponse200]:
    """Confirm withdraw

     ## تایید درخواست برداشت

    برای تایید برداشت باید کد ارسال شده به شماره تلفن همراه یا ایمیل حساب کاربری خود را از طریق کد به
    صورت خودکار دریافت کنید و به این API ارسال نمایید.

    محدودیت فراخوانی: 30 درخواست در ساعت

    Args:
        body (PostUsersWalletsWithdrawConfirmBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUsersWalletsWithdrawConfirmResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersWalletsWithdrawConfirmBody,
) -> Optional[PostUsersWalletsWithdrawConfirmResponse200]:
    """Confirm withdraw

     ## تایید درخواست برداشت

    برای تایید برداشت باید کد ارسال شده به شماره تلفن همراه یا ایمیل حساب کاربری خود را از طریق کد به
    صورت خودکار دریافت کنید و به این API ارسال نمایید.

    محدودیت فراخوانی: 30 درخواست در ساعت

    Args:
        body (PostUsersWalletsWithdrawConfirmBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUsersWalletsWithdrawConfirmResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
