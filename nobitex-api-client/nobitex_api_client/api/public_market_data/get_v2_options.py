from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v2_options_response_200 import GetV2OptionsResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/options",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetV2OptionsResponse200]:
    if response.status_code == 200:
        response_200 = GetV2OptionsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetV2OptionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetV2OptionsResponse200]:
    """Market options

     ## تنظیمات سیستم

    مواردی مانند رمزارزهای فعال، حداقل معامله در هر بازار، پله‌های کارمزد، سقف برداشت و بسیاری اطلاعات
    مفید دیگر از این طریق در دسترس شما قرار خواهد داشت.

    محدودیت فراخوانی: ۱ درخواست در دقیقه با امکان burst

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV2OptionsResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetV2OptionsResponse200]:
    """Market options

     ## تنظیمات سیستم

    مواردی مانند رمزارزهای فعال، حداقل معامله در هر بازار، پله‌های کارمزد، سقف برداشت و بسیاری اطلاعات
    مفید دیگر از این طریق در دسترس شما قرار خواهد داشت.

    محدودیت فراخوانی: ۱ درخواست در دقیقه با امکان burst

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV2OptionsResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetV2OptionsResponse200]:
    """Market options

     ## تنظیمات سیستم

    مواردی مانند رمزارزهای فعال، حداقل معامله در هر بازار، پله‌های کارمزد، سقف برداشت و بسیاری اطلاعات
    مفید دیگر از این طریق در دسترس شما قرار خواهد داشت.

    محدودیت فراخوانی: ۱ درخواست در دقیقه با امکان burst

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV2OptionsResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetV2OptionsResponse200]:
    """Market options

     ## تنظیمات سیستم

    مواردی مانند رمزارزهای فعال، حداقل معامله در هر بازار، پله‌های کارمزد، سقف برداشت و بسیاری اطلاعات
    مفید دیگر از این طریق در دسترس شما قرار خواهد داشت.

    محدودیت فراخوانی: ۱ درخواست در دقیقه با امکان burst

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV2OptionsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
