from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.sequence_response import SequenceResponse
from ...models.sequence_update import SequenceUpdate
from ...types import Response


def _get_kwargs(
    field_id: int,
    *,
    json_body: SequenceUpdate,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": "/automations/sequence/{_id}".format(
            _id=field_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, SequenceResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SequenceResponse.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, SequenceResponse]]:
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
    json_body: SequenceUpdate,
) -> Response[Union[HTTPValidationError, SequenceResponse]]:
    """Update Sequence

    Args:
        field_id (int):
        json_body (SequenceUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, SequenceResponse]]
    """

    kwargs = _get_kwargs(
        field_id=field_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    field_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: SequenceUpdate,
) -> Optional[Union[HTTPValidationError, SequenceResponse]]:
    """Update Sequence

    Args:
        field_id (int):
        json_body (SequenceUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, SequenceResponse]
    """

    return sync_detailed(
        field_id=field_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    field_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: SequenceUpdate,
) -> Response[Union[HTTPValidationError, SequenceResponse]]:
    """Update Sequence

    Args:
        field_id (int):
        json_body (SequenceUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, SequenceResponse]]
    """

    kwargs = _get_kwargs(
        field_id=field_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    field_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: SequenceUpdate,
) -> Optional[Union[HTTPValidationError, SequenceResponse]]:
    """Update Sequence

    Args:
        field_id (int):
        json_body (SequenceUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, SequenceResponse]
    """

    return (
        await asyncio_detailed(
            field_id=field_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
