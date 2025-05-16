from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.main.domain.model.ChallengeRoom import ChallengeRoom

class ChallengeRoomRepository:
    @staticmethod
    def get_by_room_id(session: AsyncSession, room_id: list[int]):
        result = session.execute(
            select(ChallengeRoom).where(ChallengeRoom.roomId.in_(room_id))
        )

        return result.scalars().all()
    
    @staticmethod
    def get_by_id(session: AsyncSession, room_id: int):
        result = session.execute(
            select(ChallengeRoom).where(ChallengeRoom.roomId == room_id)
        )

        return result.scalar_one_or_none() 