from fastapi import HTTPException
from pydantic import BaseModel, conlist
from src.main.domain.model.MemberEnum import AgeGroupEnum, JobEnum, InterestEnum

class ProfileInputDto(BaseModel):
    name: str
    gender: bool
    age_range: str
    job: str
    interests: list[str]

    def validate_age_range(self):
        try:
            return next(age for age in AgeGroupEnum if age.value == self.age_range)
        except StopIteration:
            raise HTTPException(
                status_code=400,
                detail="유효하지 않은 나이대입니다. 가능한 값: " + ", ".join([age.value for age in AgeGroupEnum])
            )
    
    def validate_job(self):
        try:
            return next(job for job in JobEnum if job.value == self.job)
        except StopIteration:
            raise HTTPException(
                status_code=400,
                detail="유효하지 않은 직업입니다. 가능한 값: " + ", ".join([job.value for job in JobEnum])
            )
    
    def validate_interests(self):
        valid_interests = [interest.value for interest in InterestEnum]
        invalid_interests = [interest for interest in self.interests if interest not in valid_interests]
        if invalid_interests:
            raise HTTPException(
                status_code=400,
                detail=f"유효하지 않은 관심사입니다: {', '.join(invalid_interests)}"
            )
        return self.interests