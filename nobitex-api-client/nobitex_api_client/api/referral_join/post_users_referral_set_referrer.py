from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_users_referral_set_referrer_body import PostUsersReferralSetReferrerBody
from ...models.post_users_referral_set_referrer_response_200 import PostUsersReferralSetReferrerResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostUsersReferralSetReferrerBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/referral/set-referrer",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostUsersReferralSetReferrerResponse200]:
    if response.status_code == 200:
        response_200 = PostUsersReferralSetReferrerResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostUsersReferralSetReferrerResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersReferralSetReferrerBody,
) -> Response[PostUsersReferralSetReferrerResponse200]:
    """Set referrer

     ## ثبت معرف کاربر

    کد دعوت باید در زمان ثبت‌نام توسط کاربر وارد شده یا با استفاده از پیوند دعوت به صورت خودکار پر شود.
    با این حال تا ۲۴ ساعت پس از ثبت‌نام نیز امکان ثبت معرف توسط کاربر با استفاده از این API وجود دارد.

    Args:
        body (PostUsersReferralSetReferrerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUsersReferralSetReferrerResponse200]
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
    body: PostUsersReferralSetReferrerBody,
) -> Optional[PostUsersReferralSetReferrerResponse200]:
    """Set referrer

     ## ثبت معرف کاربر

    کد دعوت باید در زمان ثبت‌نام توسط کاربر وارد شده یا با استفاده از پیوند دعوت به صورت خودکار پر شود.
    با این حال تا ۲۴ ساعت پس از ثبت‌نام نیز امکان ثبت معرف توسط کاربر با استفاده از این API وجود دارد.

    Args:
        body (PostUsersReferralSetReferrerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUsersReferralSetReferrerResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersReferralSetReferrerBody,
) -> Response[PostUsersReferralSetReferrerResponse200]:
    """Set referrer

     ## ثبت معرف کاربر

    کد دعوت باید در زمان ثبت‌نام توسط کاربر وارد شده یا با استفاده از پیوند دعوت به صورت خودکار پر شود.
    با این حال تا ۲۴ ساعت پس از ثبت‌نام نیز امکان ثبت معرف توسط کاربر با استفاده از این API وجود دارد.

    Args:
        body (PostUsersReferralSetReferrerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUsersReferralSetReferrerResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersReferralSetReferrerBody,
) -> Optional[PostUsersReferralSetReferrerResponse200]:
    """Set referrer

     ## ثبت معرف کاربر

    کد دعوت باید در زمان ثبت‌نام توسط کاربر وارد شده یا با استفاده از پیوند دعوت به صورت خودکار پر شود.
    با این حال تا ۲۴ ساعت پس از ثبت‌نام نیز امکان ثبت معرف توسط کاربر با استفاده از این API وجود دارد.

    Args:
        body (PostUsersReferralSetReferrerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUsersReferralSetReferrerResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
