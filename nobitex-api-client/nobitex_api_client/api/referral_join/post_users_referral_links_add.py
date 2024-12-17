from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_users_referral_links_add_body import PostUsersReferralLinksAddBody
from ...models.post_users_referral_links_add_response_200 import PostUsersReferralLinksAddResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostUsersReferralLinksAddBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/referral/links-add",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostUsersReferralLinksAddResponse200]:
    if response.status_code == 200:
        response_200 = PostUsersReferralLinksAddResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostUsersReferralLinksAddResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersReferralLinksAddBody,
) -> Response[PostUsersReferralLinksAddResponse200]:
    """Add Referral code

     ## ایجاد کد معرف

    هر کاربر نوبیتکس می‌تواند برای خود یک یا چند کد دعوت (نهایتا ۳۰) بسازد که در هر یک سهم کاربر معرف و
    کاربر دعوت شده از کارمزد اهدایی می‌تواند متفاوت باشد. با ارسال کد دعوت در قالب پیوند زیر به تعداد
    دلخواه از دوستان و پیوستن آن‌ها با این لینک به نوبیتکس معرف آن‌ها شناخته خواهید شد:

    `https://nobitex.ir/signup/?refcode=CODE`

    محدودیت فراخوانی: ۵ درخواست در هر دقیقه

    Args:
        body (PostUsersReferralLinksAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUsersReferralLinksAddResponse200]
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
    body: PostUsersReferralLinksAddBody,
) -> Optional[PostUsersReferralLinksAddResponse200]:
    """Add Referral code

     ## ایجاد کد معرف

    هر کاربر نوبیتکس می‌تواند برای خود یک یا چند کد دعوت (نهایتا ۳۰) بسازد که در هر یک سهم کاربر معرف و
    کاربر دعوت شده از کارمزد اهدایی می‌تواند متفاوت باشد. با ارسال کد دعوت در قالب پیوند زیر به تعداد
    دلخواه از دوستان و پیوستن آن‌ها با این لینک به نوبیتکس معرف آن‌ها شناخته خواهید شد:

    `https://nobitex.ir/signup/?refcode=CODE`

    محدودیت فراخوانی: ۵ درخواست در هر دقیقه

    Args:
        body (PostUsersReferralLinksAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUsersReferralLinksAddResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersReferralLinksAddBody,
) -> Response[PostUsersReferralLinksAddResponse200]:
    """Add Referral code

     ## ایجاد کد معرف

    هر کاربر نوبیتکس می‌تواند برای خود یک یا چند کد دعوت (نهایتا ۳۰) بسازد که در هر یک سهم کاربر معرف و
    کاربر دعوت شده از کارمزد اهدایی می‌تواند متفاوت باشد. با ارسال کد دعوت در قالب پیوند زیر به تعداد
    دلخواه از دوستان و پیوستن آن‌ها با این لینک به نوبیتکس معرف آن‌ها شناخته خواهید شد:

    `https://nobitex.ir/signup/?refcode=CODE`

    محدودیت فراخوانی: ۵ درخواست در هر دقیقه

    Args:
        body (PostUsersReferralLinksAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostUsersReferralLinksAddResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostUsersReferralLinksAddBody,
) -> Optional[PostUsersReferralLinksAddResponse200]:
    """Add Referral code

     ## ایجاد کد معرف

    هر کاربر نوبیتکس می‌تواند برای خود یک یا چند کد دعوت (نهایتا ۳۰) بسازد که در هر یک سهم کاربر معرف و
    کاربر دعوت شده از کارمزد اهدایی می‌تواند متفاوت باشد. با ارسال کد دعوت در قالب پیوند زیر به تعداد
    دلخواه از دوستان و پیوستن آن‌ها با این لینک به نوبیتکس معرف آن‌ها شناخته خواهید شد:

    `https://nobitex.ir/signup/?refcode=CODE`

    محدودیت فراخوانی: ۵ درخواست در هر دقیقه

    Args:
        body (PostUsersReferralLinksAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostUsersReferralLinksAddResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
