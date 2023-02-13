from fastapi import APIRouter, Depends, HTTPException, status
from typing import Optional
from sqlalchemy.orm import Session
from src.db import schemas
from src.db.database import get_db
from config import settings

router = APIRouter(prefix="/request", tags=["Request"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[schemas.FlightRead])
def get_flight(
    dep_iata: Optional[str] = None, 
    arr_iata: Optional[str] = None, 
    flight_iata: Optional[str] = None,
    duration: Optional[int] = None,
    skip: Optional[int] = 0, 
    db: Session = Depends(get_db)):

    filters = []
    if dep_iata:
        filters.append(schemas.Flight.dep_iata == dep_iata)

    if arr_iata:
        filters.append(schemas.Flight.arr_iata == arr_iata)

    if duration:
        filters.append(schemas.Flight.duration <= duration)

    if flight_iata:
        filters.append(schemas.Flight.flight_iata == flight_iata)

    if not filters:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No filters specified")

    flights = db.query(schemas.Flight).filter(*filters).order_by(schemas.Flight.id).limit(settings.return_limit).offset(skip).all()
    return flights