from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.main.domain.model.Member import Member  # 실제 Member 엔티티 경로에 따라 수정

class MemberRepository:
    @staticmethod
    def get_by_member_id(session: AsyncSession, member_id: str):
        result = session.execute(
            select(Member).where(Member.memberId == member_id)
        )

        return result.scalars().first()