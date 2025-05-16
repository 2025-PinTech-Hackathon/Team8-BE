from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from src.main.domain.model.CheckTable import CheckTable

class CheckRepository:
    @staticmethod
    def get_progress(session: AsyncSession, member_id: str, room_id: int) -> float:
        # 총 체크 개수 (date와 done 모두 null이 아닌 항목만)
        total_result = session.execute(
            select(func.count()).select_from(CheckTable)
            .where(
                CheckTable.memberId == member_id,
                CheckTable.roomId == room_id,
                CheckTable.date.isnot(None),
                CheckTable.done.isnot(None)
            )
        )
        total_count = total_result.scalar()

        if total_count == 0:
            return 0.0

        # 완료된 체크 개수
        done_result = session.execute(
            select(func.count()).select_from(CheckTable)
            .where(
                CheckTable.memberId == member_id,
                CheckTable.roomId == room_id,
                CheckTable.date.isnot(None),
                CheckTable.done == True
            )
        )
        done_count = done_result.scalar()

        progress = (done_count / total_count) * 100
        return round(progress, 0)
    
    @staticmethod
    def get_friend_ids(session: AsyncSession, member_id: str, room_id: int):
        total_result = session.execute(
            select(CheckTable)
            .where(
                CheckTable.roomId == room_id,
                CheckTable.memberId != member_id
            )
        )

        return total_result.scalars().all()
