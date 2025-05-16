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

class Day(BaseModel):
    date: date
    isDone: bool

class Days(BaseModel):
    days: List[Day]
