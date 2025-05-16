from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.params import Query
from src.main.domain.database import get_db
from src.main.auth.middlewares import get_current_user
from src.main.domain.dto import MyChallengeDto
from src.main.service.MyChallengeService import MyChallengeService

router = APIRouter(
    prefix="/health",
    tags=["health"],
)

@router.get("")
async def health(user_id: str = Depends(get_current_user)):
    return {"status": "ok", "user_id": user_id}

@router.get("/myChallenges", response_model=MyChallengeDto)
async def getChallenges(userId: str = Depends(get_current_user),
                        challengeId: int = Query(...),
                        session: AsyncSession = Depends(get_db)):
    return await MyChallengeService.create_room(session, userId, challengeId)
