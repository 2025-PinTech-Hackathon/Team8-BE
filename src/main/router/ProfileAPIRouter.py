from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.main.auth.middlewares import get_current_user
from src.main.domain.database import get_db
from src.main.domain.dto.ProfileInputDto import ProfileInputDto
from src.main.service.ProfileService import ProfileService

ProfileAPIRouter = APIRouter(
    prefix="/profile",
    tags=["profile"]
)

@ProfileAPIRouter.post("/input")
async def create_profile(
    profile: ProfileInputDto,
    memberId: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    profile_service = ProfileService(db)
    return profile_service.create_profile(profile, memberId)