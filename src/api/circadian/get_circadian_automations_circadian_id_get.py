from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.circadian_response import CircadianResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    field_id: int,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/automations/circadian/{_id}".format(
            _id=field_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CircadianResponse, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CircadianResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CircadianResponse, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    field_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[CircadianResponse, HTTPValidationError]]:
    """Get Circadian

    Args:
        field_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CircadianResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        field_id=field_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    field_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[CircadianResponse, HTTPValidationError]]:
    """Get Circadian

    Args:
        field_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CircadianResponse, HTTPValidationError]
    """

    return sync_detailed(
        field_id=field_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    field_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[CircadianResponse, HTTPValidationError]]:
    """Get Circadian

    Args:
        field_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CircadianResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        field_id=field_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    field_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[CircadianResponse, HTTPValidationError]]:
    """Get Circadian

    Args:
        field_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CircadianResponse, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            field_id=field_id,
            client=client,
        )
    ).parsed
