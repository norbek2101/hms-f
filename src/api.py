from fastapi import APIRouter
from src.auth.controller import router as auth_router
from src.users.controller import router as users_router
from src.hotels.controller import router as hotels_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(users_router)
router.include_router(hotels_router)
