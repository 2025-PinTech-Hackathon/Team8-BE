from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.main.domain.database import get_db
from src.main.auth.middlewares import get_current_user
from src.main.service.ProfileService import ProfileService
from src.main.domain.dto.ProfileRequestDto import ProfileRequestDto
from src.main.domain.dto.ProfileResponseDto import ProfileResponseDto

ProfileAPIRouter = APIRouter(
    prefix="/profile",
    tags=["profile"]
)

@ProfileAPIRouter.post("/input", response_model=ProfileResponseDto)
async def input_profile(
    request: ProfileRequestDto,
    user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    
    print(f"[ROUTER] user_id: {user_id}")
    print(f"[ROUTER] request: {request.model_dump()}")

    try:
        service = ProfileService(db)
        result = service.register_user_info(user_id, request)
        return ProfileResponseDto(
            message="사용자 정보가 성공적으로 등록되었습니다.",
            user_id=result.memberId
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"[ERROR] /profile/input - {e}")
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생했습니다.")