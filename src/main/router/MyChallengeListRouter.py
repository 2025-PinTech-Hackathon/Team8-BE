from typing import Optional
from fastapi import APIRouter, Depends
from fastapi.params import Query
from src.main.auth.middlewares import get_current_user
from domain.dto import MyChallengeListResDto
from ..service.MyChallengeListService import MyChallengeListService

router = APIRouter(
    prefix="/health",
    tags=["health"],
)

@router.get("")
async def health(user_id: str = Depends(get_current_user)):
    return {"status": "ok", "user_id": user_id}

@router.get("/myChallenges", response_model=MyChallengeListResDto)
async def getChallenges(userId: str = Depends(get_current_user),
                        tag: Optional[str] = Query(None),
                        status: str= Query(...)):
    return await MyChallengeListService.get_my_challenges(userId, tag, status)
