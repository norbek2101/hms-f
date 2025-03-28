from fastapi import APIRouter, Depends
from src.auth.dependency import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/profile")
def get_profile(user: dict = Depends(get_current_user)):
    return {"email": user["sub"]}
