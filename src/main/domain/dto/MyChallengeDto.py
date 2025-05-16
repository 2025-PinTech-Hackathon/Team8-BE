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

class Friend(BaseModel):
    friendId: str
    friendName: str
    progress: int

class FriendsProgress(BaseModel):
    friends: List[Friend]
class InviteCodeResponseDto(BaseModel):
    invitedCode: str

class ParticipateResponseDto(BaseModel):
    roomId: int
    status: str

class ParticipateRequestDto(BaseModel):
    code: str