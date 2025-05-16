from typing import List
from pydantic import BaseModel, Field
from src.main.domain.model.MemberEnum import AgeGroupEnum, JobEnum, InterestEnum

class ProfileRequestDto(BaseModel):
    ame: str
    gender: bool  # 남자: False, 여자: True
    age_range: AgeGroupEnum
    job: JobEnum
    interests: List[InterestEnum]