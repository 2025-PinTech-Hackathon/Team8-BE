from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.main.domain.model.ChallengeRoom import ChallengeRoom
from src.main.domain.model.CodeTable import CodeTable
from sqlalchemy import update

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
    
    @staticmethod
    def get_invite_code_by_room_id(session: AsyncSession, room_id: int) -> CodeTable | None:
        result = session.execute(
            select(CodeTable).where(CodeTable.roomId == room_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    def create_or_update_invite_code(session: AsyncSession, room_id: int, code: str) -> CodeTable:
        existing = ChallengeRoomRepository.get_invite_code_by_room_id(session, room_id)
        if existing:
            existing.code = code
            session.add(existing)
            return existing
        else:
            new_code = CodeTable(roomId=room_id, code=code)
            session.add(new_code)
            return new_code