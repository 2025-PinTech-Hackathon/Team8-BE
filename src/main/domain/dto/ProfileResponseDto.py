from pydantic import BaseModel

class ProfileResponseDto(BaseModel):
    message: str
    user_id: str