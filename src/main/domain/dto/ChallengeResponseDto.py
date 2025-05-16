from typing import List
from pydantic import BaseModel

class ChallengeResponseDto(BaseModel):
    challengeId: int
    title: str
    description: str
    tag: str

class UserChallengeResponse(BaseModel):
    userName: str
    categories: List[str]
    challenges: List[ChallengeResponseDto]