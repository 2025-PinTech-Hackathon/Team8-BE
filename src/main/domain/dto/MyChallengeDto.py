from typing import List, Optional
from pydantic import BaseModel
from datetime import date

class MyChallengeReqDto(BaseModel):
    roomId: int
