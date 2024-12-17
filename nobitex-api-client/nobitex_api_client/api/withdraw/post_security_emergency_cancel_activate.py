from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_security_emergency_cancel_activate_response_200 import (
    PostSecurityEmergencyCancelActivateResponse200,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/security/emergency-cancel/activate",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostSecurityEmergencyCancelActivateResponse200]:
    if response.status_code == 200:
        response_200 = PostSecurityEmergencyCancelActivateResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostSecurityEmergencyCancelActivateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PostSecurityEmergencyCancelActivateResponse200]:
    """Emergency cancel

     ## فعالسازی لغو اضطراری

    جهت فعالسازی امکان لغو اضطراریِ درخواست های برداشت از این درخواست استفاده نمائید.
    پس از فعالسازی این امکان، پیامک و ایمیل ارسالی پس از ثبت درخواست برداشت، حاوی لینکی خواهد بود که شما
    میتوانید با استفاده از آن در صورتی که درخواست برداشت توسط شما ثبت نشده است، در کمترین زمان ممکن و
    بدون نیاز به لاگین، درخواست های برداشت خود را لغو نمایید.

    **توجه:** در صورتی که درخواست برداشت شما توسط این امکان لغو
    گردد، امکان ثبت درخواست برداشت تا ۷۲ ساعت برای شما غیرفعال خواهد شد.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSecurityEmergencyCancelActivateResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PostSecurityEmergencyCancelActivateResponse200]:
    """Emergency cancel

     ## فعالسازی لغو اضطراری

    جهت فعالسازی امکان لغو اضطراریِ درخواست های برداشت از این درخواست استفاده نمائید.
    پس از فعالسازی این امکان، پیامک و ایمیل ارسالی پس از ثبت درخواست برداشت، حاوی لینکی خواهد بود که شما
    میتوانید با استفاده از آن در صورتی که درخواست برداشت توسط شما ثبت نشده است، در کمترین زمان ممکن و
    بدون نیاز به لاگین، درخواست های برداشت خود را لغو نمایید.

    **توجه:** در صورتی که درخواست برداشت شما توسط این امکان لغو
    گردد، امکان ثبت درخواست برداشت تا ۷۲ ساعت برای شما غیرفعال خواهد شد.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSecurityEmergencyCancelActivateResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PostSecurityEmergencyCancelActivateResponse200]:
    """Emergency cancel

     ## فعالسازی لغو اضطراری

    جهت فعالسازی امکان لغو اضطراریِ درخواست های برداشت از این درخواست استفاده نمائید.
    پس از فعالسازی این امکان، پیامک و ایمیل ارسالی پس از ثبت درخواست برداشت، حاوی لینکی خواهد بود که شما
    میتوانید با استفاده از آن در صورتی که درخواست برداشت توسط شما ثبت نشده است، در کمترین زمان ممکن و
    بدون نیاز به لاگین، درخواست های برداشت خود را لغو نمایید.

    **توجه:** در صورتی که درخواست برداشت شما توسط این امکان لغو
    گردد، امکان ثبت درخواست برداشت تا ۷۲ ساعت برای شما غیرفعال خواهد شد.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostSecurityEmergencyCancelActivateResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PostSecurityEmergencyCancelActivateResponse200]:
    """Emergency cancel

     ## فعالسازی لغو اضطراری

    جهت فعالسازی امکان لغو اضطراریِ درخواست های برداشت از این درخواست استفاده نمائید.
    پس از فعالسازی این امکان، پیامک و ایمیل ارسالی پس از ثبت درخواست برداشت، حاوی لینکی خواهد بود که شما
    میتوانید با استفاده از آن در صورتی که درخواست برداشت توسط شما ثبت نشده است، در کمترین زمان ممکن و
    بدون نیاز به لاگین، درخواست های برداشت خود را لغو نمایید.

    **توجه:** در صورتی که درخواست برداشت شما توسط این امکان لغو
    گردد، امکان ثبت درخواست برداشت تا ۷۲ ساعت برای شما غیرفعال خواهد شد.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostSecurityEmergencyCancelActivateResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
