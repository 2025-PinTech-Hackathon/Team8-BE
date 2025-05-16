from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.main.domain.model.Challenge import Challenge

class ChallengeRepository:
    @staticmethod
    def get_by_challenge_id(session: AsyncSession, challenge_id: int):
        result = session.execute(
            select(Challenge).where(Challenge.challengeId == challenge_id)
        )

        return result.scalar_one_or_none() 