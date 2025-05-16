from pydantic import BaseModel
from typing import List

class Feed(BaseModel):
    informationId: int
    title: str
    content: str
    tag: str

class UserInformationResponse(BaseModel):
    memberId: str
    userName: str
    categories: List[str]
    feeds: List[Feed]
