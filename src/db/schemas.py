from datetime import datetime, time
from pydantic import validator, root_validator
from sqlalchemy import String
from sqlalchemy.sql.schema import Column
from sqlmodel import Field, SQLModel
from typing import Optional


class Flight(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    flight_iata: str = Field(sa_column=Column("flight_iata", String(10), unique=True))
    dep_iata: str
    arr_iata: str
    dep_time: time
    arr_time: time
    duration: Optional[int]


class FlightCreate(SQLModel):
    flight_iata: str
    dep_iata: str
    arr_iata: str
    dep_time: time
    arr_time: time
    duration: Optional[int]

    @validator("dep_iata", "arr_iata", "flight_iata")
    def iata_validator(cls, value: str):
        return value.upper()

    @validator("dep_time", "arr_time", pre=True)
    def time_validator(cls, value: str):
        if value is not None:
            return datetime.strptime(value, "%H:%M").time()


class FlightRead(SQLModel):
    id: Optional[int]
    flight_iata: str
    dep_iata: str
    arr_iata: str
    dep_time: time
    arr_time: time
    duration: Optional[int]


# TODO: Test
# class FlightBase(SQLModel):
#     flight_iata: str = Field(sa_column=Column("flight_iata", String(10), unique=True))
#     dep_iata: str
#     arr_iata: str
#     dep_time: time
#     arr_time: time
#     duration: Optional[int]


# class Flight(FlightBase, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)


# class FlightCreate(FlightBase):

#     @validator("dep_iata", "arr_iata", "flight_iata")
#     def iata_validator(cls, value: str):
#         return value.upper()

#     @validator("dep_time", "arr_time", pre=True)
#     def time_validator(cls, value: str):
#         return datetime.strptime(value, "%H:%M").time()


# class FlightRead(FlightBase):
#     id: int


# class Airport(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     iata_code: str = Field(index=True, nullable=False)
#     icao_code: str = Field(index=True, nullable=True)
#     name: str
#     country_code: str
#     lat: float
#     long: float

#     @root_validator(pre=True)
#     def root_validate(cls, values):
#         icao = values.get("icao_code")
#         iata = values.get("iata_code")

#         if not any((icao, iata)):
#             raise ValueError("At least one of icao_code or iata_code must be specified.")

#         return values