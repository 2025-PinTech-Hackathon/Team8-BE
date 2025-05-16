from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.main.domain.model._MemberChallengeRoom import MemberChallengeRoom # 실제 Member 엔티티 경로에 따라 수정
from src.main.domain.model.ChallengeRoom import ChallengeRoom

class MemberChallengeRoomRepository:
    @staticmethod
    def get_by_member_id(session: AsyncSession, member_id: str):
        result = session.execute(
            select(MemberChallengeRoom).where(MemberChallengeRoom.memberId == member_id)
        )

        return result.scalars().all()
    
    @staticmethod
    def get_by_member_id_and_challenge_id(session: AsyncSession, member_id: str, challenge_id: int):
        result = session.execute(
            select(ChallengeRoom)
            .join(MemberChallengeRoom, ChallengeRoom.roomId == MemberChallengeRoom.roomId)
            .where(
                (MemberChallengeRoom.memberId == member_id) &
                (ChallengeRoom.challengeId == challenge_id)
            )
        )

        return result.scalars().all()
    
    @staticmethod
    def is_already_exist(session: AsyncSession, member_id: str, challenge_id: int):
        result = session.execute(
            select(ChallengeRoom).where(
                ChallengeRoom.memberId == member_id,
                ChallengeRoom.challengeId == challenge_id
            )
        )

        existing_room = result.scalar_one_or_none()

        return existing_room