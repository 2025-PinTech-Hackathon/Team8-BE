from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.main.domain.model.MemberChallengeRoom import member_challenge_room # 실제 Member 엔티티 경로에 따라 수정

class MemberChallengeRoomRepository:
    @staticmethod
    async def get_by_member_id(session: AsyncSession, member_id: str):
        result = await session.execute(
            select(member_challenge_room.c.room_id).where(member_challenge_room.c.member_id == member_id)
        )

        return result.scalars().all()