import pytest
from fastapi.testclient import TestClient
from src.api.main import app
from src.db.database import get_db


@pytest.fixture(scope="session")
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
