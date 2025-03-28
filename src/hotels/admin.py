from sqladmin import ModelView
from .models import Hotel

class HotelAdmin(ModelView, model=Hotel):
    column_list = [Hotel.id, Hotel.name, Hotel.location, Hotel.description, Hotel.owner_id]