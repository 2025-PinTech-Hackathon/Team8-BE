from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select, func
from src.main.domain.model.CheckTable import CheckTable

class CheckRepository:
    @staticmethod
    async def get_progress(session: AsyncSession, member_id: str, room_id: int) -> float:
        total_result = await session.execute(
            select(func.count()).select_from(CheckTable)
            .where(CheckTable.member_id == member_id, CheckTable.room_id == room_id)
        )
        total_count = total_result.scalar()

        if total_count == 0:
            return 0.0

        done_result = await session.execute(
            select(func.count()).select_from(CheckTable)
            .where(CheckTable.member_id == member_id, CheckTable.room_id == room_id, Check.done == True)
        )
        done_count = done_result.scalar()

        progress = (done_count / total_count) * 100
        return round(progress, 0)