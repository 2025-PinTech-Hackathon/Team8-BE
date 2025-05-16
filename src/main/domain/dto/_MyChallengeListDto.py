from typing import List, Optional
from pydantic import BaseModel
from datetime import date

class MyChallengeSummaryDto(BaseModel):
    roomId: int
    title : str
    progress: float
    participantsNum: int
    start: Optional[date]
    end: Optional[date]

class MyChallengeListResDto(BaseModel):
    memberName: str
    tags: List[str]
    myChallenges: Optional[List[MyChallengeSummaryDto]]
