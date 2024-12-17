from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_users_cards_add_body import PostUsersCardsAddBody
from ...models.post_users_cards_add_response_200 import PostUsersCardsAddResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostUsersCardsAddBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/cards-add",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostUsersCardsAddResponse200]:
    if response.status_code == 200:
        response_200 = PostUsersCardsAddResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostUsersCardsAddResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersCardsAddBody,
) -> Response[PostUsersCardsAddResponse200]:
    """Cards add

     ## افزودن کارت بانکی

    برای افزودن کارت بانکی جدید از این نوع درخواست استفاده نمایید:

    قبل از درج کارت باید نام، نام خانوادگی، کدملی و شماره همراه خود را در پروفایل نوبیتکس تکمیل کرده
    باشید.

    محدودیت فراخوانی : ۳۰ درخواست در ۳۰ دقیقه

    Args:
        body (PostUsersCardsAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUsersCardsAddResponse200]
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
    body: PostUsersCardsAddBody,
) -> Optional[PostUsersCardsAddResponse200]:
    """Cards add

     ## افزودن کارت بانکی

    برای افزودن کارت بانکی جدید از این نوع درخواست استفاده نمایید:

    قبل از درج کارت باید نام، نام خانوادگی، کدملی و شماره همراه خود را در پروفایل نوبیتکس تکمیل کرده
    باشید.

    محدودیت فراخوانی : ۳۰ درخواست در ۳۰ دقیقه

    Args:
        body (PostUsersCardsAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUsersCardsAddResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersCardsAddBody,
) -> Response[PostUsersCardsAddResponse200]:
    """Cards add

     ## افزودن کارت بانکی

    برای افزودن کارت بانکی جدید از این نوع درخواست استفاده نمایید:

    قبل از درج کارت باید نام، نام خانوادگی، کدملی و شماره همراه خود را در پروفایل نوبیتکس تکمیل کرده
    باشید.

    محدودیت فراخوانی : ۳۰ درخواست در ۳۰ دقیقه

    Args:
        body (PostUsersCardsAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUsersCardsAddResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersCardsAddBody,
) -> Optional[PostUsersCardsAddResponse200]:
    """Cards add

     ## افزودن کارت بانکی

    برای افزودن کارت بانکی جدید از این نوع درخواست استفاده نمایید:

    قبل از درج کارت باید نام، نام خانوادگی، کدملی و شماره همراه خود را در پروفایل نوبیتکس تکمیل کرده
    باشید.

    محدودیت فراخوانی : ۳۰ درخواست در ۳۰ دقیقه

    Args:
        body (PostUsersCardsAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUsersCardsAddResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
