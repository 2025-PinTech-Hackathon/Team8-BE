from pydantic import BaseModel

class CreateRoomResDto(BaseModel):
    roomId: int