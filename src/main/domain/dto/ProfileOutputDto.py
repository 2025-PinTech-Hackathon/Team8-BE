from pydantic import BaseModel
from typing import List

class ProfileOutputDto(BaseModel):
    name: str
    gender: str
    age_range: str
    job: str
    interests: List[str]

    class Config:
        from_attributes = True 