from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.params import Query
from src.main.domain.database import get_db
from src.main.auth.middlewares import get_current_user
from src.main.service.MyChallengeService import MyChallengeService
from src.main.domain.dto.MyChallengeDto import MyChallengeReqDto

router = APIRouter(
)

@router.post("/myChallenges/{challengeId}", response_model=MyChallengeReqDto)
async def getChallenges(challengeId: int, userId: str = Depends(get_current_user),
                        session: AsyncSession = Depends(get_db)):
    return MyChallengeService.create_room(session, userId, challengeId)
