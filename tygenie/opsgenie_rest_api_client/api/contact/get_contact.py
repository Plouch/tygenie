from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_contact_response import GetContactResponse
from ...types import Response


def _get_kwargs(
    identifier: str,
    contact_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/users/{identifier}/contacts/{contact_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetContactResponse]]:
    if response.status_code == 200:
        response_200 = GetContactResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 402:
        response_402 = cast(Any, None)
        return response_402
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422
    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetContactResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identifier: str,
    contact_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetContactResponse]]:
    """Get Contact

     Returns contact with given id

    Args:
        identifier (str):
        contact_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetContactResponse]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        contact_id=contact_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    contact_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetContactResponse]]:
    """Get Contact

     Returns contact with given id

    Args:
        identifier (str):
        contact_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetContactResponse]
    """

    return sync_detailed(
        identifier=identifier,
        contact_id=contact_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    contact_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetContactResponse]]:
    """Get Contact

     Returns contact with given id

    Args:
        identifier (str):
        contact_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetContactResponse]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        contact_id=contact_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    contact_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetContactResponse]]:
    """Get Contact

     Returns contact with given id

    Args:
        identifier (str):
        contact_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetContactResponse]
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            contact_id=contact_id,
            client=client,
        )
    ).parsed
