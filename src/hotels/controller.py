from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from . import service, schemas
from src.auth.jwt import verify_token  # Ensure authentication

router = APIRouter(prefix="/hotels", tags=["Hotels"])

@router.post("/", response_model=schemas.HotelResponse)
def create_hotel(hotel: schemas.HotelCreate, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return service.create_hotel(db, hotel, owner_id=token["sub"])  # Assuming "sub" contains user ID

@router.get("/", response_model=list[schemas.HotelResponse])
def get_hotels(db: Session = Depends(get_db)):
    return service.get_hotels(db)

@router.get("/{hotel_id}", response_model=schemas.HotelResponse)
def get_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = service.get_hotel_by_id(db, hotel_id)
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return hotel

@router.delete("/{hotel_id}")
def delete_hotel(hotel_id: int, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    deleted_hotel = service.delete_hotel(db, hotel_id)
    if not deleted_hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return {"message": "Hotel deleted successfully"}
