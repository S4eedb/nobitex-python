from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_auth_login_body import PostAuthLoginBody
from ...models.post_auth_login_response_200 import PostAuthLoginResponse200
from ...models.post_auth_login_response_400 import PostAuthLoginResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostAuthLoginBody,
    x_totp: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_totp, Unset):
        headers["X-TOTP"] = x_totp

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/login/",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[PostAuthLoginResponse200, PostAuthLoginResponse400]]:
    if response.status_code == 200:
        response_200 = PostAuthLoginResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = PostAuthLoginResponse400.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[PostAuthLoginResponse200, PostAuthLoginResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostAuthLoginBody,
    x_totp: Union[Unset, str] = UNSET,
) -> Response[Union[PostAuthLoginResponse200, PostAuthLoginResponse400]]:
    """Login

     ## دریافت توکن

    دریافت توکن به صورت خودکار و با ارسال درخواست به آدرس زیر صورت می‌گیرد. این تنها درخواستی است که
    نیاز دارید به آن نام کاربری و رمز عبور خود را ارسال کنید. تمامی دیگر درخواست از توکن به جای رمز عبور
    برای احراز هویت استفاده می‌کنند. توکن‌های صادر شده بعد از چهار ساعت (کوتاه مدت) یا سی روز (طولانی
    مدت) منقضی می‌شوند و باید مجددا با ارسال درخواست لاگین، توکن جدیدی دریافت کنید.

    در صورت نیاز به توکن‌های با تاریخ انقضای طولانی‌تر و آگاهی از ملاحظات امنیتی لازم، با پشتیبانی
    نوبیتکس تماس بگیرید.

    برای لاگین حتما باید از ایران درخواست ارسال کنید. بدیهی است که استفاده از هر پروکسی باعث برگشت خطا
    می‌شود.

    Args:
        x_totp (Union[Unset, str]):
        body (PostAuthLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostAuthLoginResponse200, PostAuthLoginResponse400]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_totp=x_totp,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostAuthLoginBody,
    x_totp: Union[Unset, str] = UNSET,
) -> Optional[Union[PostAuthLoginResponse200, PostAuthLoginResponse400]]:
    """Login

     ## دریافت توکن

    دریافت توکن به صورت خودکار و با ارسال درخواست به آدرس زیر صورت می‌گیرد. این تنها درخواستی است که
    نیاز دارید به آن نام کاربری و رمز عبور خود را ارسال کنید. تمامی دیگر درخواست از توکن به جای رمز عبور
    برای احراز هویت استفاده می‌کنند. توکن‌های صادر شده بعد از چهار ساعت (کوتاه مدت) یا سی روز (طولانی
    مدت) منقضی می‌شوند و باید مجددا با ارسال درخواست لاگین، توکن جدیدی دریافت کنید.

    در صورت نیاز به توکن‌های با تاریخ انقضای طولانی‌تر و آگاهی از ملاحظات امنیتی لازم، با پشتیبانی
    نوبیتکس تماس بگیرید.

    برای لاگین حتما باید از ایران درخواست ارسال کنید. بدیهی است که استفاده از هر پروکسی باعث برگشت خطا
    می‌شود.

    Args:
        x_totp (Union[Unset, str]):
        body (PostAuthLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostAuthLoginResponse200, PostAuthLoginResponse400]
    """

    return sync_detailed(
        client=client,
        body=body,
        x_totp=x_totp,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostAuthLoginBody,
    x_totp: Union[Unset, str] = UNSET,
) -> Response[Union[PostAuthLoginResponse200, PostAuthLoginResponse400]]:
    """Login

     ## دریافت توکن

    دریافت توکن به صورت خودکار و با ارسال درخواست به آدرس زیر صورت می‌گیرد. این تنها درخواستی است که
    نیاز دارید به آن نام کاربری و رمز عبور خود را ارسال کنید. تمامی دیگر درخواست از توکن به جای رمز عبور
    برای احراز هویت استفاده می‌کنند. توکن‌های صادر شده بعد از چهار ساعت (کوتاه مدت) یا سی روز (طولانی
    مدت) منقضی می‌شوند و باید مجددا با ارسال درخواست لاگین، توکن جدیدی دریافت کنید.

    در صورت نیاز به توکن‌های با تاریخ انقضای طولانی‌تر و آگاهی از ملاحظات امنیتی لازم، با پشتیبانی
    نوبیتکس تماس بگیرید.

    برای لاگین حتما باید از ایران درخواست ارسال کنید. بدیهی است که استفاده از هر پروکسی باعث برگشت خطا
    می‌شود.

    Args:
        x_totp (Union[Unset, str]):
        body (PostAuthLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostAuthLoginResponse200, PostAuthLoginResponse400]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_totp=x_totp,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostAuthLoginBody,
    x_totp: Union[Unset, str] = UNSET,
) -> Optional[Union[PostAuthLoginResponse200, PostAuthLoginResponse400]]:
    """Login

     ## دریافت توکن

    دریافت توکن به صورت خودکار و با ارسال درخواست به آدرس زیر صورت می‌گیرد. این تنها درخواستی است که
    نیاز دارید به آن نام کاربری و رمز عبور خود را ارسال کنید. تمامی دیگر درخواست از توکن به جای رمز عبور
    برای احراز هویت استفاده می‌کنند. توکن‌های صادر شده بعد از چهار ساعت (کوتاه مدت) یا سی روز (طولانی
    مدت) منقضی می‌شوند و باید مجددا با ارسال درخواست لاگین، توکن جدیدی دریافت کنید.

    در صورت نیاز به توکن‌های با تاریخ انقضای طولانی‌تر و آگاهی از ملاحظات امنیتی لازم، با پشتیبانی
    نوبیتکس تماس بگیرید.

    برای لاگین حتما باید از ایران درخواست ارسال کنید. بدیهی است که استفاده از هر پروکسی باعث برگشت خطا
    می‌شود.

    Args:
        x_totp (Union[Unset, str]):
        body (PostAuthLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostAuthLoginResponse200, PostAuthLoginResponse400]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_totp=x_totp,
        )
    ).parsed
