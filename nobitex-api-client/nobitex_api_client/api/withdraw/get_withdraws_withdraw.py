from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_withdraws_withdraw_response_200 import GetWithdrawsWithdrawResponse200
from ...models.get_withdraws_withdraw_response_404 import GetWithdrawsWithdrawResponse404
from ...types import Response


def _get_kwargs(
    withdraw: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/withdraws/{withdraw}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetWithdrawsWithdrawResponse200, GetWithdrawsWithdrawResponse404]]:
    if response.status_code == 200:
        response_200 = GetWithdrawsWithdrawResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = GetWithdrawsWithdrawResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetWithdrawsWithdrawResponse200, GetWithdrawsWithdrawResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    withdraw: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[GetWithdrawsWithdrawResponse200, GetWithdrawsWithdrawResponse404]]:
    """Withdraw status

     ## مشاهده برداشت

    برای مشاهده وضعیت یک درخواست برداشت از این نوع درخواست استفاده نمایید.

    محدودیت فراخوانی: ۶۰ درخواست در ۲ دقیقه

    Args:
        withdraw (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetWithdrawsWithdrawResponse200, GetWithdrawsWithdrawResponse404]]
    """

    kwargs = _get_kwargs(
        withdraw=withdraw,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    withdraw: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[GetWithdrawsWithdrawResponse200, GetWithdrawsWithdrawResponse404]]:
    """Withdraw status

     ## مشاهده برداشت

    برای مشاهده وضعیت یک درخواست برداشت از این نوع درخواست استفاده نمایید.

    محدودیت فراخوانی: ۶۰ درخواست در ۲ دقیقه

    Args:
        withdraw (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetWithdrawsWithdrawResponse200, GetWithdrawsWithdrawResponse404]
    """

    return sync_detailed(
        withdraw=withdraw,
        client=client,
    ).parsed


async def asyncio_detailed(
    withdraw: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[GetWithdrawsWithdrawResponse200, GetWithdrawsWithdrawResponse404]]:
    """Withdraw status

     ## مشاهده برداشت

    برای مشاهده وضعیت یک درخواست برداشت از این نوع درخواست استفاده نمایید.

    محدودیت فراخوانی: ۶۰ درخواست در ۲ دقیقه

    Args:
        withdraw (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetWithdrawsWithdrawResponse200, GetWithdrawsWithdrawResponse404]]
    """

    kwargs = _get_kwargs(
        withdraw=withdraw,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    withdraw: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[GetWithdrawsWithdrawResponse200, GetWithdrawsWithdrawResponse404]]:
    """Withdraw status

     ## مشاهده برداشت

    برای مشاهده وضعیت یک درخواست برداشت از این نوع درخواست استفاده نمایید.

    محدودیت فراخوانی: ۶۰ درخواست در ۲ دقیقه

    Args:
        withdraw (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetWithdrawsWithdrawResponse200, GetWithdrawsWithdrawResponse404]
    """

    return (
        await asyncio_detailed(
            withdraw=withdraw,
            client=client,
        )
    ).parsed