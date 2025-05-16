from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.main.domain.database import get_db
from fastapi.params import Query
from src.main.auth.middlewares import get_current_user

from src.main.domain.dto._MyChallengeListDto import MyChallengeListResDto
from src.main.service._MyChallengeListService import MyChallengeListService

from src. main.domain.model.ChallengeStatusEnum import ChallengeStatusEnum
from src.main.domain.model.MemberEnum import InterestEnum

router = APIRouter(
)

@router.get("/myChallenges", response_model=MyChallengeListResDto)
async def getChallenges(userId: str = Depends(get_current_user),
                        tag: Optional[InterestEnum] = Query(None),
                        status: ChallengeStatusEnum= Query(...),
                        session: AsyncSession = Depends(get_db)):
    return MyChallengeListService.get_my_challenge_List(session, userId, tag, status)
