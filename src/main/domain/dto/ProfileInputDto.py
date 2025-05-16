from fastapi import HTTPException
from pydantic import BaseModel, conlist
from src.main.domain.model.MemberEnum import AgeGroupEnum, JobEnum, InterestEnum
from typing import List

class ProfileInputDto(BaseModel):
    name: str
    gender: bool  # true: 여자, false: 남자
    age_range: str  # 한글로 입력 (예: "20대")
    job: str  # 한글로 입력 (예: "대학생")
    interests: List[str]  # 한글로 입력 (예: ["장학금", "주거지원"])

    def validate_age_range(self) -> AgeGroupEnum:
        """한글 나이대를 AgeGroupEnum으로 변환"""
        try:
            return next(age for age in AgeGroupEnum if AgeGroupEnum.to_korean(age) == self.age_range)
        except StopIteration:
            raise HTTPException(
                status_code=400,
                detail="유효하지 않은 나이대입니다. 가능한 값: " + ", ".join([AgeGroupEnum.to_korean(age) for age in AgeGroupEnum])
            )
    
    def validate_job(self) -> JobEnum:
        """한글 직업명을 JobEnum으로 변환"""
        try:
            return next(job for job in JobEnum if JobEnum.to_korean(job) == self.job)
        except StopIteration:
            raise HTTPException(
                status_code=400,
                detail="유효하지 않은 직업입니다. 가능한 값: " + ", ".join([JobEnum.to_korean(job) for job in JobEnum])
            )
    
    def validate_interests(self) -> List[str]:
        """한글 관심사를 영문 코드로 변환"""
        try:
            # 입력된 한글 관심사를 영문 코드로 변환
            return [next(interest.name for interest in InterestEnum if interest.value == interest_kr) 
                   for interest_kr in self.interests]
        except StopIteration:
            valid_interests = [interest.value for interest in InterestEnum]
            raise HTTPException(
                status_code=400,
                detail=f"유효하지 않은 관심사입니다. 가능한 값: {', '.join(valid_interests)}"
            )