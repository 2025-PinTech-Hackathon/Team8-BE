from fastapi import APIRouter, Depends, Query, HTTPException
from src.main.service.MainService import MainService
from src.main.domain.dto.ChallengeResponseDto import UserChallengeResponse
from src.main.domain.dto.InformationResponseDto import UserInformationResponse
from typing import Optional
from src.main.auth.middlewares import get_current_user
from sqlalchemy.orm import Session
from src.main.domain.database import get_db
import traceback
from typing import Optional
from src.main.domain.model.MemberEnum import InterestEnum

MainAPIRouter = APIRouter(
    prefix="/main",
    tags=["main"]
)

@MainAPIRouter.get("/information", response_model=UserInformationResponse)
async def get_user_information(
    tag: Optional[str] = Query(None, description="카테고리 (ex. SCHOLOARSHIP)"),
    member_id: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        service = MainService(db)

        if tag is not None and tag.strip().lower() != "null":
            result = service.get_information_by_specific_tag(member_id, tag)
        else:
            result = service.get_information_by_tag(member_id, tag)

        if result is None:
            raise HTTPException(status_code=404, detail="해당 사용자 또는 카테고리에 대한 정보가 없습니다.")
        return result

    except Exception:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생했습니다.")

    
# 맞춤형 챌린지 메인 페이지
@MainAPIRouter.get("/challenge", response_model=UserChallengeResponse)
async def get_user_challenge(
    tag: Optional[str] = Query(None, description="카테고리"),
    member_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        service = MainService(db)

        if tag is not None and tag.strip().lower() != "null":
            result = service.get_challenge_by_specific_tag(member_id, tag)
        else:
            result = service.get_challenge_by_all_tags(member_id)

        if result is None:
            raise HTTPException(status_code=404, detail="해당 사용자 또는 카테고리에 대한 정보가 없습니다.")
        return result

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생했습니다.")
    
# 태그 목록 조회
@MainAPIRouter.get("/tags")
async def get_tags(
    member_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        service = MainService(db)
        result = service.get_tags()
        print(f"[DEBUG] result: {result}")
        return {
            "tags": result
        }
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생했습니다.")

