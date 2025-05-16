from fastapi import APIRouter, Depends
from src.main.auth.middlewares import get_current_user


router = APIRouter(
    prefix="/health",
    tags=["health"],
)

@router.get("")
async def health(user_id: str = Depends(get_current_user)):
    return {"status": "ok", "user_id": user_id}

@router.get("/challeges/{userId}")
async def getChallenges(userId: str = Depends(get_current_user)):
    