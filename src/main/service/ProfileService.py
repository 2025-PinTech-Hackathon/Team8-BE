from sqlalchemy.orm import Session
from src.main.repository.ProfileRepository import ProfileRepository
from src.main.domain.model.Member import Member
from src.main.domain.dto.ProfileRequestDto import ProfileRequestDto
from fastapi import HTTPException

class ProfileService:
    def __init__(self, db: Session):
        self.repository = ProfileRepository(db)

    def register_user_info(self, user_id: str, request: ProfileRequestDto) -> Member:
        if self.repository.find_by_id(user_id):
            raise HTTPException(status_code=409, detail="해당 이름으로 이미 등록된 정보가 존재합니다.")

        new_member = Member(
            memberId=user_id,
            name=request.name,
            gender=request.gender,
            age=request.age_range,
            job=request.job,
            interest=[interest.value for interest in request.interests],  # JSON 저장
            email=None  # 필요 시 수정
        )