from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.main.domain.model.MemberChallengeRoom import member_challenge_room # 실제 Member 엔티티 경로에 따라 수정
from src.main.domain.model.ChallengeRoom import ChallengeRoom

class MemberChallengeRoomRepository:
    @staticmethod
    async def get_by_member_id(session: AsyncSession, member_id: str):
        result = await session.execute(
            select(member_challenge_room.c.room_id).where(member_challenge_room.c.member_id == member_id)
        )

        return result.scalars().all()
    
    @staticmethod
    async def is_already_exist(session: AsyncSession, member_id: str, challenge_id: int):
        result = await session.execute(
            select(ChallengeRoom).where(
                ChallengeRoom.memberId == member_id,
                ChallengeRoom.challengeId == challenge_id
            )
        )

        existing_room = result.scalar_one_or_none()

        return existing_room