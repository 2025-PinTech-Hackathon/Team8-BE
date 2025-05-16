from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.main.domain.model.Member import Member
from src.main.domain.dto.ProfileInputDto import ProfileInputDto
from src.main.repository.MemberRepository import MemberRepository
import uuid
from src.main.domain.dto.ProfileOutputDto import ProfileOutputDto
from src.main.domain.model.MemberEnum import AgeGroupEnum, JobEnum, InterestEnum

class ProfileService:
    def __init__(self, db: Session):
        self.member_repository = MemberRepository(db)
        self.db = db

    def create_profile(self, profile: ProfileInputDto, memberId: str) -> dict:
        try:
            # 이름 중복 체크
            existing_member = self.member_repository.find_by_id(memberId)
            if existing_member:
                raise HTTPException(
                    status_code=409,
                    detail="해당 이름으로 이미 등록된 정보가 존재합니다."
                )

            # Enum 값 검증 및 변환 (한글 입력값 -> 영문 코드)
            age_enum = profile.validate_age_range()  # 예: "20대" -> AGE_20s
            job_enum = profile.validate_job()  # 예: "대학생" -> UNIVERSITY
            validated_interests = profile.validate_interests()  # 예: ["장학금"] -> ["SCHOLARSHIP"]

            # 새 멤버 생성
            new_member = Member(
                memberId=memberId,  # 이미 생성된 memberId 사용
                name=profile.name,
                gender=profile.gender,
                age=age_enum,
                job=job_enum,
                interest=validated_interests
            )

            # DB에 저장
            saved_member = self.member_repository.save(new_member)

            return {
                "message": "사용자 정보가 성공적으로 등록되었습니다.",
                "user_id": saved_member.memberId
            }

        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail="서버 오류가 발생했습니다. 잠시 후 다시 시도해주세요."
            )

    def get_profile(self, member_id: str) -> ProfileOutputDto:
        try:
            member = self.db.query(Member).filter(Member.memberId == member_id).first()
            
            if not member:
                raise HTTPException(
                    status_code=404,
                    detail="사용자 정보를 찾을 수 없습니다."
                )
            
            # interests를 한글로 변환
            korean_interests = [InterestEnum.to_korean(interest) for interest in member.interest]
            
            return ProfileOutputDto(
                name=member.name,
                gender="여자" if member.gender else "남자",
                age_range=AgeGroupEnum.to_korean(member.age),
                job=JobEnum.to_korean(member.job),
                interests=korean_interests
            )
            
        except HTTPException as he:
            raise he
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail="서버 오류가 발생했습니다. 잠시 후 다시 시도해주세요."
            ) 