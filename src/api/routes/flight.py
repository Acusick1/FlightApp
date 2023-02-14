import logging
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from src.db import schemas
from src.db.database import get_db
from config import settings

router = APIRouter(prefix="/flight", tags=["Flight"])


@router.get("/{idx}", status_code=status.HTTP_200_OK, response_model=schemas.FlightRead)
def get_flight_from_id(idx: int, db: Session = Depends(get_db)):

    flights = db.query(schemas.Flight).filter(schemas.Flight.id == idx).first()

    if flights is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Flight with id: {idx} not found")

    return flights