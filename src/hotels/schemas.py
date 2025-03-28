from pydantic import BaseModel
from typing import Optional

class HotelBase(BaseModel):
    name: str
    location: str
    description: Optional[str] = None

class HotelCreate(HotelBase):
    pass

class HotelResponse(HotelBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
