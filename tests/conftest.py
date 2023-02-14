import pytest
from sqlalchemy.orm import Session
from sqlmodel import SQLModel
from src.db import schemas
from src.db.database import engine
from config import settings


@pytest.fixture(scope="session")
def mock_data():
    return [
        schemas.FlightCreate(flight_iata="AB123", dep_iata="LHR", arr_iata="AMS", dep_time="10:00", arr_time="11:00", duration=60),
        schemas.FlightCreate(flight_iata="AB124", dep_iata="AMS", arr_iata="LHR", dep_time="11:15", arr_time="12:15", duration=60),
    ]

@pytest.fixture(scope="session")
def tables():
    if settings.db_name.endswith("test"):
        SQLModel.metadata.drop_all(engine)
        SQLModel.metadata.create_all(engine)
    else:
        raise Exception("Testing database name must end with 'test', ensure environment variables are properly set in pytest.ini file")
    
    yield


@pytest.fixture(scope="session")
def session(tables, mock_data):

    session = Session(engine)

    for entry in mock_data:
        session.add(schemas.Flight.from_orm(entry))
        session.commit()

    yield session
    session.close()
