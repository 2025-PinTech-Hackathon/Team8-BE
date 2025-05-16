from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.params import Query
from src.main.domain.database import get_db
from src.main.auth.middlewares import get_current_user
from src.main.service._MyChallengeService import MyChallengeService
from src.main.domain.dto.MyChallengeDto import MyChallengeReqDto
from src.main.domain.dto.MyChallengeDto import MyChallengeRoomResDto, InviteCodeResponseDto

router = APIRouter(
)

@router.post("/myChallenges/{challengeId}", response_model=MyChallengeReqDto)
async def getChallenges(challengeId: int, userId: str = Depends(get_current_user),
                        session: AsyncSession = Depends(get_db)):
    return MyChallengeService.create_room(session, userId, challengeId)

@router.get("/myChallenges/{roomId}", response_model=MyChallengeRoomResDto)
async def getChallengeDetail(roomId: int, userId: str = Depends(get_current_user),
                            session: AsyncSession = Depends(get_db)):
    return MyChallengeService.getChallengeDetail(session, userId, roomId)

@router.get("/myChallenges/{roomId}/invite", response_model=InviteCodeResponseDto)
async def get_invite_code(roomId: int, userId: str = Depends(get_current_user),
                          session: AsyncSession = Depends(get_db)):
    return MyChallengeService.get_invite_code(session, roomId)