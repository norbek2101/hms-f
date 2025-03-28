from sqlalchemy.orm import Session
from . import models, schemas

def create_hotel(db: Session, hotel: schemas.HotelCreate, owner_id: int):
    db_hotel = models.Hotel(**hotel.model_dump(), owner_id=owner_id)
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel

def get_hotels(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Hotel).offset(skip).limit(limit).all()

def get_hotel_by_id(db: Session, hotel_id: int):
    return db.query(models.Hotel).filter(models.Hotel.id == hotel_id).first()

def delete_hotel(db: Session, hotel_id: int):
    db_hotel = db.query(models.Hotel).filter(models.Hotel.id == hotel_id).first()
    if db_hotel:
        db.delete(db_hotel)
        db.commit()
    return db_hotel
