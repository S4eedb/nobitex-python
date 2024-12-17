from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_auth_logout_response_200 import PostAuthLogoutResponse200
from ...models.post_auth_logout_response_401 import PostAuthLogoutResponse401
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/logout/",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[PostAuthLogoutResponse200, PostAuthLogoutResponse401]]:
    if response.status_code == 200:
        response_200 = PostAuthLogoutResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = PostAuthLogoutResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[PostAuthLogoutResponse200, PostAuthLogoutResponse401]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[PostAuthLogoutResponse200, PostAuthLogoutResponse401]]:
    """Logout

     ## سوزاندن توکن

    برای خروج یا سوزاندن توکن، از این درخواست استفاده کنید:

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostAuthLogoutResponse200, PostAuthLogoutResponse401]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[PostAuthLogoutResponse200, PostAuthLogoutResponse401]]:
    """Logout

     ## سوزاندن توکن

    برای خروج یا سوزاندن توکن، از این درخواست استفاده کنید:

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostAuthLogoutResponse200, PostAuthLogoutResponse401]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[PostAuthLogoutResponse200, PostAuthLogoutResponse401]]:
    """Logout

     ## سوزاندن توکن

    برای خروج یا سوزاندن توکن، از این درخواست استفاده کنید:

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostAuthLogoutResponse200, PostAuthLogoutResponse401]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[PostAuthLogoutResponse200, PostAuthLogoutResponse401]]:
    """Logout

     ## سوزاندن توکن

    برای خروج یا سوزاندن توکن، از این درخواست استفاده کنید:

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostAuthLogoutResponse200, PostAuthLogoutResponse401]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed