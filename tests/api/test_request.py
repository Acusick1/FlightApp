import pytest
from src.db import schemas


@pytest.mark.parametrize(
    "dep_iata, arr_iata",
    [
        ("AMS", "LHR"),
        ("LHR", "AMS")
    ]
)
def test_flight_request(dep_iata, arr_iata, client):

    get_response = client.get("/request/flight", params={"dep_iata": dep_iata, "arr_iata": arr_iata})
    assert get_response.status_code == 200

    data = get_response.json()
    result = schemas.Flight(**data[0])
    assert result.dep_iata == dep_iata.upper()
    assert result.arr_iata == arr_iata.upper()


def test_flight_request_no_filters(client):

    get_response = client.get("/request/flight")
    assert get_response.status_code == 400
    assert get_response.json() == {"detail": "No filters specified"}
