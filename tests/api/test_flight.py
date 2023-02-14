import pytest
from src.db import schemas


@pytest.mark.parametrize(
    "idx", [1, 2]
)
def test_flight(idx, client):

    get_response = client.get(f"/flight/{idx}")
    assert get_response.status_code == 200

    data = get_response.json()
    result = schemas.Flight(**data)
    assert result.id == idx


def test_flight_not_found(client):

    get_response = client.get(f"/flight/0")
    assert get_response.status_code == 404