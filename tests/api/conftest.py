import pytest
from datetime import datetime
from fastapi.testclient import TestClient
from src.api.main import app
from src.db import schemas
from src.db.database import get_db
from config import settings


@pytest.fixture(scope="session")
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


# @pytest.fixture(scope="session")
# def get_request():
#     request = schemas.FlightRequest(
#         dep_port="GLA",
#         arr_port="LHR",
#     )

#     yield request