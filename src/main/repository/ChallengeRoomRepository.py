from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.main.domain.model.ChallengeRoom import ChallengeRoom

class ChallengeRoomRepository:
    @staticmethod
    async def get_by_room_id(session: AsyncSession, room_id: int):
        result = await session.execute(
            select(ChallengeRoom).where(ChallengeRoom.roomId == room_id)
        )

        return result.scalars.all()