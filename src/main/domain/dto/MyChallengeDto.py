from typing import List, Optional
from pydantic import BaseModel
from datetime import date

class MyChallengeReqDto(BaseModel):
    roomId: int

class MyChallengeRoomResDto(BaseModel):
    title: str
    status: str
    content: str
    start: date
    end: date
    progress: int