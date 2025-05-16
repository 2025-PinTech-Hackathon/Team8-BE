from fastapi import APIRouter, Depends, Query, HTTPException
from src.main.service.MainService import MainService
from src.main.domain.dto.InformationResponseDto import UserInformationResponse
from typing import Optional
from src.main.auth.middlewares import get_current_user
from sqlalchemy.orm import Session
from src.main.domain.database import get_db
import traceback

MainAPIRouter = APIRouter(
    prefix="/main",
    tags=["main"]
)

# 맞춤형 정보 메인 페이지
@MainAPIRouter.get("/information", response_model=UserInformationResponse)
async def get_user_information(
    tag: str = Query(..., description="카테고리"),
    member_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        print(f" /main/information 진입 - tag: {tag}, member_id: {member_id}")
        service = MainService(db)
        result = service.get_information_by_tag(member_id, tag)
        if result is None:
            raise HTTPException(status_code=404, detail="해당 사용자 또는 카테고리에 대한 정보가 없습니다.")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail="서버 내부 오류가 발생했습니다.")