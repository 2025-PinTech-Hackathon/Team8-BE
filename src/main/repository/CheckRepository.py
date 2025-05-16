from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select, func
from src.main.domain.model.Check import Check

class CheckRepository:
    @staticmethod
    async def get_progress(session: AsyncSession, member_id: str, room_id: int) -> float:
        total_result = await session.execute(
            select(func.count()).select_from(Check)
            .where(Check.member_id == member_id, Check.room_id == room_id)
        )
        total_count = total_result.scalar()

        if total_count == 0:
            return 0.0

        done_result = await session.execute(
            select(func.count()).select_from(Check)
            .where(Check.member_id == member_id, Check.room_id == room_id, Check.done == True)
        )
        done_count = done_result.scalar()

        progress = (done_count / total_count) * 100
        return round(progress, 0)